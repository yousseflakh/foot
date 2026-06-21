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

# CSS مخصص
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 10px;
    }
    .question-box {
        background: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 20px 0;
    }
    .correct-answer {
        background: #d4edda;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #28a745;
    }
    .wrong-answer {
        background: #f8d7da;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #dc3545;
    }
</style>
""", unsafe_allow_html=True)

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
                    
                    questions.append({
                        'question': question,
                        'options': options,
                        'correct': options.index(correct_answer),
                        'category': q['category'],
                        'correct_answer': correct_answer
                    })
                
                st.session_state.questions = questions
                st.session_state.current_q = 0
                st.session_state.score = 0
                st.session_state.total = 0
                st.session_state.correct = 0
                st.session_state.answered = False
                st.session_state.game_over = False
                st.session_state.message = ""
                return True
                
    except Exception as e:
        st.error(f"خطأ في الاتصال: {str(e)}")
    
    return False

def load_fallback_questions():
    """أسئلة احتياطية"""
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

# عرض العنوان
st.markdown('<h1 class="main-title">🧠 تحدي العقول</h1>', unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.markdown("## ⚙️ الإعدادات")
    
    difficulty = st.selectbox(
        "اختر الصعوبة:",
        ['easy', 'medium', 'hard'],
        format_func=lambda x: {'easy': 'سهل', 'medium': 'متوسط', 'hard': 'صعب'}[x],
        index=2
    )
    
    if st.button("🚀 بدء لعبة جديدة", use_container_width=True):
        st.session_state.difficulty = difficulty
        with st.spinner("جاري تحميل الأسئلة..."):
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

# المحتوى الرئيسي
if not st.session_state.questions:
    # شاشة البداية
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <h2>🎯 اختبر معرفتك!</h2>
            <p style="font-size: 1.1em; color: #666;">
                أسئلة ثقافية عامة من جميع المجالات
            </p>
            <p style="color: #999; margin-top: 20px;">
                📚 10 أسئلة في كل جولة<br>
                ⭐ 10 نقاط لكل إجابة صحيحة<br>
                🔥 اختر مستوى الصعوبة من القائمة الجانبية
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 ابدأ اللعب", use_container_width=True):
            with st.spinner("جاري تحميل الأسئلة..."):
                if not load_questions():
                    st.warning("⚠️ استخدام الأسئلة الاحتياطية")
                    load_fallback_questions()
            st.rerun()

else:
    # عرض الأسئلة
    if not st.session_state.game_over:
        q = st.session_state.questions[st.session_state.current_q]
        total = len(st.session_state.questions)
        
        # شريط التقدم
        st.progress((st.session_state.current_q) / total, text=f"السؤال {st.session_state.current_q + 1} من {total}")
        
        # الفئة
        st.markdown(f"<span style='background: #667eea; color: white; padding: 5px 15px; border-radius: 20px;'>{q['category']}</span>", unsafe_allow_html=True)
        
        # السؤال
        st.markdown(f"""
        <div class="question-box">
            <h3>❓ {q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # عرض الخيارات
        cols = st.columns(2)
        for i, option in enumerate(q['options']):
            with cols[i % 2]:
                if st.button(
                    option,
                    key=f"opt_{st.session_state.current_q}_{i}",
                    disabled=st.session_state.answered,
                    use_container_width=True
                ):
                    st.session_state.answered = True
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
                    st.session_state.message = ""
                    st.rerun()
                else:
                    st.session_state.game_over = True
                    st.rerun()
    
    else:
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
            with st.spinner("جاري تحميل الأسئلة..."):
                if not load_questions():
                    load_fallback_questions()
            st.rerun()

st.markdown("---")
st.caption("🧠 مصدر الأسئلة: Open Trivia DB | أسئلة لا متناهية")
