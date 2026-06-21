import streamlit as st
import random
import requests
import re
import html
from datetime import datetime

# إعداد الصفحة
st.set_page_config(
    page_title="🧠 تحدي العقول - صعب جداً",
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
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 15px;
        text-shadow: 0 0 30px rgba(245, 87, 108, 0.3);
    }
    
    .question-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #f5576c;
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
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        border-color: #f5576c !important;
        transform: scale(1.03);
        box-shadow: 0 0 30px rgba(245, 87, 108, 0.3);
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
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        border-radius: 10px !important;
    }
    
    .stProgress > div {
        background: #1a1a2e !important;
        border-radius: 10px !important;
    }
    
    .category-badge {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        color: #ffffff !important;
        padding: 6px 18px !important;
        border-radius: 20px !important;
        display: inline-block !important;
        margin-bottom: 10px !important;
        font-weight: 600 !important;
        box-shadow: 0 0 20px rgba(245, 87, 108, 0.2);
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
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        border-color: #f5576c !important;
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(245, 87, 108, 0.3);
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
        border-left: 5px solid #f093fb !important;
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
        background: #f5576c;
    }
    
    .difficulty-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: bold;
        margin-left: 10px;
    }
    .difficulty-hard {
        background: #f5576c;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==================== جلب الأسئلة الصعبة من ويكيبيديا ====================
def fetch_wikipedia_articles(limit=30):
    """جلب مقالات عشوائية من ويكيبيديا العربية"""
    try:
        url = "https://ar.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'random',
            'rnnamespace': 0,
            'rnlimit': limit
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('query', {}).get('random', [])
            return articles
    except Exception as e:
        st.error(f"⚠️ خطأ في جلب المقالات: {str(e)}")
    
    return []

def fetch_article_details(title):
    """جلب تفاصيل المقال للحصول على معلومات أكثر"""
    try:
        url = "https://ar.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'titles': title,
            'prop': 'extracts|info',
            'explaintext': True,
            'exintro': True
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            pages = data.get('query', {}).get('pages', {})
            for page_id, page_data in pages.items():
                if 'extract' in page_data:
                    return page_data['extract']
    except:
        pass
    return None

def generate_hard_questions(num_questions=10):
    """توليد أسئلة صعبة من ويكيبيديا"""
    questions = []
    
    # جلب مقالات عشوائية
    articles = fetch_wikipedia_articles(limit=num_questions * 3)
    
    if not articles:
        return None
    
    # تصنيفات عشوائية
    categories = ['تاريخ', 'علوم', 'جغرافيا', 'ثقافة', 'أدب', 'فلسفة', 'سياسة', 'اقتصاد']
    
    for article in articles[:num_questions * 2]:
        title = article.get('title', '')
        
        # تجاهل العناوين القصيرة أو غير المناسبة
        if len(title) < 8 or len(title) > 60:
            continue
        
        # جلب تفاصيل المقال
        extract = fetch_article_details(title)
        
        # أنواع مختلفة من الأسئلة الصعبة
        question_types = [
            f'ما هو/من هو "{title}" في التاريخ؟',
            f'ماذا تعرف عن "{title}"؟',
            f'في أي مجال اشتهر "{title}"؟',
            f'ما هي أهمية "{title}" في الثقافة العربية؟',
            f'من هو الشخصية المعروفة "{title}"؟'
        ]
        
        # جلب 3 خيارات خاطئة من مقالات أخرى
        other_articles = [a.get('title', '') for a in articles if a.get('title') != title]
        wrong_options = random.sample(other_articles, min(3, len(other_articles)))
        
        # إذا لم تكن هناك خيارات كافية، استخدم خيارات احتياطية صعبة
        if len(wrong_options) < 3:
            fallback_hard = [
                'ابن خلدون', 'الفارابي', 'البيروني', 'الكندي', 'الرازي',
                'الخوارزمي', 'ابن سينا', 'الغزالي', 'ابن رشد', 'ابن عربي',
                'المتنبي', 'أبو تمام', 'الفرزدق', 'جرير', 'الأخطل',
                'هارون الرشيد', 'المأمون', 'المنصور', 'المهدي', 'الأمين'
            ]
            additional = [f for f in fallback_hard if f not in wrong_options and f != title]
            wrong_options.extend(random.sample(additional, min(3 - len(wrong_options), len(additional))))
        
        # خلط الخيارات
        options = [title] + wrong_options[:3]
        random.shuffle(options)
        
        questions.append({
            'question': random.choice(question_types),
            'options': options,
            'correct': options.index(title),
            'category': random.choice(categories),
            'correct_answer': title,
            'difficulty': 'صعب جداً',
            'extract': extract[:200] + '...' if extract else ''
        })
        
        if len(questions) >= num_questions:
            break
    
    return questions

# ==================== أسئلة محلية صعبة جداً ====================
HARD_LOCAL_QUESTIONS = [
    # تاريخ صعب
    {
        'question': 'في أي عام تم سقوط الأندلس نهائياً؟',
        'options': ['1492', '1493', '1494', '1495'],
        'correct': 0,
        'category': 'تاريخ',
        'correct_answer': '1492',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'من هو الخليفة الأموي الذي بنى قبة الصخرة؟',
        'options': ['عبد الملك بن مروان', 'الوليد بن عبد الملك', 'سليمان بن عبد الملك', 'عمر بن عبد العزيز'],
        'correct': 0,
        'category': 'تاريخ',
        'correct_answer': 'عبد الملك بن مروان',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'في أي عام وقعت معركة عين جالوت؟',
        'options': ['1260', '1261', '1262', '1263'],
        'correct': 0,
        'category': 'تاريخ',
        'correct_answer': '1260',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'من هو مؤسس الدولة الفاطمية؟',
        'options': ['عبيد الله المهدي', 'المعز لدين الله', 'الحاكم بأمر الله', 'المنصور بالله'],
        'correct': 0,
        'category': 'تاريخ',
        'correct_answer': 'عبيد الله المهدي',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'في أي عام تم فتح القسطنطينية؟',
        'options': ['1453', '1454', '1455', '1456'],
        'correct': 0,
        'category': 'تاريخ',
        'correct_answer': '1453',
        'difficulty': 'صعب جداً'
    },
    
    # علوم صعبة
    {
        'question': 'من هو مكتشف الدورة الدموية الصغرى؟',
        'options': ['ابن النفيس', 'جالينوس', 'ابن سينا', 'الرازي'],
        'correct': 0,
        'category': 'علوم',
        'correct_answer': 'ابن النفيس',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'ما هي السرعة التي يحتاجها جسم للهروب من جاذبية الأرض؟',
        'options': ['11.2 كم/ث', '12.2 كم/ث', '10.2 كم/ث', '13.2 كم/ث'],
        'correct': 0,
        'category': 'علوم',
        'correct_answer': '11.2 كم/ث',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'من هو مؤسس علم المناعة؟',
        'options': ['ابن زهر', 'الرازي', 'ابن سينا', 'ابن النفيس'],
        'correct': 0,
        'category': 'علوم',
        'correct_answer': 'ابن زهر',
        'difficulty': 'صعب جداً'
    },
    
    # جغرافيا صعبة
    {
        'question': 'ما هي أعلى قمة جبلية في أفريقيا؟',
        'options': ['جبل كليمنجارو', 'جبل كينيا', 'جبل راس دشين', 'جبل كروجر'],
        'correct': 0,
        'category': 'جغرافيا',
        'correct_answer': 'جبل كليمنجارو',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'ما هو أعمق نقطة في المحيطات؟',
        'options': ['خندق ماريانا', 'خندق بورتوريكو', 'خندق تونغا', 'خندق كوريل'],
        'correct': 0,
        'category': 'جغرافيا',
        'correct_answer': 'خندق ماريانا',
        'difficulty': 'صعب جداً'
    },
    
    # أدب صعب
    {
        'question': 'من هو صاحب ديوان "الحماسة"؟',
        'options': ['أبو تمام', 'المتنبي', 'الفرزدق', 'جرير'],
        'correct': 0,
        'category': 'أدب',
        'correct_answer': 'أبو تمام',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'من هو مؤلف كتاب "الكامل في التاريخ"؟',
        'options': ['ابن الأثير', 'الطبري', 'ابن كثير', 'ابن خلدون'],
        'correct': 0,
        'category': 'أدب',
        'correct_answer': 'ابن الأثير',
        'difficulty': 'صعب جداً'
    },
    
    # دين صعب
    {
        'question': 'من هو الصحابي الملقب بـ "الفاروق"؟',
        'options': ['عمر بن الخطاب', 'أبو بكر الصديق', 'عثمان بن عفان', 'علي بن أبي طالب'],
        'correct': 0,
        'category': 'دين',
        'correct_answer': 'عمر بن الخطاب',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'ما هي السورة التي تسمى "قلب القرآن"؟',
        'options': ['سورة يس', 'سورة الفاتحة', 'سورة الإخلاص', 'سورة الكوثر'],
        'correct': 0,
        'category': 'دين',
        'correct_answer': 'سورة يس',
        'difficulty': 'صعب جداً'
    },
    
    # ثقافة عامة صعبة
    {
        'question': 'من هو مؤسس علم العروض؟',
        'options': ['الخليل بن أحمد', 'سيبويه', 'الفراهيدي', 'الأصمعي'],
        'correct': 0,
        'category': 'ثقافة',
        'correct_answer': 'الخليل بن أحمد',
        'difficulty': 'صعب جداً'
    },
    {
        'question': 'ما هي أول دولة عربية اعترفت بالولايات المتحدة؟',
        'options': ['المغرب', 'مصر', 'السعودية', 'تونس'],
        'correct': 0,
        'category': 'سياسة',
        'correct_answer': 'المغرب',
        'difficulty': 'صعب جداً'
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
    st.session_state.total_questions_loaded = 0

def load_hard_questions(num=10):
    """تحميل أسئلة صعبة"""
    # محاولة جلب من ويكيبيديا أولاً
    with st.spinner("🌐 جاري جلب أسئلة صعبة من ويكيبيديا..."):
        questions = generate_hard_questions(num)
        
        if questions and len(questions) >= num:
            st.session_state.questions = questions[:num]
            st.session_state.source = 'ويكيبيديا (صعب)'
            st.session_state.total_questions_loaded = len(questions)
            return True
    
    # استخدام الأسئلة المحلية الصعبة
    st.warning("⚠️ استخدام الأسئلة المحلية الصعبة")
    available = HARD_LOCAL_QUESTIONS.copy()
    
    # إذا كان الطلب أكثر من المتاح، كرر الأسئلة
    if len(available) < num:
        while len(available) < num:
            available.extend(random.sample(HARD_LOCAL_QUESTIONS, min(num - len(available), len(HARD_LOCAL_QUESTIONS))))
    
    selected = random.sample(available, num)
    st.session_state.questions = selected
    st.session_state.source = 'محلي (صعب جداً)'
    st.session_state.total_questions_loaded = len(selected)
    return True

def load_more_questions():
    """تحميل المزيد من الأسئلة (لا محدود)"""
    current_count = len(st.session_state.questions)
    new_questions = generate_hard_questions(10)
    
    if new_questions:
        # إضافة أسئلة جديدة إلى القائمة الحالية
        st.session_state.questions.extend(new_questions)
        st.session_state.total_questions_loaded = len(st.session_state.questions)
        return True
    else:
        # استخدام أسئلة محلية
        new_local = random.sample(HARD_LOCAL_QUESTIONS, min(10, len(HARD_LOCAL_QUESTIONS)))
        st.session_state.questions.extend(new_local)
        st.session_state.total_questions_loaded = len(st.session_state.questions)
        return True

# عرض العنوان
st.markdown('<h1 class="main-title">🧠 تحدي العقول - صعب جداً</h1>', unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.markdown("## ⚙️ الإعدادات")
    st.markdown("---")
    
    num_questions = st.slider("📚 عدد الأسئلة في الجولة:", 5, 30, 10)
    
    if st.button("🚀 بدء لعبة جديدة", use_container_width=True):
        load_hard_questions(num_questions)
        st.rerun()
    
    st.markdown("---")
    
    if st.session_state.questions:
        if st.button("➕ تحميل المزيد من الأسئلة", use_container_width=True):
            with st.spinner("جاري تحميل المزيد..."):
                load_more_questions()
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
        st.metric("📚 إجمالي الأسئلة المحملة", st.session_state.total_questions_loaded)
        
        if st.session_state.source:
            st.info(f"📌 المصدر: {st.session_state.source}")

# المحتوى الرئيسي
if not st.session_state.questions:
    # شاشة البداية
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="start-box">
            <h2>🎯 تحدى نفسك!</h2>
            <p style="font-size: 1.1em; margin: 20px 0; color: #f5576c;">
                🔥 أسئلة صعبة جداً للمحترفين فقط
            </p>
            <p style="color: #8899bb;">
                📚 أسئلة من ويكيبيديا العربية<br>
                🧠 أسئلة تاريخية وعلمية وأدبية<br>
                ⭐ 10 نقاط لكل إجابة صحيحة<br>
                ➕ يمكنك تحميل المزيد من الأسئلة<br>
                📖 أسئلة غير محدودة
            </p>
            <div style="margin-top: 20px; padding: 10px; background: #2a1a2e; border-radius: 10px; border: 1px solid #f5576c;">
                <span style="color: #f5576c;">⚠️ تحذير: هذه الأسئلة مخصصة للخبراء</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 ابدأ التحدي", use_container_width=True):
            load_hard_questions(num_questions)
            st.rerun()

else:
    # عرض الأسئلة
    if not st.session_state.game_over and st.session_state.current_q < len(st.session_state.questions):
        q = st.session_state.questions[st.session_state.current_q]
        total = len(st.session_state.questions)
        
        # شريط التقدم
        st.progress((st.session_state.current_q) / total, text=f"السؤال {st.session_state.current_q + 1} من {total}")
        
        # الفئة والصعوبة
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f'<span class="category-badge">📌 {q["category"]}</span>', unsafe_allow_html=True)
        with col2:
            difficulty = q.get('difficulty', 'صعب')
            st.markdown(f'<span style="background: #f5576c; color: white; padding: 4px 12px; border-radius: 15px; float: right;">🔥 {difficulty}</span>', unsafe_allow_html=True)
        
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
            
            # عرض معلومات إضافية عن الإجابة
            if 'extract' in q and q['extract']:
                with st.expander("📖 معلومات إضافية"):
                    st.write(q['extract'])
            
            col1, col2 = st.columns(2)
            with col1:
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
            with col2:
                if st.button("➕ تحميل المزيد", use_container_width=True):
                    with st.spinner("جاري تحميل المزيد..."):
                        load_more_questions()
                    st.rerun()
    
    elif st.session_state.game_over or st.session_state.current_q >= len(st.session_state.questions):
        # نهاية اللعبة
        st.markdown("---")
        st.markdown("## 🏆 انتهى التحدي!")
        
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
            st.success("🌟🌟🌟 **عبقري! إجابة كاملة في أسئلة صعبة جداً!**")
        elif correct >= total * 0.7:
            st.success("⭐ **أداء ممتاز! أنت خبير حقيقي!**")
        elif correct >= total * 0.5:
            st.info("📚 **أداء جيد! مع المزيد ستصل للاحتراف!**")
        else:
            st.warning("💪 **لا تستسلم! هذه الأسئلة صعبة فعلاً!**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 لعب مرة أخرى", use_container_width=True):
                load_hard_questions(num_questions)
                st.rerun()
        with col2:
            if st.button("➕ تحميل المزيد", use_container_width=True):
                with st.spinner("جاري تحميل المزيد..."):
                    load_more_questions()
                    st.session_state.game_over = False
                st.rerun()

st.markdown("---")
