import streamlit as st
import random
import time

# إعداد الصفحة
st.set_page_config(
    page_title="⚽ لعبة كرة القدم الثقافية",
    page_icon="⚽",
    layout="centered"
)

# الأسئلة الصعبة (ثقافة عامة)
QUESTIONS = [
    {
        "question": "ما هو أطول نهر في العالم؟",
        "options": ["النيل", "الأمازون", "المسيسيبي", "اليانغتسي"],
        "correct": 1,
        "hint": "يقع في أمريكا الجنوبية"
    },
    {
        "question": "في أي عام هبط الإنسان على سطح القمر؟",
        "options": ["1965", "1969", "1971", "1973"],
        "correct": 1,
        "hint": "نهاية الستينيات"
    },
    {
        "question": "ما هي اللغة الأكثر تحدثاً في العالم كلغة أم؟",
        "options": ["الإنجليزية", "الإسبانية", "الصينية الماندرين", "الهندية"],
        "correct": 2,
        "hint": "آسيا"
    },
    {
        "question": "من هو مؤسس علم الجبر؟",
        "options": ["الخوارزمي", "ابن سينا", "الفارابي", "البيروني"],
        "correct": 0,
        "hint": "عالم رياضيات مسلم"
    },
    {
        "question": "ما هو أسرع حيوان بري في العالم؟",
        "options": ["الأسد", "الغزال", "الفهد", "الأرنب"],
        "correct": 2,
        "hint": "سرعته تتجاوز 100 كم/ساعة"
    },
    {
        "question": "كم عدد الكواكب في المجموعة الشمسية؟",
        "options": ["7", "8", "9", "10"],
        "correct": 1,
        "hint": "تم استبعاد بلوتو"
    },
    {
        "question": "ما هي عاصمة اليابان؟",
        "options": ["بكين", "سيئول", "طوكيو", "بانكوك"],
        "correct": 2,
        "hint": "أكبر مدينة في اليابان"
    },
    {
        "question": "من الذي اخترع المصباح الكهربائي؟",
        "options": ["توماس أديسون", "نيكولا تسلا", "ألبرت أينشتاين", "غراهام بيل"],
        "correct": 0,
        "hint": "مخترع أمريكي شهير"
    },
]

# تهيئة حالة اللعبة
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.goals = 0
    st.session_state.shots = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.questions = random.sample(QUESTIONS, 5)  # 5 أسئلة لكل جولة

# العنوان
st.title("⚽ كرة القدم الثقافية")
st.markdown("---")

# عرض الملعب
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### 🏟️ الملعب")

# عرض الإحصائيات
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⭐ النقاط", st.session_state.score)
with col2:
    st.metric("⚽ الأهداف", st.session_state.goals)
with col3:
    st.metric("🎯 التسديدات", st.session_state.shots)
with col4:
    progress = (st.session_state.current_q) / len(st.session_state.questions)
    st.progress(progress, text=f"السؤال {st.session_state.current_q + 1}/{len(st.session_state.questions)}")

st.markdown("---")

# عرض السؤال الحالي
if st.session_state.current_q < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.current_q]
    
    st.markdown(f"### ❓ {q['question']}")
    
    # عرض التلميح
    with st.expander("💡 تلميح"):
        st.write(q['hint'])
    
    # عرض الخيارات
    options = q['options']
    cols = st.columns(2)
    
    for i, option in enumerate(options):
        with cols[i % 2]:
            # تعطيل الأزرار بعد الإجابة
            disabled = st.session_state.answered
            # تلوين الزر حسب الإجابة
            if st.session_state.answered and st.session_state.selected == i:
                if i == q['correct']:
                    btn_style = "✅ " + option
                else:
                    btn_style = "❌ " + option
            elif st.session_state.answered and i == q['correct']:
                btn_style = "✅ " + option
            else:
                btn_style = option
            
            if st.button(
                btn_style,
                key=f"q{i}",
                disabled=disabled,
                use_container_width=True
            ):
                st.session_state.answered = True
                st.session_state.selected = i
                st.session_state.shots += 1
                
                if i == q['correct']:
                    st.session_state.score += 10
                    st.session_state.goals += 1
                    st.success("⚽ **هدف!** إجابة صحيحة! +10 نقاط")
                    st.balloons()
                else:
                    st.error("❌ **ضربة حظ!** إجابة خاطئة")
                    
                st.rerun()
    
    # زر الانتقال للسؤال التالي
    if st.session_state.answered:
        if st.button("⏩ التالي", use_container_width=True):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.selected = None
            st.rerun()

else:
    # نهاية اللعبة
    st.markdown("### 🏆 نهاية المباراة!")
    st.markdown("---")
    
    # تقييم الأداء
    total = len(st.session_state.questions)
    goals = st.session_state.goals
    
    if goals == total:
        st.success("🌟🌟🌟 **رائع! سجلت في كل التسديدات! لاعب نجم!**")
    elif goals >= total * 0.6:
        st.success("⭐ **أداء ممتاز! أنت لاعب محترف!**")
    elif goals >= total * 0.4:
        st.info("👏 **أداء جيد! واصل التدريب!**")
    else:
        st.warning("📚 **تحتاج إلى مزيد من التدريب! العب مرة أخرى**")
    
    # عرض الإحصائيات النهائية
    col1, col2 = st.columns(2)
    with col1:
        st.metric("⚽ الأهداف", f"{goals}/{total}")
    with col2:
        st.metric("⭐ مجموع النقاط", st.session_state.score)
    
    # إعادة التشغيل
    if st.button("🔄 مباراة جديدة", use_container_width=True):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.goals = 0
        st.session_state.shots = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.questions = random.sample(QUESTIONS, 5)
        st.rerun()

# زخرفة
st.markdown("---")
st.caption("⚽ سجل هدفاً بكل إجابة صحيحة!")
