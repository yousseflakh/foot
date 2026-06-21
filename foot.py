import streamlit as st
import random
import requests
import re

# إعداد الصفحة
st.set_page_config(
    page_title="🧠 تحدي العقول - عربي",
    page_icon="🧠",
    layout="wide"
)

# CSS للخلفية السوداء
st.markdown("""
<style>
    .stApp {
        background-color: #0a0a0a !important;
    }
    
    div, p, h1, h2, h3, h4, h5, h6, span, label, .stMarkdown {
        color: #ffffff !important;
    }
    
    .css-1d391kg, .css-12oz5g7, section[data-testid="stSidebar"] {
        background-color: #1a1a1a !important;
    }
    
    .main-title {
        text-align: center;
        font-size: 2.8em;
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 15px;
        text-shadow: 0 0 30px rgba(0, 210, 255, 0.3);
    }
    
    .question-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #00d2ff;
        margin: 20px 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.5);
        border: 1px solid #2a2a4a;
    }
    
    .question-box h3 {
        color: #ffffff !important;
        font-size: 1.3em;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #1a1a2e 0%, #2a2a4a 100%) !important;
        color: #ffffff !important;
        border: 2px solid #3a3a5a !important;
        border-radius: 12px !important;
        padding: 14px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .stButton button:hover:not(:disabled) {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%) !important;
        border-color: #00d2ff !important;
        transform: scale(1.03);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.3);
    }
    
    .stButton button:disabled {
        opacity: 0.6 !important;
        cursor: not-allowed !important;
    }
    
    .stAlert {
        background: #1a1a2e !important;
        border-radius: 12px !important;
        padding: 15px !important;
        border: 1px solid #2a2a4a !important;
    }
    
    .stAlert div {
        color: #ffffff !important;
    }
    
    .stSuccess {
        border-left: 5px solid #00b894 !important;
    }
    
    .stError {
        border-left: 5px solid #e17055 !important;
    }
    
    .stMetric {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid #2a2a4a !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .stMetric div {
        color: #ffffff !important;
    }
    
    .stMetric label {
        color: #8899bb !important;
    }
    
    .stProgress > div > div {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%) !important;
        border-radius: 10px !important;
    }
    
    .stProgress > div {
        background: #1a1a2e !important;
        border-radius: 10px !important;
    }
    
    .category-badge {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%) !important;
        color: #ffffff !important;
        padding: 6px 18px !important;
        border-radius: 20px !important;
        display: inline-block !important;
        margin-bottom: 10px !important;
        font-weight: 600 !important;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.2);
    }
    
    .start-box {
        text-align: center;
        padding: 50px 30px;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
        border-radius: 20px;
        border: 1px solid #2a2a4a;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    }
    
    .start-box h2 {
        color: #ffffff !important;
        font-size: 2em;
    }
    
    .start-box p {
        color: #8899bb !important;
    }
    
    footer, .stCaption {
        color: #445566 !important;
    }
    
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1a1a2e !important;
        border-color: #2a2a4a !important;
        color: #ffffff !important;
    }
    
    .stSelectbox div[data-baseweb="select"] div {
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%) !important;
        border-color: #00d2ff !important;
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(0, 210, 255, 0.3);
    }
    
    .stSidebar .stMarkdown, .stSidebar div {
        color: #ffffff !important;
    }
    
    .stWarning {
        background: #1a1a2e !important;
        border-left: 5px solid #fdcb6e !important;
    }
    
    .stInfo {
        background: #1a1a2e !important;
        border-left: 5px solid #00d2ff !important;
    }
    
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }
    ::-webkit-scrollbar-thumb {
        background: #2a2a4a;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #3a7bd5;
    }
</style>
""", unsafe_allow_html=True)

