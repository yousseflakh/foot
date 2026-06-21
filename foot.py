import streamlit as st
import random
import requests
import json
import os
from datetime import datetime

# إعداد الصفحة
st.set_page_config(
    page_title="🧠 تحدي العقول",
    page_icon="🧠",
    layout="wide"
)

# CSS
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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 15px;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
    }
    .question-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%) !important;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #667eea;
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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border-color: #667eea !important;
        transform: scale(1.03);
        box-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border-radius: 10px !important;
    }
    .stProgress > div {
        background: #1a1a2e !important;
        border-radius: 10px !important;
    }
    .category-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: #ffffff !important;
        padding: 6px 18px !important;
        border-radius: 20px !important;
        display: inline-block !important;
        margin-bottom: 10px !important;
        font-weight: 600 !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.2);
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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border-color: #667eea !important;
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
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
        border-left: 5px solid #667eea !important;
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
        background: #667eea;
    }
    .difficulty-easy {
        background: #00b894 !important;
        color: white !important;
        padding: 4px 12px !important;
        border-radius: 15px !important;
        float: right !important;
    }
    .difficulty-medium {
        background: #fdcb6e !important;
        color: #1a1a2e !important;
        padding: 4px 12px !important;
        border-radius: 15px !important;
        float: right !important;
    }
    .difficulty-hard {
        background: #e17055 !important;
        color: white !important;
        padding: 4px 12px !important;
        border-radius: 15px !important;
        float: right !important;
    }
    .difficulty-expert {
        background: #f5576c !important;
        color: white !important;
        padding: 4px 12px !important;
        border-radius: 15px !important;
        float: right !important;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.6; }
        100% { opacity: 1; }
    }
    .leaderboard-item {
        display: flex;
        justify-content: space-between;
        padding: 10px 15px;
        margin: 5px 0;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 10px;
        border: 1px solid #2a2a4a;
        transition: all 0.3s;
    }
    .leaderboard-item:hover {
        border-color: #667eea;
        transform: scale(1.02);
    }
    .leaderboard-rank {
        font-weight: bold;
        color: #667eea;
        min-width: 40px;
    }
    .leaderboard-name {
        flex: 1;
        margin: 0 15px;
    }
    .leaderboard-score {
        font-weight: bold;
        color: #00b894;
    }
    .leaderboard-date {
        color: #8899bb;
        font-size: 0.8em;
        margin-left: 15px;
    }
    .top-rank {
        background: linear-gradient(135deg, #2a1a2e 0%, #1a2a2e 100%) !important;
        border-color: #667eea !important;
    }
    .end-game-btn {
        background: linear-gradient(135deg, #f5576c 0%, #e17055 100%) !important;
        border-color: #f5576c !important;
        color: white !important;
    }
    .end-game-btn:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 0 30px rgba(245, 87, 108, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# ==================== نظام تخزين النتائج ====================
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_leaderboard(leaderboard):
    try:
        with open(LEADERBOARD_FILE, 'w', encoding='utf-8') as f:
            json.dump(leaderboard, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False

def add_score_to_leaderboard(name, score, correct, total, difficulty):
    leaderboard = load_leaderboard()
    
    leaderboard.append({
        'name': name,
        'score': score,
        'correct': correct,
        'total': total,
        'difficulty': difficulty,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    if len(leaderboard) > 100:
        leaderboard = leaderboard[:100]
    
    save_leaderboard(leaderboard)
    return leaderboard

def get_player_rank(name):
    leaderboard = load_leaderboard()
    for i, entry in enumerate(leaderboard):
        if entry['name'] == name:
            return i + 1
    return None

# ==================== الأسئلة بمستويات صعوبة متنوعة ====================
QUESTIONS_BY_DIFFICULTY = {
    'سهل': [
        {'question': 'ما هي عاصمة مصر؟', 'options': ['الإسكندرية', 'القاهرة', 'الجيزة', 'الأقصر'], 'correct': 1, 'category': 'جغرافيا', 'correct_answer': 'القاهرة'},
        {'question': 'كم عدد الكواكب في المجموعة الشمسية؟', 'options': ['7', '8', '9', '10'], 'correct': 1, 'category': 'علوم', 'correct_answer': '8'},
        {'question': 'ما هي عاصمة السعودية؟', 'options': ['جدة', 'الرياض', 'مكة', 'الدمام'], 'correct': 1, 'category': 'جغرافيا', 'correct_answer': 'الرياض'},
        {'question': 'من هو النبي الذي أنزل عليه التوراة؟', 'options': ['موسى', 'عيسى', 'محمد', 'إبراهيم'], 'correct': 0, 'category': 'دين', 'correct_answer': 'موسى'},
        {'question': 'ما هي عاصمة فرنسا؟', 'options': ['لندن', 'باريس', 'برلين', 'مدريد'], 'correct': 1, 'category': 'جغرافيا', 'correct_answer': 'باريس'},
        {'question': 'ما هو لون الدم؟', 'options': ['أزرق', 'أحمر', 'أخضر', 'أصفر'], 'correct': 1, 'category': 'علوم', 'correct_answer': 'أحمر'},
        {'question': 'كم عدد أركان الإسلام؟', 'options': ['3', '4', '5', '6'], 'correct': 2, 'category': 'دين', 'correct_answer': '5'},
        {'question': 'ما هي عاصمة الأردن؟', 'options': ['عمان', 'الزرقاء', 'إربد', 'العقبة'], 'correct': 0, 'category': 'جغرافيا', 'correct_answer': 'عمان'},
    ],
    'متوسط': [
        {'question': 'في أي عام هبط الإنسان على سطح القمر؟', 'options': ['1965', '1969', '1971', '1973'], 'correct': 1, 'category': 'تاريخ', 'correct_answer': '1969'},
        {'question': 'من هو مخترع المصباح الكهربائي؟', 'options': ['توماس أديسون', 'نيكولا تسلا', 'ألبرت أينشتاين', 'غراهام بيل'], 'correct': 0, 'category': 'علوم', 'correct_answer': 'توماس أديسون'},
        {'question': 'ما هو أطول نهر في العالم؟', 'options': ['نهر الأمازون', 'نهر النيل', 'نهر المسيسيبي', 'نهر اليانغتسي'], 'correct': 1, 'category': 'جغرافيا', 'correct_answer': 'نهر النيل'},
        {'question': 'من هو مؤسس الدولة العثمانية؟', 'options': ['عثمان الأول', 'أورخان الأول', 'مراد الأول', 'بايزيد الأول'], 'correct': 0, 'category': 'تاريخ', 'correct_answer': 'عثمان الأول'},
        {'question': 'ما هي عملة المملكة المتحدة؟', 'options': ['دولار', 'يورو', 'جنيه إسترليني', 'فرنك'], 'correct': 2, 'category': 'اقتصاد', 'correct_answer': 'جنيه إسترليني'},
        {'question': 'ما هي عاصمة أستراليا؟', 'options': ['سيدني', 'ملبورن', 'كانبرا', 'بريسبان'], 'correct': 2, 'category': 'جغرافيا', 'correct_answer': 'كانبرا'},
        {'question': 'من هو مؤلف رواية "البؤساء"؟', 'options': ['فيكتور هوغو', 'ألكسندر دوماس', 'جول فيرن', 'إميل زولا'], 'correct': 0, 'category': 'أدب', 'correct_answer': 'فيكتور هوغو'},
    ],
    'صعب': [
        {'question': 'في أي عام تم سقوط الأندلس نهائياً؟', 'options': ['1492', '1493', '1494', '1495'], 'correct': 0, 'category': 'تاريخ', 'correct_answer': '1492'},
        {'question': 'من هو الخليفة الأموي الذي بنى قبة الصخرة؟', 'options': ['عبد الملك بن مروان', 'الوليد بن عبد الملك', 'سليمان بن عبد الملك', 'عمر بن عبد العزيز'], 'correct': 0, 'category': 'تاريخ', 'correct_answer': 'عبد الملك بن مروان'},
        {'question': 'من هو مكتشف الدورة الدموية الصغرى؟', 'options': ['ابن النفيس', 'جالينوس', 'ابن سينا', 'الرازي'], 'correct': 0, 'category': 'علوم', 'correct_answer': 'ابن النفيس'},
        {'question': 'ما هي أعلى قمة جبلية في أفريقيا؟', 'options': ['جبل كليمنجارو', 'جبل كينيا', 'جبل راس دشين', 'جبل كروجر'], 'correct': 0, 'category': 'جغرافيا', 'correct_answer': 'جبل كليمنجارو'},
        {'question': 'من هو صاحب ديوان "الحماسة"؟', 'options': ['أبو تمام', 'المتنبي', 'الفرزدق', 'جرير'], 'correct': 0, 'category': 'أدب', 'correct_answer': 'أبو تمام'},
        {'question': 'ما هي عاصمة الخلافة العباسية؟', 'options': ['دمشق', 'بغداد', 'القاهرة', 'قرطبة'], 'correct': 1, 'category': 'تاريخ', 'correct_answer': 'بغداد'},
        {'question': 'من هو مؤسس علم النحو؟', 'options': ['أبو الأسود الدؤلي', 'سيبويه', 'الخليل بن أحمد', 'الأصمعي'], 'correct': 0, 'category': 'ثقافة', 'correct_answer': 'أبو الأسود الدؤلي'},
    ],
    'صعب جداً': [
        {'question': 'في أي عام وقعت معركة عين جالوت؟', 'options': ['1260', '1261', '1262', '1263'], 'correct': 0, 'category': 'تاريخ', 'correct_answer': '1260'},
        {'question': 'من هو مؤسس الدولة الفاطمية؟', 'options': ['عبيد الله المهدي', 'المعز لدين الله', 'الحاكم بأمر الله', 'المنصور بالله'], 'correct': 0, 'category': 'تاريخ', 'correct_answer': 'عبيد الله المهدي'},
        {'question': 'في أي عام تم فتح القسطنطينية؟', 'options': ['1453', '1454', '1455', '1456'], 'correct': 0, 'category': 'تاريخ', 'correct_answer': '1453'},
        {'question': 'ما هي السرعة التي يحتاجها جسم للهروب من جاذبية الأرض؟', 'options': ['11.2 كم/ث', '12.2 كم/ث', '10.2 كم/ث', '13.2 كم/ث'], 'correct': 0, 'category': 'علوم', 'correct_answer': '11.2 كم/ث'},
        {'question': 'من هو مؤلف كتاب "الكامل في التاريخ"؟', 'options': ['ابن الأثير', 'الطبري', 'ابن كثير', 'ابن خلدون'], 'correct': 0, 'category': 'أدب', 'correct_answer': 'ابن الأثير'},
        {'question': 'ما هي السورة التي تسمى "قلب القرآن"؟', 'options': ['سورة يس', 'سورة الفاتحة', 'سورة الإخلاص', 'سورة الكوثر'], 'correct': 0, 'category': 'دين', 'correct_answer': 'سورة يس'},
        {'question': 'من هو مؤسس علم العروض؟', 'options': ['الخليل بن أحمد', 'سيبويه', 'الفراهيدي', 'الأصمعي'], 'correct': 0, 'category': 'ثقافة', 'correct_answer': 'الخليل بن أحمد'},
        {'question': 'ما هي أول دولة عربية اعترفت بالولايات المتحدة؟', 'options': ['المغرب', 'مصر', 'السعودية', 'تونس'], 'correct': 0, 'category': 'سياسة', 'correct_answer': 'المغرب'},
        {'question': 'من هو مؤسس علم المنطق في الحضارة العربية؟', 'options': ['الكندي', 'الفارابي', 'ابن سينا', 'الغزالي'], 'correct': 1, 'category': 'فلسفة', 'correct_answer': 'الفارابي'},
        {'question': 'ما هي أقدم مدينة في العالم؟', 'options': ['دمشق', 'أريحا', 'بغداد', 'القاهرة'], 'correct': 1, 'category': 'تاريخ', 'correct_answer': 'أريحا'},
    ]
}

# تهيئة حالة اللعبة
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'correct' not in st.session_state:
    st.session_state.correct = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'game_ended' not in st.session_state:
    st.session_state.game_ended = False
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'selected' not in st.session_state:
    st.session_state.selected = None
if 'current_difficulty' not in st.session_state:
    st.session_state.current_difficulty = 'صعب'
if 'score_saved' not in st.session_state:
    st.session_state.score_saved = False

def load_questions_by_difficulty(difficulty='صعب', num=15):
    """تحميل أسئلة حسب الصعوبة"""
    st.session_state.current_difficulty = difficulty
    available = QUESTIONS_BY_DIFFICULTY.get(difficulty, [])
    
    if not available:
        available = QUESTIONS_BY_DIFFICULTY.get('صعب', [])
    
    if len(available) < num:
        while len(available) < num:
            available.extend(random.sample(QUESTIONS_BY_DIFFICULTY.get(difficulty, QUESTIONS_BY_DIFFICULTY['صعب']), 
                                          min(num - len(available), len(QUESTIONS_BY_DIFFICULTY.get(difficulty, QUESTIONS_BY_DIFFICULTY['صعب'])))))
    
    selected = random.sample(available, num)
    st.session_state.questions = selected
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.correct = 0
    st.session_state.answered = False
    st.session_state.game_over = False
    st.session_state.game_ended = False
    st.session_state.message = ""
    st.session_state.selected = None
    st.session_state.score_saved = False

def end_game():
    """إنهاء التحدي وحفظ النتيجة"""
    if not st.session_state.game_ended and st.session_state.total > 0:
        add_score_to_leaderboard(
            st.session_state.player_name,
            st.session_state.score,
            st.session_state.correct,
            st.session_state.total,
            st.session_state.current_difficulty
        )
        st.session_state.game_ended = True
        st.session_state.game_over = True
        st.session_state.score_saved = True

# ==================== عرض لوحة المتصدرين ====================
def display_leaderboard(limit=10):
    leaderboard = load_leaderboard()
    
    if not leaderboard:
        st.info("📭 لا توجد نتائج حتى الآن. كن أول من يلعب!")
        return
    
    for i, entry in enumerate(leaderboard[:limit]):
        rank = i + 1
        medal = ""
        if rank == 1:
            medal = "🥇"
        elif rank == 2:
            medal = "🥈"
        elif rank == 3:
            medal = "🥉"
        
        is_current = entry['name'] == st.session_state.player_name
        diff_emoji = {'سهل': '🟢', 'متوسط': '🟡', 'صعب': '🟠', 'صعب جداً': '🔴'}.get(entry.get('difficulty', ''), '')
        
        st.markdown(f"""
        <div class="leaderboard-item {'top-rank' if is_current else ''}" style="{ 'border-color: #667eea; border-width: 2px;' if is_current else '' }">
            <span class="leaderboard-rank">{medal} #{rank}</span>
            <span class="leaderboard-name">{entry['name']} { '👈' if is_current else '' }</span>
            <span class="leaderboard-score">⭐ {entry['score']}</span>
            <span class="leaderboard-date">{diff_emoji} {entry.get('difficulty', '')} | {entry['date']}</span>
        </div>
        """, unsafe_allow_html=True)

# ==================== شاشة تسجيل الدخول ====================
def login_screen():
    st.markdown('<h1 class="main-title">🧠 تحدي العقول</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="start-box">
            <h2>👋 مرحباً بك!</h2>
            <p style="font-size: 1.1em; margin: 20px 0;">
                أدخل اسمك واختر الصعوبة لبدء التحدي
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        name = st.text_input("👤 اسم اللاعب:", max_chars=30, placeholder="اكتب اسمك هنا...")
        
        difficulty = st.selectbox(
            "🎯 اختر مستوى الصعوبة:",
            ['سهل', 'متوسط', 'صعب', 'صعب جداً'],
            index=2,
            format_func=lambda x: {
                'سهل': '🟢 سهل - 15 سؤال',
                'متوسط': '🟡 متوسط - 15 سؤال',
                'صعب': '🟠 صعب - 15 سؤال',
                'صعب جداً': '🔴 صعب جداً - 15 سؤال'
            }[x]
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 دخول", use_container_width=True):
                if name and name.strip():
                    st.session_state.player_name = name.strip()
                    st.session_state.logged_in = True
                    load_questions_by_difficulty(difficulty, 15)
                    st.rerun()
                else:
                    st.error("❌ الرجاء إدخال اسمك!")
        
        st.markdown("---")
        st.markdown("### 🏆 لوحة المتصدرين")
        display_leaderboard(limit=5)

# ==================== شاشة اللعب ====================
def game_screen():
    st.markdown('<h1 class="main-title">🧠 تحدي العقول</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        diff_emoji = {'سهل': '🟢', 'متوسط': '🟡', 'صعب': '🟠', 'صعب جداً': '🔴'}.get(st.session_state.current_difficulty, '')
        st.markdown(f"### 👋 مرحباً {st.session_state.player_name}!")
        st.markdown(f"**🎯 الصعوبة:** {diff_emoji} {st.session_state.current_difficulty}")
    with col3:
        if st.button("🚪 خروج", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.player_name = ""
            st.rerun()
    
    st.markdown("---")
    
    # الشريط الجانبي
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.player_name}")
        st.markdown(f"**🎯 الصعوبة:** {st.session_state.current_difficulty}")
        st.markdown("---")
        
        # تغيير الصعوبة
        new_difficulty = st.selectbox(
            "🔄 تغيير الصعوبة:",
            ['سهل', 'متوسط', 'صعب', 'صعب جداً'],
            index=['سهل', 'متوسط', 'صعب', 'صعب جداً'].index(st.session_state.current_difficulty),
            format_func=lambda x: {
                'سهل': '🟢 سهل',
                'متوسط': '🟡 متوسط',
                'صعب': '🟠 صعب',
                'صعب جداً': '🔴 صعب جداً'
            }[x]
        )
        
        if st.button("🔄 بدء جولة جديدة", use_container_width=True):
            load_questions_by_difficulty(new_difficulty, 15)
            st.rerun()
        
        st.markdown("---")
        
        if st.session_state.total > 0 and not st.session_state.game_ended:
            if st.button("🏁 إنهاء التحدي", use_container_width=True):
                end_game()
                st.rerun()
        
        st.markdown("---")
        
        if st.session_state.total > 0:
            st.markdown("## 📊 إحصائياتك")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("⭐ النقاط", st.session_state.score)
            with col2:
                pct = (st.session_state.correct / st.session_state.total * 100) if st.session_state.total > 0 else 0
                st.metric("✅ النجاح", f"{pct:.0f}%")
            
            st.metric("📝 الإجابات", f"{st.session_state.correct}/{st.session_state.total}")
            
            rank = get_player_rank(st.session_state.player_name)
            if rank:
                st.metric("🏆 الترتيب", f"#{rank}")
        
        st.markdown("---")
        st.markdown("### 🏆 المتصدرين")
        display_leaderboard(limit=5)
    
    # المحتوى الرئيسي
    if not st.session_state.questions:
        st.info("📚 اضغط على 'بدء جولة جديدة' لبدء التحدي")
        if st.button("🎮 بدء التحدي", use_container_width=True):
            load_questions_by_difficulty(st.session_state.current_difficulty, 15)
            st.rerun()
    
    elif st.session_state.game_over:
        # عرض شاشة النهاية
        st.markdown("---")
        st.markdown("## 🏆 انتهى التحدي!")
        st.balloons()
        
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
            st.info("📚 **أداء جيد! مع المزيد ستصل للاحتراف!**")
        else:
            st.warning("💪 **لا تستسلم! الممارسة تصنع الإتقان!**")
        
        if st.session_state.score_saved:
            st.success(f"✅ تم حفظ نتيجتك في لوحة المتصدرين!")
        
        # عرض لوحة المتصدرين الكاملة
        st.markdown("---")
        st.markdown("### 🏆 لوحة المتصدرين")
        display_leaderboard(limit=20)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 لعب مرة أخرى", use_container_width=True):
                load_questions_by_difficulty(st.session_state.current_difficulty, 15)
                st.rerun()
        with col2:
            if st.button("🏠 الصفحة الرئيسية", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.player_name = ""
                st.rerun()
    
    elif not st.session_state.game_over and st.session_state.current_q < len(st.session_state.questions):
        q = st.session_state.questions[st.session_state.current_q]
        total = len(st.session_state.questions)
        
        st.progress((st.session_state.current_q) / total, text=f"السؤال {st.session_state.current_q + 1} من {total}")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f'<span class="category-badge">📌 {q["category"]}</span>', unsafe_allow_html=True)
        with col2:
            difficulty = q.get('difficulty', st.session_state.current_difficulty)
            diff_class = {
                'سهل': 'difficulty-easy',
                'متوسط': 'difficulty-medium',
                'صعب': 'difficulty-hard',
                'صعب جداً': 'difficulty-expert'
            }.get(difficulty, 'difficulty-hard')
            st.markdown(f'<span class="{diff_class}">🔥 {difficulty}</span>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="question-box">
            <h3>❓ {q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
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
                    end_game()
                    st.rerun()

# ==================== التشغيل الرئيسي ====================
if not st.session_state.logged_in:
    login_screen()
else:
    game_screen()
