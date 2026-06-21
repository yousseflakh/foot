import streamlit as st
import requests
import random
import html

# إعداد الصفحة
st.set_page_config(
    page_title="🧠 تحدي العقول",
    page_icon="🧠",
    layout="wide"
)

# CSS مخصص لإصلاح مشاكل العرض
st.markdown("""
<style>
    /* إصلاح النص الأبيض */
    .stApp {
        background-color: #f0f2f6;
    }
    
    .main-title {
        text-align: center;
        font-size: 2.5em;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 10px;
        color: #000 !important;
    }
    
    .question-box {
        background: #ffffff !important;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 20px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .question-box h3 {
        color: #1a1a2e !important;
    }
    
    /* إصلاح ألوان النصوص */
    div, p, h1, h2, h3, h4, h5, h6, span, label {
        color: #1a1a2e !important;
    }
    
    /* إصلاح أزرار الخيارات */
    .stButton button {
        background: white !important;
        color: #1a1a2e !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        width: 100% !important;
        transition: all 0.3s !important;
        font-size: 16px !important;
    }
    
    .stButton button:hover:not(:disabled) {
        background: #667eea !important;
        color: white !important;
        border-color: #667eea !important;
        transform: scale(1.02);
    }
    
    .stButton button:disabled {
        opacity: 0.7 !important;
        cursor: not-allowed !important;
    }
    
    /* ألوان الإجابات */
    .correct-answer {
        background: #d4edda !important;
        border-color: #28a745 !important;
        color: #155724 !important;
    }
    
    .wrong-answer {
        background: #f8d7da !important;
        border-color: #dc3545 !important;
        color: #721c24 !important;
    }
    
    /* إصلاح الشريط الجانبي */
    .css-1d391kg, .css-12oz5g7 {
        background-color: #ffffff !important;
    }
    
    /* إصلاح رسائل النجاح والخطأ */
    .stAlert {
        background-color: #ffffff !important;
        border-radius: 10px !important;
        padding: 15px !important;
    }
    
    .stAlert div {
        color: #1a1a2e !important;
    }
    
    /* إصلاح المقاييس */
    .stMetric {
        background: white !important;
        padding: 15px !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
    }
    
    .stMetric div {
        color: #1a1a2e !important;
    }
    
    /* إصلاح شريط التقدم */
    .stProgress > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* إصلاح مربع الفئة */
    .category-badge {
        background: #667eea !important;
        color: white !important;
        padding: 5px 15px !important;
        border-radius: 20px !important;
        display: inline-block !important;
        margin-bottom: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# ترجمة الأسئلة إلى العربية (حل مؤقت)
def translate_question(q_data):
    """ترجمة الأسئلة من الإنجليزية إلى العربية"""
    # قاموس ترجمة بسيط للفئات
    categories = {
        'General Knowledge': 'معرفة عامة',
        'Science': 'علوم',
        'History': 'تاريخ',
        'Geography': 'جغرافيا',
        'Art': 'فن',
        'Literature': 'أدب',
        'Music': 'موسيقى',
        'Sports': 'رياضة',
        'Entertainment': 'ترفيه',
        'Mythology': 'أساطير',
        'Politics': 'سياسة',
        'Celebrities': 'مشاهير'
    }
    
    # ترجمة الفئة
    category = q_data.get('category', 'معرفة عامة')
    for eng, ar in categories.items():
        if eng in category:
            category = ar
            break
    
    return {
        'question': q_data['question'],
        'options': q_data['options'],
        'correct': q_data['correct'],
        'category': category,
        'correct_answer': q_data['correct_answer']
    }

# تهيئة حالة اللعبة
if 'questions' not in st.session_state:
    st.session_state.questions = []
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.correct = 0
    st.session_state.answered = False
    st.session_state.game_over = False
    st.session_state.difficulty = 'hard'
    st.session_state.message = ""
    st.session_state.use_fallback = False

def load_questions():
    """جلب الأسئلة من API"""
    try:
        url = f"https://opentdb.com/api.php?amount=10&difficulty={st.session_state.difficulty}&type=multiple"
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data['response_code'] == 0:
                questions = []
                for q in data['results']:
                    # تنظيف النص من رموز HTML
                    question = html.unescape(q['question'])
                    correct_answer = html.unescape(q['correct_answer'])
                    incorrect_answers = [html.unescape(a) for a in q['incorrect_answers']]
                    
                    # ترتيب الخيارات عشوائياً
                    options = [correct_answer] + incorrect_answers
                    random.shuffle(options)
                    
                    q_data = {
                        'question': question,
                        'options': options,
                        'correct': options.index(correct_answer),
                        'category': q['category'],
                        'correct_answer': correct_answer
                    }
                    
                    # ترجمة السؤال
                    q_data = translate_question(q_data)
                    questions.append(q_data)
                
                st.session_state.questions = questions
                st.session_state.current_q = 0
                st.session_state.score = 0
                st.session_state.total = 0
                st.session_state.correct = 0
                st.session_state.answered = False
                st.session_state.game_over = False
                st.session_state.message = ""
                st.session_state.use_fallback = False
                return True
                
    except Exception as e:
        st.error(f"⚠️ خطأ في الاتصال: {str(e)}")
    
    return False

def load_fallback_questions():
    """أسئلة احتياطية بالعربية"""
    questions = [
        {
            'question': 'ما هو أطول نهر في العالم؟',
            'options': ['نهر الأمازون', 'نهر النيل', 'نهر المسيسيبي', 'نهر اليانغتسي'],
            'correct': 1,
            'category': 'جغرافيا',
            'correct_answer': 'نهر النيل'
        },
        {
            'question': 'في أي عام هبط الإنسان على سطح القمر؟',
            'options': ['1965', '1969', '1971', '1973'],
            'correct': 1,
            'category': 'تاريخ',
            'correct_answer': '1969'
        },
        {
            'question': 'ما هي عاصمة اليابان؟',
            'options': ['بكين', 'سيئول', 'طوكيو', 'بانكوك'],
            'correct': 2,
            'category': 'جغرافيا',
            'correct_answer': 'طوكيو'
        },
        {
            'question': 'من هو مخترع المصباح الكهربائي؟',
            'options': ['توماس أديسون', 'نيكولا تسلا', 'ألبرت أينشتاين', 'غراهام بيل'],
            'correct': 0,
            'category': 'علوم',
            'correct_answer': 'توماس أديسون'
        },
        {
            'question': 'كم عدد الكواكب في المجموعة الشمسية؟',
            'options': ['7', '8', '9', '10'],
            'correct': 1,
            'category': 'علوم',
            'correct_answer': '8'
        },
        {
            'question': 'ما هي اللغة الأكثر تحدثاً في العالم كلغة أم؟',
            'options': ['الإنجليزية', 'الإسبانية', 'الصينية الماندرين', 'الهندية'],
            'correct': 2,
            'category': 'ثقافة',
            'correct_answer': 'الصينية الماندرين'
        },
        {
            'question': 'من هو مؤسس علم الجبر؟',
            'options': ['الخوارزمي', 'ابن سينا', 'الفارابي', 'البيروني'],
            'correct': 0,
            'category': 'تاريخ',
            'correct_answer': 'الخوارزمي'
        },
        {
            'question': 'ما هو أسرع حيوان بري؟',
            'options': ['الأسد', 'الغزال', 'الفهد', 'الأرنب'],
            'correct': 2,
            'category': 'علوم',
            'correct_answer': 'الفهد'
        },
        {
            'question': 'من هو مؤلف رواية "الجريمة والعقاب"؟',
            'options': ['فيودور دوستويفسكي', 'ليو تولستوي', 'أنطون تشيخوف', 'نيكولاي غوغول'],
            'correct': 0,
            'category': 'أدب',
            'correct_answer': 'فيودور دوستويفسكي'
        },
        {
            'question': 'ما هي أصغر دولة في العالم من حيث المساحة؟',
            'options': ['الفاتيكان', 'موناكو', 'ناورو', 'سان مارينو'],
            'correct': 0,
            'category': 'جغرافيا',
            'correct_answer': 'الفاتيكان'
        }
    ]
    
    st.session_state.questions = questions
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.correct = 0
    st.session_state.answered = False
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.use_fallback = True

# عرض العنوان
st.markdown('<h1 class="main-title">🧠 تحدي العقول</h1>', unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.markdown("## ⚙️ الإعدادات")
    
    difficulty = st.selectbox(
        "اختر الصعوبة:",
        ['easy', 'medium', 'hard'],
        format_func=lambda x: {'easy': '🟢 سهل', 'medium': '🟡 متوسط', 'hard': '🔴 صعب'}[x],
        index=2
    )
    
    if st.button("🚀 بدء لعبة جديدة", use_container_width=True):
        st.session_state.difficulty = difficulty
        with st.spinner("⏳ جاري تحميل الأسئلة..."):
            if not load_questions():
                st.warning("⚠️ استخدام الأسئلة الاحتياطية")
                load_fallback_questions()
        st.rerun()
    
    st.markdown("---")
    
    if st.session_state.total > 0:
        st.markdown("## 📊 الإحصائيات")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("⭐ النقاط", st.session_state.score)
        with col2:
            pct = (st.session_state.correct / st.session_state.total * 100) if st.session_state.total > 0 else 0
            st.metric("✅ النجاح", f"{pct:.0f}%")
        
        st.metric("📝 الإجابات", f"{st.session_state.correct}/{st.session_state.total}")
        
        if st.session_state.use_fallback:
            st.info("📡 وضع عدم الاتصال")

# المحتوى الرئيسي
if not st.session_state.questions:
    # شاشة البداية
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 40px 0; background: white; border-radius: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h2 style="color: #1a1a2e;">🎯 اختبر معرفتك!</h2>
            <p style="font-size: 1.1em; color: #555; margin: 20px 0;">
                أسئلة ثقافية عامة من جميع المجالات
            </p>
            <p style="color: #777;">
                📚 10 أسئلة في كل جولة<br>
                ⭐ 10 نقاط لكل إجابة صحيحة<br>
                🔥 اختر مستوى الصعوبة من القائمة الجانبية
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 ابدأ اللعب", use_container_width=True):
            with st.spinner("⏳ جاري تحميل الأسئلة..."):
                if not load_questions():
                    st.warning("⚠️ استخدام الأسئلة الاحتياطية")
                    load_fallback_questions()
            st.rerun()

else:
    # عرض الأسئلة
    if not st.session_state.game_over and st.session_state.current_q < len(st.session_state.questions):
        q = st.session_state.questions[st.session_state.current_q]
        total = len(st.session_state.questions)
        
        # شريط التقدم
        st.progress((st.session_state.current_q) / total, text=f"السؤال {st.session_state.current_q + 1} من {total}")
        
        # الفئة
        st.markdown(f'<span class="category-badge">{q["category"]}</span>', unsafe_allow_html=True)
        
        # السؤال
        st.markdown(f"""
        <div class="question-box">
            <h3 style="color: #1a1a2e;">❓ {q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # عرض الخيارات
        cols = st.columns(2)
        for i, option in enumerate(q['options']):
            with cols[i % 2]:
                # تحديد نمط الزر بعد الإجابة
                button_text = option
                if st.session_state.answered:
                    if i == q['correct']:
                        button_text = "✅ " + option
                    elif st.session_state.selected == i:
                        button_text = "❌ " + option
                
                if st.button(
                    button_text,
                    key=f"opt_{st.session_state.current_q}_{i}",
                    disabled=st.session_state.answered,
                    use_container_width=True
                ):
                    st.session_state.answered = True
                    st.session_state.selected = i
                    st.session_state.total += 1
                    
                    if i == q['correct']:
                        st.session_state.score += 10
                        st.session_state.correct += 1
                        st.session_state.message = f"✅ صحيح! +10 نقاط"
                    else:
                        st.session_state.message = f"❌ خطأ! الإجابة الصحيحة: {q['correct_answer']}"
                    
                    st.rerun()
        
        # عرض التغذية الراجعة
        if st.session_state.answered:
            st.markdown("---")
            
            if "صحيح" in st.session_state.message:
                st.success(st.session_state.message)
            else:
                st.error(st.session_state.message)
            
            if st.button("⏩ السؤال التالي", use_container_width=True):
                if st.session_state.current_q + 1 < len(st.session_state.questions):
                    st.session_state.current_q += 1
                    st.session_state.answered = False
                    st.session_state.selected = None
                    st.session_state.message = ""
                    st.rerun()
                else:
                    st.session_state.game_over = True
                    st.rerun()
    
    elif st.session_state.game_over or st.session_state.current_q >= len(st.session_state.questions):
        # نهاية اللعبة
        st.markdown("---")
        st.markdown("## 🏆 انتهت اللعبة!")
        
        total = len(st.session_state.questions)
        correct = st.session_state.correct
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ الإجابات الصحيحة", f"{correct}/{total}")
        with col2:
            pct = (correct / total * 100) if total > 0 else 0
            st.metric("📊 نسبة النجاح", f"{pct:.0f}%")
        with col3:
            st.metric("⭐ مجموع النقاط", st.session_state.score)
        
        # تقييم الأداء
        if correct == total:
            st.success("🌟🌟🌟 **مذهل! إجابة كاملة! أنت عبقري!**")
        elif correct >= total * 0.7:
            st.success("⭐ **أداء ممتاز! استمر بهذا المستوى!**")
        elif correct >= total * 0.5:
            st.info("📚 **أداء جيد! مع مزيد من التدريب ستصبح أفضل!**")
        else:
            st.warning("💪 **لا تستسلم! الممارسة تصنع الإتقان!**")
        
        if st.button("🔄 لعب مرة أخرى", use_container_width=True):
            with st.spinner("⏳ جاري تحميل الأسئلة..."):
                if not load_questions():
                    load_fallback_questions()
            st.rerun()

st.markdown("---")
st.caption("🧠 مصدر الأسئلة: Open Trivia DB | أسئلة لا متناهية")