# ==================== جلب الأسئلة من ويكيبيديا ====================
def fetch_wikipedia_articles():
    """جلب مقالات عشوائية من ويكيبيديا العربية"""
    try:
        # جلب قائمة بالمقالات العشوائية
        url = "https://ar.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'random',
            'rnnamespace': 0,
            'rnlimit': 20
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('query', {}).get('random', [])
            
            questions = []
            categories = ['تاريخ', 'علوم', 'جغرافيا', 'ثقافة', 'أدب']
            
            for article in articles:
                title = article.get('title', '')
                if len(title) > 5:  # تجاهل العناوين القصيرة
                    # إنشاء سؤال من عنوان المقال
                    correct_answer = title
                    
                    # جلب 3 خيارات خاطئة من مقالات أخرى
                    wrong_options = []
                    other_articles = [a.get('title', '') for a in articles if a.get('title') != title]
                    if len(other_articles) >= 3:
                        wrong_options = random.sample(other_articles, 3)
                    else:
                        # خيارات احتياطية
                        fallback = ['القاهرة', 'باريس', 'لندن', 'طوكيو', 'القمر', 'المريخ']
                        wrong_options = random.sample(fallback, 3)
                    
                    options = [correct_answer] + wrong_options
                    random.shuffle(options)
                    
                    questions.append({
                        'question': f'ما هو/ما هي "{title}"؟ (مقالة من ويكيبيديا)',
                        'options': options,
                        'correct': options.index(correct_answer),
                        'category': random.choice(categories),
                        'correct_answer': correct_answer
                    })
            
            return questions
    except Exception as e:
        st.error(f"⚠️ خطأ في جلب المقالات: {str(e)}")
    
    return None

def load_fallback_questions():
    """أسئلة احتياطية"""
    fallback = [
        {
            'question': 'ما هي عاصمة مصر؟',
            'options': ['الإسكندرية', 'القاهرة', 'الجيزة', 'الأقصر'],
            'correct': 1,
            'category': 'جغرافيا',
            'correct_answer': 'القاهرة'
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
            'question': 'ما هو أطول نهر في العالم؟',
            'options': ['نهر الأمازون', 'نهر النيل', 'نهر المسيسيبي', 'نهر اليانغتسي'],
            'correct': 1,
            'category': 'جغرافيا',
            'correct_answer': 'نهر النيل'
        },
        {
            'question': 'من هو مؤسس الدولة العثمانية؟',
            'options': ['عثمان الأول', 'أورخان الأول', 'مراد الأول', 'بايزيد الأول'],
            'correct': 0,
            'category': 'تاريخ',
            'correct_answer': 'عثمان الأول'
        }
    ]
    return fallback

# ==================== مكتبة الأسئلة المحلية ====================
LOCAL_QUESTIONS = [
    # تاريخ
    {
        'question': 'في أي عام سقطت الخلافة العثمانية؟',
        'options': ['1918', '1922', '1924', '1920'],
        'correct': 1,
        'category': 'تاريخ',
        'correct_answer': '1922'
    },
    {
        'question': 'من هو مؤسس الدولة العثمانية؟',
        'options': ['عثمان الأول', 'أورخان الأول', 'مراد الأول', 'بايزيد الأول'],
        'correct': 0,
        'category': 'تاريخ',
        'correct_answer': 'عثمان الأول'
    },
    {
        'question': 'في أي عام هبط الإنسان على سطح القمر؟',
        'options': ['1965', '1969', '1971', '1973'],
        'correct': 1,
        'category': 'تاريخ',
        'correct_answer': '1969'
    },
    {
        'question': 'ما هو أطول نهر في العالم؟',
        'options': ['نهر الأمازون', 'نهر النيل', 'نهر المسيسيبي', 'نهر اليانغتسي'],
        'correct': 1,
        'category': 'جغرافيا',
        'correct_answer': 'نهر النيل'
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
        'question': 'من هو شاعر المعلقات؟',
        'options': ['امرؤ القيس', 'عنترة بن شداد', 'زهير بن أبي سلمى', 'طرفة بن العبد'],
        'correct': 0,
        'category': 'أدب',
        'correct_answer': 'امرؤ القيس'
    }
]

# تهيئة حالة اللعبة
if 'questions' not in st.session_state:
    st.session_state.questions = []
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.correct = 0
    st.session_state.answered = False
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.selected = None
    st.session_state.source = 'local'

def load_questions_from_wikipedia(num=10):
    """تحميل أسئلة من ويكيبيديا"""
    with st.spinner("🌐 جاري جلب الأسئلة من ويكيبيديا..."):
        questions = fetch_wikipedia_articles()
        
        if questions and len(questions) >= num:
            selected = random.sample(questions, min(num, len(questions)))
            st.session_state.questions = selected
            st.session_state.source = 'wikipedia'
            return True
        else:
            st.warning("⚠️ استخدام الأسئلة المحلية")
            return False

def load_local_questions(num=10):
    """تحميل أسئلة محلية"""
    if len(LOCAL_QUESTIONS) >= num:
        questions = random.sample(LOCAL_QUESTIONS, num)
    else:
        questions = LOCAL_QUESTIONS.copy()
        random.shuffle(questions)
    
    st.session_state.questions = questions
    st.session_state.source = 'local'
    
    # إعادة تعيين الحالة
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.correct = 0
    st.session_state.answered = False
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.selected = None

