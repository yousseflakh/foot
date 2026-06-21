import streamlit as st
import requests
import random
import time

# إعداد الصفحة
st.set_page_config(
    page_title="🧠 تحدي العقول",
    page_icon="🧠",
    layout="wide"
)

# CSS مخصص للتصميم
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3em;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 20px;
    }
    .score-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    .question-box {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 20px 0;
    }
    .option-btn {
        width: 100%;
        margin: 5px 0;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        background: white;
        transition: all 0.3s;
    }
    .option-btn:hover {
        transform: scale(1.02);
        border-color: #667eea;
    }
    .correct {
        background: #d4edda !important;
        border-color: #28a745 !important;
    }
    .wrong {
        background: #f8d7da !important;
        border-color: #dc3545 !important;
    }
</style>
""", unsafe_allow_html=True)

# دوال لجلب الأسئلة من API مفتوح
def fetch_questions(amount=10, difficulty='hard'):
    """جلب أسئلة من Open Trivia DB"""
    try:
        url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data['response_code'] == 0:
                return data['results']
    except:
        pass
    return None

def get_fallback_questions():
    """أسئلة احتياطية في حال فشل الاتصال"""
    return [
        {
            "question": "ما هو أطول جبل في العالم؟",
            "correct_answer": "إيفرست",
            "incorrect_answers": ["كليمنجارو", "ماونت مكينلي", "إلبروس"],
            "category": "جغرافيا"
        },
        {
            "question": "في أي عام سقطت الخلافة العثمانية؟",
            "correct_answer": "1922",
            "incorrect_answers": ["1918", "1924", "1920"],
            "category": "تاريخ"
        },
        {
            "question": "من هو مخترع الإنترنت؟",
            "correct_answer": "تيم بيرنرز لي",
            "incorrect_answers": ["بيل غيتس", "ستيف جوبز", "مارك زوكربيرغ"],
            "category": "تكنولوجيا"
        },
        {
            "question": "ما هي أصغر دولة في العالم من حيث المساحة؟",
            "correct_answer": "الفاتيكان",
            "incorrect_answers": ["موناكو", "ناورو", "سان مارينو"],
            "category": "جغرافيا"
        },
        {
            "question": "من هو مؤلف رواية \"الجريمة والعقاب\"؟",
            "correct_answer": "فيودور دوستويفسكي",
            "incorrect_answers": ["ليو تولستوي", "أنطون تشيخوف", "نيكولاي غوغول"],
            "category": "أدب"
        }
    ]

# تهيئة حالة اللعبة
if 'questions' not in st.session_state:
    st.session_state.questions = []
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.total_answered = 0
    st.session_state.correct_answers = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.difficulty = 'hard'
    st.session_state.category = 'any'
    st.session_state.game_started = False
    st.session_state.feedback = ""

# وظيفة تحميل الأسئلة
def load_questions():
    with st.spinner("🔄 جاري تحميل الأسئلة..."):
        questions = fetch_questions(amount=10, difficulty=st.session_state.difficulty)
        
        if questions is None:
            questions = get_fallback_questions()
            st.warning("⚠️ باستخدام الأسئلة الاحتياطية (غير متصل بالإنترنت)")
        else:
            st.success("✅ تم تحميل الأسئلة بنجاح!")
        
        # تنظيف الأسئلة
        cleaned = []
        for q in questions:
            options = [q['correct_answer']] + q['incorrect_answers']
            random.shuffle(options)
            cleaned.append({
                'question': q['question'],
                'options': options,
                'correct': options.index(q['correct_answer']),
                'category': q.get('category', 'عام'),
                'correct_answer': q['correct_answer']
            })
        
        st.session_state.questions = cleaned
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.total_answered = 0
        st.session_state.correct_answers = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.game_started = True
        st.session_state.feedback = ""

# العنوان
st.markdown('<h1 class="main-title">🧠 تحدي العقول</h1>', unsafe_allow_html=True)

# الشريط الجانبي للإعدادات
with st.sidebar:
    st.markdown("## ⚙️ الإعدادات")
    
    difficulty = st.selectbox(
        "صعوبة الأسئلة",
        ['easy', 'medium', 'hard'],
        index=2,
        help="صعوبة - متوسط - صعب"
    )
    
    if st.button("🚀 بدء لعبة جديدة", use_container_width=True):
        st.session_state.difficulty = difficulty
        load_questions()
        st.rerun()
    
    st.markdown("---")
    
    if st.session_state.game_started:
        st.markdown("## 📊 الإحصائيات")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("⭐ النقاط", st.session_state.score)
        with col2:
            correct_pct = (st.session_state.correct_answers / st.session_state.total_answered * 100) if st.session_state.total_answered > 0 else 0
            st.metric("✅ النجاح", f"{correct_pct:.0f}%")
        
        st.metric("📝 المجيب", f"{st.session_state.correct_answers}/{st.session_state.total_answered}")

# المحتوى الرئيسي
if not st.session_state.game_started:
    # شاشة البداية
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 50px 0;">
            <h2>🎯 اختبر ذكائك!</h2>
            <p style="font-size: 1.2em; color: #666;">
                أسئلة ثقافية عامة صعبة من جميع أنحاء العالم
            </p>
            <p style="color: #999;">
                📚 10 أسئلة لكل جولة<br>
                ⭐ 10 نقاط لكل إجابة صحيحة<br>
                🔥 تحدى نفسك!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 ابدأ اللعب", use_container_width=True):
            load_questions()
            st.rerun()
else:
    # عرض الأسئلة
    if st.session_state.current_q < len(st.session_state.questions):
        q = st.session_state.questions[st.session_state.current_q]
        total = len(st.session_state.questions)
        
        # شريط التقدم
        st.progress((st.session_state.current_q) / total, text=f"السؤال {st.session_state.current_q + 1} من {total}")
        
        # عرض الفئة
        st.markdown(f"<span style='background: #667eea; color: white; padding: 5px 15px; border-radius: 20px;'>{q['category']}</span>", unsafe_allow_html=True)
        
        # السؤال
        st.markdown(f"""
        <div class="question-box">
            <h3>❓ {q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # الخيارات
        cols = st.columns(2)
        for i, option in enumerate(q['options']):
            with cols[i % 2]:
                # تحديد نمط الزر
                btn_style = "option-btn"
                if st.session_state.answered:
                    if i == q['correct']:
                        btn_style += " correct"
                    elif st.session_state.selected == i and i != q['correct']:
                        btn_style += " wrong"
                
                if st.button(
                    option,
                    key=f"opt_{i}",
                    disabled=st.session_state.answered,
                    use_container_width=True
                ):
                    st.session_state.answered = True
                    st.session_state.selected = i
                    st.session_state.total_answered += 1
                    
                    if i == q['correct']:
                        st.session_state.score += 10
                        st.session_state.correct_answers += 1
                        st.session_state.feedback = "✅ **صحيح!** +10 نقاط"
                    else:
                        st.session_state.feedback = f"❌ **خطأ!** الإجابة الصحيحة: {q['correct_answer']}"
                    
                    st.rerun()
        
        # عرض التغذية الراجعة
        if st.session_state.answered:
            st.markdown("---")
            if "صحيح" in st.session_state.feedback:
                st.success(st.session_state.feedback)
            else:
                st.error(st.session_state.feedback)
            
            if st.button("⏩ السؤال التالي", use_container_width=True):
                st.session_state.current_q += 1
                st.session_state.answered = False
                st.session_state.selected = None
                st.session_state.feedback = ""
                st.rerun()
    
    else:
        # نهاية اللعبة
        st.markdown("---")
        st.markdown("## 🏆 انتهت اللعبة!")
        
        total = len(st.session_state.questions)
        correct = st.session_state.correct_answers
        
        # تقييم الأداء
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ الإجابات الصحيحة", f"{correct}/{total}")
        with col2:
            pct = (correct / total * 100) if total > 0 else 0
            st.metric("📊 نسبة النجاح", f"{pct:.0f}%")
        with col3:
            st.metric("⭐ مجموع النقاط", st.session_state.score)
        
        # رسالة تشجيعية
        if correct == total:
            st.success("🌟🌟🌟 **مذهل! إجابة كاملة! أنت عبقري!**")
        elif correct >= total * 0.7:
            st.success("⭐ **أداء ممتاز! استمر بهذا المستوى!**")
        elif correct >= total * 0.5:
            st.info("📚 **أداء جيد! مع مزيد من التدريب ستصبح أفضل!**")
        else:
            st.warning("💪 **لا تستسلم! الممارسة تصنع الإتقان!**")
        
        # إعادة التشغيل
        if st.button("🔄 لعب مرة أخرى", use_container_width=True):
            load_questions()
            st.rerun()

# التذييل
st.markdown("---")
st.caption("🧠 مصدر الأسئلة: Open Trivia DB | أسئلة لا متناهية")
