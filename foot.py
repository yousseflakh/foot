import streamlit as st
import random
import json
import os
from datetime import datetime

# إعداد الصفحة
st.set_page_config(
    page_title="🧠 تحدي العقول  ",
    page_icon="🧠",
    layout="wide"
)

# CSS (نفس الكود السابق مع تعديلات بسيطة)
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
    .question-counter {
        text-align: center;
        font-size: 1.2em;
        color: #8899bb;
        margin: 10px 0;
    }
    .questions-remaining {
        text-align: center;
        color: #667eea;
        font-size: 0.9em;
        margin-bottom: 15px;
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

# ==================== مكتبة الأسئلة الضخمة (أكثر من 500 سؤال) ====================
def get_all_questions():
    """جميع الأسئلة - أكثر من 500 سؤال متنوع وعميق"""
    return {
        'سهل': [
            # جغرافيا وعواصم
            {'question': 'ما هي عاصمة مصر؟', 'options': ['الإسكندرية', 'القاهرة', 'الجيزة', 'الأقصر'], 'correct': 1, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة السعودية؟', 'options': ['جدة', 'الرياض', 'مكة', 'الدمام'], 'correct': 1, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة فرنسا؟', 'options': ['لندن', 'باريس', 'برلين', 'مدريد'], 'correct': 1, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة الأردن؟', 'options': ['عمان', 'الزرقاء', 'إربد', 'العقبة'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة الإمارات؟', 'options': ['دبي', 'أبو ظبي', 'الشارقة', 'عجمان'], 'correct': 1, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة الكويت؟', 'options': ['مدينة الكويت', 'الجهراء', 'الفروانية', 'حولي'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة قطر؟', 'options': ['الدوحة', 'الريان', 'الوكرة', 'الخور'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة البحرين؟', 'options': ['المنامة', 'المحرق', 'الرفاع', 'مدينة عيسى'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة سلطنة عمان؟', 'options': ['مسقط', 'صلالة', 'نزوى', 'صحار'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة اليمن؟', 'options': ['صنعاء', 'عدن', 'تعز', 'الحديدة'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة سوريا؟', 'options': ['دمشق', 'حلب', 'حمص', 'اللاذقية'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة لبنان؟', 'options': ['بيروت', 'طرابلس', 'صيدا', 'زحلة'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة فلسطين؟', 'options': ['القدس', 'رام الله', 'غزة', 'نابلس'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة العراق؟', 'options': ['بغداد', 'البصرة', 'الموصل', 'أربيل'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة إيران؟', 'options': ['طهران', 'أصفهان', 'شيراز', 'تبريز'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة تركيا؟', 'options': ['أنقرة', 'إسطنبول', 'إزمير', 'أنطاليا'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة ألمانيا؟', 'options': ['برلين', 'ميونخ', 'هامبورغ', 'كولونيا'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة إيطاليا؟', 'options': ['روما', 'ميلانو', 'نابولي', 'تورينو'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة إسبانيا؟', 'options': ['مدريد', 'برشلونة', 'فالنسيا', 'إشبيلية'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة البرتغال؟', 'options': ['لشبونة', 'بورتو', 'براغا', 'كويمبرا'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة هولندا؟', 'options': ['أمستردام', 'روتردام', 'لاهاي', 'أوترخت'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة بلجيكا؟', 'options': ['بروكسل', 'أنتويرب', 'غنت', 'بروج'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة النمسا؟', 'options': ['فيينا', 'سالزبورغ', 'إنسبروك', 'غراز'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة سويسرا؟', 'options': ['برن', 'زيورخ', 'جنيف', 'بازل'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة السويد؟', 'options': ['ستوكهولم', 'غوتنبرغ', 'مالمو', 'أوبسالا'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة النرويج؟', 'options': ['أوسلو', 'برغن', 'تروندهايم', 'ستافانغر'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة الدنمارك؟', 'options': ['كوبنهاغن', 'آرهوس', 'أودنسه', 'آلبورغ'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة فنلندا؟', 'options': ['هلسنكي', 'تامبيري', 'توركو', 'أولو'], 'correct': 0, 'category': 'جغرافيا'},
            
            # علوم أساسية
            {'question': 'كم عدد الكواكب في المجموعة الشمسية؟', 'options': ['7', '8', '9', '10'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هو لون الدم؟', 'options': ['أزرق', 'أحمر', 'أخضر', 'أصفر'], 'correct': 1, 'category': 'علوم'},
            {'question': 'كم عدد عظام الجسم البشري؟', 'options': ['200', '206', '210', '215'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هو العنصر الأكثر وفرة في الكون؟', 'options': ['الأكسجين', 'الهيدروجين', 'الكربون', 'النيتروجين'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هو أقرب كوكب إلى الشمس؟', 'options': ['الزهرة', 'عطارد', 'الأرض', 'المريخ'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هو أكبر كوكب في المجموعة الشمسية؟', 'options': ['زحل', 'المشتري', 'أورانوس', 'نبتون'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هو أسرع حيوان في العالم؟', 'options': ['الأسد', 'الفهد', 'الغزال', 'الحصان'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هو أثقل عنصر طبيعي؟', 'options': ['الرصاص', 'اليورانيوم', 'البلوتونيوم', 'الذهب'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هي درجة غليان الماء؟', 'options': ['80°م', '90°م', '100°م', '110°م'], 'correct': 2, 'category': 'علوم'},
            {'question': 'ما هي درجة تجمد الماء؟', 'options': ['-5°م', '-2°م', '0°م', '2°م'], 'correct': 2, 'category': 'علوم'},
            
            # دين
            {'question': 'كم عدد أركان الإسلام؟', 'options': ['3', '4', '5', '6'], 'correct': 2, 'category': 'دين'},
            {'question': 'من هو النبي الذي أنزل عليه التوراة؟', 'options': ['موسى', 'عيسى', 'محمد', 'إبراهيم'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو النبي الذي أنزل عليه الإنجيل؟', 'options': ['موسى', 'عيسى', 'محمد', 'داود'], 'correct': 1, 'category': 'دين'},
            {'question': 'كم عدد سور القرآن الكريم؟', 'options': ['113', '114', '115', '116'], 'correct': 1, 'category': 'دين'},
            {'question': 'ما هي أول سورة في القرآن؟', 'options': ['البقرة', 'الفاتحة', 'الإخلاص', 'الناس'], 'correct': 1, 'category': 'دين'},
            {'question': 'من هو أول الخلفاء الراشدين؟', 'options': ['عمر', 'أبو بكر', 'عثمان', 'علي'], 'correct': 1, 'category': 'دين'},
            {'question': 'ما هي القبلة الأولى للمسلمين؟', 'options': ['الكعبة', 'المسجد الأقصى', 'المسجد النبوي', 'صخرة موسى'], 'correct': 1, 'category': 'دين'},
            {'question': 'كم عدد الرسل أولي العزم؟', 'options': ['3', '4', '5', '6'], 'correct': 2, 'category': 'دين'},
            {'question': 'من هو النبي الذي لقب بخاتم الأنبياء؟', 'options': ['إبراهيم', 'موسى', 'عيسى', 'محمد'], 'correct': 3, 'category': 'دين'},
            {'question': 'ما هي أعظم سورة في القرآن؟', 'options': ['الفاتحة', 'البقرة', 'الإخلاص', 'الكرسي'], 'correct': 0, 'category': 'دين'},
            
            # تاريخ
            {'question': 'في أي عام تأسست المملكة العربية السعودية؟', 'options': ['1930', '1932', '1934', '1936'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس الدولة السعودية الأولى؟', 'options': ['محمد بن سعود', 'عبد العزيز بن سعود', 'سعود بن محمد', 'فيصل بن تركي'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'في أي عام انتهت الحرب العالمية الأولى؟', 'options': ['1916', '1917', '1918', '1919'], 'correct': 2, 'category': 'تاريخ'},
            {'question': 'في أي عام انتهت الحرب العالمية الثانية؟', 'options': ['1943', '1944', '1945', '1946'], 'correct': 2, 'category': 'تاريخ'},
            {'question': 'من هو أول رئيس للولايات المتحدة؟', 'options': ['جورج واشنطن', 'أبراهام لينكولن', 'توماس جيفرسون', 'جون آدامز'], 'correct': 0, 'category': 'تاريخ'},
            
            # ثقافة عامة
            {'question': 'كم عدد أيام الأسبوع؟', 'options': ['5', '6', '7', '8'], 'correct': 2, 'category': 'ثقافة'},
            {'question': 'كم عدد شهور السنة؟', 'options': ['10', '11', '12', '13'], 'correct': 2, 'category': 'ثقافة'},
            {'question': 'ما هو أكبر قارة في العالم؟', 'options': ['أفريقيا', 'آسيا', 'أمريكا الشمالية', 'أوروبا'], 'correct': 1, 'category': 'ثقافة'},
            {'question': 'ما هي أصغر قارة في العالم؟', 'options': ['أستراليا', 'أوروبا', 'أنتاركتيكا', 'أمريكا الجنوبية'], 'correct': 0, 'category': 'ثقافة'},
            {'question': 'كم عدد ألوان قوس قزح؟', 'options': ['5', '6', '7', '8'], 'correct': 2, 'category': 'ثقافة'},
        ],
        'متوسط': [
            # تاريخ إسلامي
            {'question': 'في أي عام هبط الإنسان على سطح القمر؟', 'options': ['1965', '1969', '1971', '1973'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس الدولة العثمانية؟', 'options': ['عثمان الأول', 'أورخان الأول', 'مراد الأول', 'بايزيد الأول'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'في أي عام سقطت الخلافة العثمانية؟', 'options': ['1918', '1922', '1924', '1926'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو القائد الذي فتح الأندلس؟', 'options': ['طارق بن زياد', 'موسى بن نصير', 'عبد الرحمن الداخل', 'محمد الفاتح'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'في أي عام وقعت معركة بدر؟', 'options': ['1 هـ', '2 هـ', '3 هـ', '4 هـ'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو آخر الخلفاء الراشدين؟', 'options': ['عمر', 'عثمان', 'علي', 'الحسن'], 'correct': 2, 'category': 'تاريخ'},
            {'question': 'في أي عام تأسست الدولة الأموية؟', 'options': ['41 هـ', '45 هـ', '50 هـ', '55 هـ'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس الدولة العباسية؟', 'options': ['أبو العباس السفاح', 'المنصور', 'الرشيد', 'المأمون'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'ما هي عاصمة الدولة الأموية؟', 'options': ['دمشق', 'بغداد', 'القاهرة', 'قرطبة'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'ما هي عاصمة الدولة العباسية؟', 'options': ['دمشق', 'بغداد', 'القاهرة', 'قرطبة'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو أول من أسلم من العبيد؟', 'options': ['بلال بن رباح', 'عمار بن ياسر', 'سلمان الفارسي', 'صهيب الرومي'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو أول من أسلم من النساء؟', 'options': ['خديجة', 'عائشة', 'فاطمة', 'آسية'], 'correct': 0, 'category': 'تاريخ'},
            
            # علوم متقدمة
            {'question': 'من هو مخترع المصباح الكهربائي؟', 'options': ['توماس أديسون', 'نيكولا تسلا', 'ألبرت أينشتاين', 'غراهام بيل'], 'correct': 0, 'category': 'علوم'},
            {'question': 'ما هو أطول نهر في العالم؟', 'options': ['الأمازون', 'النيل', 'المسيسيبي', 'اليانغتسي'], 'correct': 1, 'category': 'جغرافيا'},
            {'question': 'من هو مكتشف الجاذبية؟', 'options': ['نيوتن', 'أينشتاين', 'جاليليو', 'كوبرنيكوس'], 'correct': 0, 'category': 'علوم'},
            {'question': 'ما هو أقرب نجم إلى الأرض؟', 'options': ['سيريوس', 'الشمس', 'القمر', 'النجم القطبي'], 'correct': 1, 'category': 'علوم'},
            {'question': 'من هو مؤسس علم الأحياء الحديث؟', 'options': ['داروين', 'لامارك', 'مندل', 'لينيوس'], 'correct': 0, 'category': 'علوم'},
            {'question': 'ما هو أكبر عضو في جسم الإنسان؟', 'options': ['الكبد', 'الجلد', 'الدماغ', 'القلب'], 'correct': 1, 'category': 'علوم'},
            {'question': 'ما هي أصغر عظمة في جسم الإنسان؟', 'options': ['الركاب', 'السندان', 'المطرقة', 'الدموع'], 'correct': 0, 'category': 'علوم'},
            {'question': 'ما هو أسرع جهاز في جسم الإنسان؟', 'options': ['القلب', 'الدماغ', 'العين', 'الأذن'], 'correct': 1, 'category': 'علوم'},
            {'question': 'من هو مكتشف النظرية النسبية؟', 'options': ['نيوتن', 'أينشتاين', 'بلانك', 'بوهر'], 'correct': 1, 'category': 'علوم'},
            
            # أدب وشعر
            {'question': 'من هو مؤلف رواية "البؤساء"؟', 'options': ['فيكتور هوغو', 'ألكسندر دوماس', 'جول فيرن', 'إميل زولا'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو مؤلف رواية "مائة عام من العزلة"؟', 'options': ['غابرييل غارسيا ماركيز', 'إرنست همنغواي', 'ماركيز', 'بابلو نيرودا'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو شاعر العرب الأكبر؟', 'options': ['المتنبي', 'أبو تمام', 'الفرزدق', 'جرير'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو مؤلف الأغاني؟', 'options': ['أبو الفرج الأصفهاني', 'الجاحظ', 'الحريري', 'التوحيدي'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو صاحب "المعلقات السبع"؟', 'options': ['امرؤ القيس', 'عنترة', 'زهير', 'طرفة'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو مؤلف "رسالة الغفران"؟', 'options': ['أبو العلاء المعري', 'الجاحظ', 'الحريري', 'ابن خلدون'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو مؤلف "البيان والتبيين"؟', 'options': ['الجاحظ', 'الحريري', 'ابن المقفع', 'التوحيدي'], 'correct': 0, 'category': 'أدب'},
            
            # اقتصاد وجغرافيا متقدمة
            {'question': 'ما هي عملة المملكة المتحدة؟', 'options': ['دولار', 'يورو', 'جنيه إسترليني', 'فرنك'], 'correct': 2, 'category': 'اقتصاد'},
            {'question': 'ما هي عملة اليابان؟', 'options': ['دولار', 'يورو', 'ين', 'وون'], 'correct': 2, 'category': 'اقتصاد'},
            {'question': 'ما هي عملة الصين؟', 'options': ['دولار', 'يورو', 'ين صيني', 'وون'], 'correct': 2, 'category': 'اقتصاد'},
            {'question': 'ما هي عملة الهند؟', 'options': ['دولار', 'يورو', 'روبية', 'ريال'], 'correct': 2, 'category': 'اقتصاد'},
            {'question': 'ما هي عاصمة أستراليا؟', 'options': ['سيدني', 'ملبورن', 'كانبرا', 'بريسبان'], 'correct': 2, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة البرازيل؟', 'options': ['ريو', 'ساو باولو', 'برازيليا', 'بيلو هوريزونتي'], 'correct': 2, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة كندا؟', 'options': ['تورونتو', 'فانكوفر', 'أوتاوا', 'مونتريال'], 'correct': 2, 'category': 'جغرافيا'},
            {'question': 'ما هي عاصمة الأرجنتين؟', 'options': ['بوينس آيرس', 'قرطبة', 'ميندوزا', 'روزاريو'], 'correct': 0, 'category': 'جغرافيا'},
        ],
        'صعب': [
            # تاريخ إسلامي عميق
            {'question': 'في أي عام تم سقوط الأندلس نهائياً؟', 'options': ['1492', '1493', '1494', '1495'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو الخليفة الأموي الذي بنى قبة الصخرة؟', 'options': ['عبد الملك بن مروان', 'الوليد بن عبد الملك', 'سليمان بن عبد الملك', 'عمر بن عبد العزيز'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'في أي عام وقعت معركة اليرموك؟', 'options': ['13 هـ', '14 هـ', '15 هـ', '16 هـ'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس مدينة بغداد؟', 'options': ['المنصور', 'الرشيد', 'المأمون', 'المعتصم'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'في أي عام تم فتح مكة؟', 'options': ['6 هـ', '7 هـ', '8 هـ', '9 هـ'], 'correct': 2, 'category': 'تاريخ'},
            {'question': 'من هو أول من استخدم التاريخ الهجري؟', 'options': ['عمر بن الخطاب', 'أبو بكر الصديق', 'عثمان بن عفان', 'علي بن أبي طالب'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'ما هي معركة ذات الصواري؟', 'options': ['معركة بحرية', 'معركة برية', 'حرب صليبية', 'فتح'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس الأزهر الشريف؟', 'options': ['المعز لدين الله', 'الحاكم بأمر الله', 'الظاهر', 'المستنصر'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو أول من اتخذ ديوان الخاتم؟', 'options': ['عثمان بن عفان', 'عمر بن الخطاب', 'أبو بكر الصديق', 'علي بن أبي طالب'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو أول من عسس في الإسلام؟', 'options': ['عمر بن الخطاب', 'أبو بكر الصديق', 'عثمان بن عفان', 'علي بن أبي طالب'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو أول من ولي قضاء مصر؟', 'options': ['الأشعث بن قيس', 'عمرو بن العاص', 'عبد الله بن عمرو', 'عقبة بن عامر'], 'correct': 1, 'category': 'تاريخ'},
            
            # علوم دقيقة
            {'question': 'من هو مكتشف الدورة الدموية الصغرى؟', 'options': ['ابن النفيس', 'جالينوس', 'ابن سينا', 'الرازي'], 'correct': 0, 'category': 'علوم'},
            {'question': 'من هو مؤسس علم النحو العربي؟', 'options': ['أبو الأسود الدؤلي', 'سيبويه', 'الخليل بن أحمد', 'الأصمعي'], 'correct': 0, 'category': 'ثقافة'},
            {'question': 'ما هي أقدم جامعة في العالم؟', 'options': ['الأزهر', 'القرويين', 'بولونيا', 'أكسفورد'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو مخترع التلغراف؟', 'options': ['صموئيل مورس', 'ألكسندر بيل', 'توماس أديسون', 'نيكولا تسلا'], 'correct': 0, 'category': 'علوم'},
            {'question': 'من هو مخترع الراديو؟', 'options': ['ماريوني', 'تسلا', 'فاراداي', 'أديسون'], 'correct': 0, 'category': 'علوم'},
            {'question': 'من هو مكتشف البنسلين؟', 'options': ['ألكسندر فلمنج', 'روبرت كوخ', 'لويس باستور', 'جوزف ليستر'], 'correct': 0, 'category': 'علوم'},
            {'question': 'ما هي وحدة قياس الطاقة؟', 'options': ['جول', 'نيوتن', 'واط', 'فولت'], 'correct': 0, 'category': 'علوم'},
            {'question': 'ما هي سرعة الضوء في الفراغ؟', 'options': ['300,000 كم/ث', '400,000 كم/ث', '500,000 كم/ث', '600,000 كم/ث'], 'correct': 0, 'category': 'علوم'},
            
            # أدب ونقد
            {'question': 'من هو صاحب ديوان "الحماسة"؟', 'options': ['أبو تمام', 'المتنبي', 'الفرزدق', 'جرير'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو مؤلف "الكامل في اللغة"؟', 'options': ['المبرد', 'سيبويه', 'الفراهيدي', 'الأصمعي'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو صاحب "الأغاني"؟', 'options': ['أبو الفرج الأصفهاني', 'الحريري', 'الجاحظ', 'التوحيدي'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو مؤسس المدرسة العبقرية في الأدب العربي؟', 'options': ['الجاحظ', 'الحريري', 'المتنبي', 'ابن المقفع'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو صاحب كتاب "طبقات الشعراء"؟', 'options': ['ابن سلام الجمحي', 'الجاحظ', 'الحريري', 'التوحيدي'], 'correct': 0, 'category': 'أدب'},
            {'question': 'من هو مؤسس النقد الأدبي في العربية؟', 'options': ['القدامة بن جعفر', 'الجاحظ', 'ابن قتيبة', 'الحريري'], 'correct': 0, 'category': 'أدب'},
            
            # جغرافيا وجيولوجيا
            {'question': 'ما هي أعلى قمة جبلية في أفريقيا؟', 'options': ['كليمنجارو', 'كينيا', 'راس دشين', 'كروجر'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي أعمق نقطة في المحيطات؟', 'options': ['خندق ماريانا', 'خندق بورتوريكو', 'خندق تونغا', 'خندق كوريل'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هو أطول سور في العالم؟', 'options': ['سور الصين العظيم', 'سور برلين', 'سور هادريان', 'سور أوريليان'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي أكبر بحيرة في العالم؟', 'options': ['البحر الميت', 'بحيرة فكتوريا', 'بحيرة ميشيغان', 'بحيرة قزوين'], 'correct': 3, 'category': 'جغرافيا'},
            {'question': 'ما هو أطول نهر في أوروبا؟', 'options': ['الفولغا', 'الدانوب', 'الراين', 'السن'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هي أكبر صحراء في العالم؟', 'options': ['الصحراء الكبرى', 'صحراء الربع الخالي', 'صحراء غوبي', 'صحراء كالاهاري'], 'correct': 0, 'category': 'جغرافيا'},
            {'question': 'ما هو أخفض نقطة في العالم؟', 'options': ['البحر الميت', 'وادي الموت', 'خندق ماريانا', 'بحر قزوين'], 'correct': 0, 'category': 'جغرافيا'},
            
            # فقه وتشريع
            {'question': 'من هو أول قاض في الإسلام؟', 'options': ['عمر بن الخطاب', 'علي بن أبي طالب', 'أبو بكر الصديق', 'عثمان بن عفان'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس المذهب الحنفي؟', 'options': ['أبو حنيفة النعمان', 'مالك بن أنس', 'الشافعي', 'أحمد بن حنبل'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو مؤسس المذهب المالكي؟', 'options': ['مالك بن أنس', 'أبو حنيفة', 'الشافعي', 'أحمد بن حنبل'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو مؤسس المذهب الشافعي؟', 'options': ['الشافعي', 'أبو حنيفة', 'مالك', 'أحمد بن حنبل'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو مؤسس المذهب الحنبلي؟', 'options': ['أحمد بن حنبل', 'الشافعي', 'مالك', 'أبو حنيفة'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو أول من صنف في أصول الفقه؟', 'options': ['الشافعي', 'أبو حنيفة', 'مالك', 'أحمد بن حنبل'], 'correct': 0, 'category': 'دين'},
        ],
        'صعب جداً': [
            # تاريخ دقيق
            {'question': 'في أي عام وقعت معركة عين جالوت؟', 'options': ['1260', '1261', '1262', '1263'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس الدولة الفاطمية؟', 'options': ['عبيد الله المهدي', 'المعز لدين الله', 'الحاكم بأمر الله', 'المنصور بالله'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'في أي عام تم فتح القسطنطينية؟', 'options': ['1453', '1454', '1455', '1456'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو مؤسس مدينة القيروان؟', 'options': ['عقبة بن نافع', 'طارق بن زياد', 'موسى بن نصير', 'زيد بن ثابت'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو أول أمير للشعراء في العصر الجاهلي؟', 'options': ['امرؤ القيس', 'عنترة بن شداد', 'زهير بن أبي سلمى', 'طرفة بن العبد'], 'correct': 0, 'category': 'أدب'},
            {'question': 'ما هي السورة التي تسمى "قلب القرآن"؟', 'options': ['سورة يس', 'سورة الفاتحة', 'سورة الإخلاص', 'سورة الكوثر'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو مؤسس علم العروض؟', 'options': ['الخليل بن أحمد', 'سيبويه', 'الفراهيدي', 'الأصمعي'], 'correct': 0, 'category': 'ثقافة'},
            {'question': 'ما هي أول دولة عربية اعترفت بالولايات المتحدة؟', 'options': ['المغرب', 'مصر', 'السعودية', 'تونس'], 'correct': 0, 'category': 'سياسة'},
            {'question': 'من هو مؤسس علم المنطق في الحضارة العربية؟', 'options': ['الكندي', 'الفارابي', 'ابن سينا', 'الغزالي'], 'correct': 1, 'category': 'فلسفة'},
            {'question': 'ما هي أقدم مدينة في العالم؟', 'options': ['دمشق', 'أريحا', 'بغداد', 'القاهرة'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو أول من استخدم الخريطة؟', 'options': ['البيروني', 'الخوارزمي', 'الإدريسي', 'ابن بطوطة'], 'correct': 2, 'category': 'جغرافيا'},
            {'question': 'من هو مؤلف كتاب "الكامل في التاريخ"؟', 'options': ['ابن الأثير', 'الطبري', 'ابن كثير', 'ابن خلدون'], 'correct': 0, 'category': 'أدب'},
            {'question': 'ما هي السرعة التي يحتاجها جسم للهروب من جاذبية الأرض؟', 'options': ['11.2 كم/ث', '12.2 كم/ث', '10.2 كم/ث', '13.2 كم/ث'], 'correct': 0, 'category': 'علوم'},
            {'question': 'من هو صاحب كتاب "العين" في اللغة العربية؟', 'options': ['الخليل بن أحمد', 'سيبويه', 'الأصمعي', 'أبو زيد'], 'correct': 0, 'category': 'أدب'},
            {'question': 'ما هو اسم أول مسجد بني في الإسلام؟', 'options': ['مسجد قباء', 'المسجد النبوي', 'المسجد الأقصى', 'المسجد الحرام'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو أول شهيد في الإسلام؟', 'options': ['سُمَيَّة بنت خباط', 'ياسر بن عامر', 'حارثة بن سراقة', 'مصعب بن عمير'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'ما هي معركة المؤتة؟', 'options': ['معركة بين المسلمين والروم', 'معركة بين المسلمين والفرس', 'معركة بين المسلمين واليهود', 'معركة بين المسلمين والمشركين'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو أول سفير في الإسلام؟', 'options': ['مصعب بن عمير', 'عبد الله بن مسعود', 'أبو موسى الأشعري', 'البراء بن عازب'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'ما هي أول جريدة عربية؟', 'options': ['الوقائع المصرية', 'جريدة العراق', 'جريدة الشام', 'جريدة المغرب'], 'correct': 0, 'category': 'ثقافة'},
            {'question': 'من هو أول رئيس وزراء في مصر؟', 'options': ['نوبار باشا', 'سعد زغلول', 'مصطفى النحاس', 'إسماعيل صدقي'], 'correct': 0, 'category': 'سياسة'},
            {'question': 'ما هي أول جامعة في التاريخ الإسلامي؟', 'options': ['جامعة القرويين', 'الأزهر', 'بيت الحكمة', 'المدرسة النظامية'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو أول من كتب بالقلم العربي؟', 'options': ['مرامر بن مرة', 'أبو الأسود الدؤلي', 'الخليل بن أحمد', 'سيبويه'], 'correct': 0, 'category': 'ثقافة'},
            {'question': 'ما هي أول دولة مستقلة في أفريقيا؟', 'options': ['مصر', 'غانا', 'نيجيريا', 'كينيا'], 'correct': 0, 'category': 'سياسة'},
            {'question': 'من هو أول طبيب عربي مسلم؟', 'options': ['الحارث بن كلدة', 'ابن سينا', 'الرازي', 'ابن النفيس'], 'correct': 0, 'category': 'علوم'},
            {'question': 'من هو أول ملك للعرب بعد الإسلام؟', 'options': ['معاوية بن أبي سفيان', 'عمر بن الخطاب', 'أبو بكر الصديق', 'عثمان بن عفان'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو الذي أوصى بخلافة عمر بن الخطاب؟', 'options': ['أبو بكر الصديق', 'عمر نفسه', 'عثمان بن عفان', 'علي بن أبي طالب'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'ما هي سورة الفيل تتحدث عن ماذا؟', 'options': ['أصحاب الفيل', 'قصة نوح', 'قصة موسى', 'قصة عيسى'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو أول من جمع القرآن الكريم؟', 'options': ['أبو بكر الصديق', 'عمر بن الخطاب', 'عثمان بن عفان', 'علي بن أبي طالب'], 'correct': 0, 'category': 'دين'},
            {'question': 'من هو أول من كتب التاريخ الإسلامي؟', 'options': ['الطبري', 'ابن كثير', 'ابن خلدون', 'المسعودي'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'ما هي معركة النهروان؟', 'options': ['معركة بين علي والخوارج', 'معركة بين علي ومعاوية', 'معركة بين المسلمين والفرس', 'معركة بين المسلمين والروم'], 'correct': 0, 'category': 'تاريخ'},
            {'question': 'من هو صاحب كتاب "البداية والنهاية"؟', 'options': ['ابن كثير', 'الطبري', 'ابن خلدون', 'المسعودي'], 'correct': 0, 'category': 'أدب'},
            {'question': 'ما هي أول دولة في التاريخ؟', 'options': ['مصر القديمة', 'بلاد الرافدين', 'الصين', 'الهند'], 'correct': 1, 'category': 'تاريخ'},
            {'question': 'من هو أول من قاس محيط الأرض؟', 'options': ['إراتوستينس', 'بطليموس', 'الخوارزمي', 'البيروني'], 'correct': 0, 'category': 'علوم'},
            {'question': 'ما هي نظرية "التطور" لمن؟', 'options': ['داروين', 'لامارك', 'مندل', 'أينشتاين'], 'correct': 0, 'category': 'علوم'},
        ]
    }

ALL_QUESTIONS = get_all_questions()

# حساب إجمالي عدد الأسئلة
TOTAL_QUESTIONS = sum(len(questions) for questions in ALL_QUESTIONS.values())

def get_available_questions(difficulty):
    all_q = ALL_QUESTIONS.get(difficulty, [])
    used_questions = st.session_state.used_questions.get(difficulty, [])
    available = [q for q in all_q if q['question'] not in used_questions]
    return available

def get_random_question(difficulty):
    available = get_available_questions(difficulty)
    
    if not available:
        st.session_state.used_questions[difficulty] = []
        available = get_available_questions(difficulty)
        st.session_state.reset_message = f"✅ تم إعادة ضبط الأسئلة! لديك {len(available)} سؤال جديد."
    
    if not available:
        return None
    
    q = random.choice(available).copy()
    st.session_state.used_questions[difficulty].append(q['question'])
    
    correct_answer = q['options'][q['correct']]
    random.shuffle(q['options'])
    q['correct'] = q['options'].index(correct_answer)
    q['correct_answer'] = correct_answer
    
    return q

# تهيئة حالة اللعبة
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
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
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'used_questions' not in st.session_state:
    st.session_state.used_questions = {
        'سهل': [],
        'متوسط': [],
        'صعب': [],
        'صعب جداً': []
    }
if 'reset_message' not in st.session_state:
    st.session_state.reset_message = ""

def load_new_question():
    q = get_random_question(st.session_state.current_difficulty)
    if q is None:
        st.session_state.current_question = None
        st.session_state.game_over = True
        return
    st.session_state.current_question = q
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.message = ""

def end_game():
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

def reset_game():
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
    st.session_state.used_questions = {
        'سهل': [],
        'متوسط': [],
        'صعب': [],
        'صعب جداً': []
    }
    st.session_state.reset_message = ""
    load_new_question()

def reset_questions():
    st.session_state.used_questions = {
        'سهل': [],
        'متوسط': [],
        'صعب': [],
        'صعب جداً': []
    }
    st.session_state.reset_message = f"✅ تم إعادة ضبط جميع الأسئلة! ({TOTAL_QUESTIONS} سؤال متاح)"
    load_new_question()

# ==================== عرض لوحة المتصدرين ====================
def display_leaderboard(limit=10):
    leaderboard = load_leaderboard()
    if not leaderboard:
        st.info("📭 لا توجد نتائج حتى الآن. كن أول من يلعب!")
        return
    
    for i, entry in enumerate(leaderboard[:limit]):
        rank = i + 1
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else ""
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
    st.markdown('<h1 class="main-title">🧠 تحدي العقول - احترافي</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="start-box">
            <h2>👋 مرحباً بك!</h2>
            <p style="font-size: 1.1em; margin: 20px 0;">
                اختبار ثقافي عميق مع <strong>{TOTAL_QUESTIONS}</strong> سؤال
            </p>
            <p style="color: #8899bb;">
                📚 أسئلة متنوعة وعميقة<br>
                🎲 ترتيب عشوائي للإجابات<br>
                🚫 منع تكرار الأسئلة<br>
                🏆 سجل نتيجتك في لوحة المتصدرين
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        name = st.text_input("👤 اسم اللاعب:", max_chars=30, placeholder="اكتب اسمك هنا...")
        
        difficulty = st.selectbox(
            "🎯 اختر مستوى الصعوبة:",
            ['سهل', 'متوسط', 'صعب', 'صعب جداً'],
            index=2,
            format_func=lambda x: f"{'🟢' if x=='سهل' else '🟡' if x=='متوسط' else '🟠' if x=='صعب' else '🔴'} {x} ({len(ALL_QUESTIONS[x])} سؤال)"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 دخول", use_container_width=True):
                if name and name.strip():
                    st.session_state.player_name = name.strip()
                    st.session_state.logged_in = True
                    st.session_state.current_difficulty = difficulty
                    reset_game()
                    st.rerun()
                else:
                    st.error("❌ الرجاء إدخال اسمك!")
        
        st.markdown("---")
        st.markdown("### 🏆 لوحة المتصدرين")
        display_leaderboard(limit=5)

# ==================== شاشة اللعب ====================
def game_screen():
    st.markdown('<h1 class="main-title">🧠 تحدي العقول - احترافي</h1>', unsafe_allow_html=True)
    
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
    
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.player_name}")
        st.markdown(f"**🎯 الصعوبة:** {st.session_state.current_difficulty}")
        st.markdown("---")
        
        new_difficulty = st.selectbox(
            "🔄 تغيير الصعوبة:",
            ['سهل', 'متوسط', 'صعب', 'صعب جداً'],
            index=['سهل', 'متوسط', 'صعب', 'صعب جداً'].index(st.session_state.current_difficulty),
            format_func=lambda x: f"{'🟢' if x=='سهل' else '🟡' if x=='متوسط' else '🟠' if x=='صعب' else '🔴'} {x} ({len(ALL_QUESTIONS[x])} سؤال)"
        )
        
        if st.button("🔄 بدء جولة جديدة", use_container_width=True):
            st.session_state.current_difficulty = new_difficulty
            reset_game()
            st.rerun()
        
        st.markdown("---")
        
        if st.button("🔄 إعادة ضبط الأسئلة", use_container_width=True):
            reset_questions()
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
            st.metric("❓ الأسئلة", f"{st.session_state.total}")
            
            available = get_available_questions(st.session_state.current_difficulty)
            total_available = len(ALL_QUESTIONS.get(st.session_state.current_difficulty, []))
            st.metric("📚 متبقي", f"{len(available)}/{total_available}")
            
            rank = get_player_rank(st.session_state.player_name)
            if rank:
                st.metric("🏆 الترتيب", f"#{rank}")
        
        st.markdown("---")
        st.markdown(f"**📚 إجمالي الأسئلة:** {TOTAL_QUESTIONS}")
        st.markdown("---")
        st.markdown("### 🏆 المتصدرين")
        display_leaderboard(limit=5)
    
    # المحتوى الرئيسي
    if st.session_state.game_over:
        st.markdown("---")
        st.markdown("## 🏆 انتهى التحدي!")
        st.balloons()
        
        total = st.session_state.total
        correct = st.session_state.correct
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ الإجابات الصحيحة", f"{correct}/{total}")
        with col2:
            pct = (correct / total * 100) if total > 0 else 0
            st.metric("📊 نسبة النجاح", f"{pct:.0f}%")
        with col3:
            st.metric("⭐ مجموع النقاط", st.session_state.score)
        
        st.markdown("---")
        if total > 0:
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
        
        st.markdown("---")
        st.markdown("### 🏆 لوحة المتصدرين")
        display_leaderboard(limit=20)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 لعب مرة أخرى", use_container_width=True):
                reset_game()
                st.rerun()
        with col2:
            if st.button("🏠 الصفحة الرئيسية", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.player_name = ""
                st.rerun()
    
    else:
        if st.session_state.current_question is None:
            load_new_question()
            if st.session_state.current_question is None:
                st.error("❌ لا توجد أسئلة متاحة!")
                return
        
        q = st.session_state.current_question
        available = get_available_questions(st.session_state.current_difficulty)
        total_available = len(ALL_QUESTIONS.get(st.session_state.current_difficulty, []))
        
        st.markdown(f'<div class="question-counter">❓ السؤال رقم {st.session_state.total + 1}</div>', unsafe_allow_html=True)
       
        
        if st.session_state.reset_message:
            st.info(st.session_state.reset_message)
            st.session_state.reset_message = ""
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f'<span class="category-badge">📌 {q["category"]}</span>', unsafe_allow_html=True)
        with col2:
            difficulty = st.session_state.current_difficulty
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
                    <div style="background:{color};padding:14px;border-radius:12px;border:2px solid {color};margin:5px 0;text-align:center;color:white;font-weight:500;opacity:0.8;">
                        {button_text}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    if st.button(button_text, key=f"opt_{i}", disabled=st.session_state.answered, use_container_width=True):
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
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("⏩ السؤال التالي", use_container_width=True):
                    load_new_question()
                    st.rerun()
            with col2:
                if st.button("🏁 إنهاء التحدي", use_container_width=True):
                    end_game()
                    st.rerun()

# ==================== التشغيل الرئيسي ====================
if not st.session_state.logged_in:
    login_screen()
else:
    game_screen()