# عرض العنوان
st.markdown('<h1 class="main-title">🧠 تحدي العقول - عربي</h1>', unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.markdown("## ⚙️ الإعدادات")
    st.markdown("---")
    
    # اختيار مصدر الأسئلة
    source = st.selectbox(
        "📚 مصدر الأسئلة:",
        ['محلي', 'ويكيبيديا (إنترنت)'],
        format_func=lambda x: x
    )
    
    # اختيار عدد الأسئلة
    num_questions = st.slider("📚 عدد الأسئلة:", 3, 15, 10)
    
    if st.button("🚀 بدء لعبة جديدة", use_container_width=True):
        if source == 'ويكيبيديا (إنترنت)':
            if not load_questions_from_wikipedia(num_questions):
                load_local_questions(num_questions)
                st.session_state.source = 'local (احتياطي)'
        else:
            load_local_questions(num_questions)
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
        
        if st.session_state.source == 'wikipedia':
            st.success("🌐 ويكيبيديا")
        elif st.session_state.source == 'local':
            st.info("📚 محلي")
        else:
            st.warning(f"📚 {st.session_state.source}")

# المحتوى الرئيسي
if not st.session_state.questions:
    # شاشة البداية
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="start-box">
            <h2>🎯 اختبر معرفتك!</h2>
            <p style="font-size: 1.1em; margin: 20px 0;">
                أسئلة ثقافية عامة بالعربية
            </p>
            <p style="color: #8899bb;">
                📚 اختر مصدر الأسئلة من القائمة الجانبية<br>
                🌐 ويكيبيديا: أسئلة من مقالات عربية<br>
                📖 محلي: أسئلة مكتوبة مسبقاً<br>
                ⭐ 10 نقاط لكل إجابة صحيحة
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button("🎮 ابدأ اللعب", use_container_width=True):
                if source == 'ويكيبيديا (إنترنت)':
                    if not load_questions_from_wikipedia(num_questions):
                        load_local_questions(num_questions)
                else:
                    load_local_questions(num_questions)
                st.rerun()

else:
    # عرض الأسئلة
    if not st.session_state.game_over and st.session_state.current_q < len(st.session_state.questions):
        q = st.session_state.questions[st.session_state.current_q]
        total = len(st.session_state.questions)
        
        # شريط التقدم
        st.progress((st.session_state.current_q) / total, text=f"السؤال {st.session_state.current_q + 1} من {total}")
        
        # الفئة
        st.markdown(f'<span class="category-badge">📌 {q["category"]}</span>', unsafe_allow_html=True)
        
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
                button_text = option
                
                if st.session_state.answered:
                    if i == q['correct']:
                        button_text = "✅ " + option
                    elif st.session_state.selected == i and i != q['correct']:
                        button_text = "❌ " + option
                
                if st.session_state.answered:
                    color = '#00b894' if '✅' in button_text else '#e17055' if '❌' in button_text else '#2a2a4a'
                    st.markdown(f"""
                    <div style="
                        background: {color};
                        padding: 14px;
                        border-radius: 12px;
                        border: 2px solid {color};
                        margin: 5px 0;
                        text-align: center;
                        color: white;
                        font-weight: 500;
                        opacity: 0.8;
                    ">
                        {button_text}
                    </div>
                    """, unsafe_allow_html=True)
                else:
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
                st.success(f"🎉 {st.session_state.message}")
            else:
                st.error(f"😅 {st.session_state.message}")
            
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
        st.markdown("---")
        if correct == total:
            st.success("🌟🌟🌟 **مذهل! إجابة كاملة! أنت عبقري!**")
        elif correct >= total * 0.7:
            st.success("⭐ **أداء ممتاز! استمر بهذا المستوى!**")
        elif correct >= total * 0.5:
            st.info("📚 **أداء جيد! مع مزيد من التدريب ستصبح أفضل!**")
        else:
            st.warning("💪 **لا تستسلم! الممارسة تصنع الإتقان!**")
        
        if st.button("🔄 لعب مرة أخرى", use_container_width=True):
            if source == 'ويكيبيديا (إنترنت)':
                if not load_questions_from_wikipedia(num_questions):
                    load_local_questions(num_questions)
            else:
                load_local_questions(num_questions)
            st.rerun()

st.markdown("---")
st.caption("📚 أسئلة عربية | 🌐 ويكيبيديا + 📖 محلي | نسخة 2.0")
