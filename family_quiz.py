import streamlit as st

st.set_page_config(page_title="Sisters Fun Quiz ❤️", layout="centered")

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
}
.title {
    text-align: center;
    font-size: 35px;
    color: #2c3e50;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">👭 Sisters Fun Quiz 💖</p>', unsafe_allow_html=True)

# ---------- QUESTIONS ----------
questions = [
    "Who works more? 💪",
    "Whom do you love more? ❤️",
    "Who is the most beautiful? 😍",
    "Who is the topper? 📚",
    "Who is the most intelligent? 🧠",
    "Who is Amma’s girl? 👩‍👧",
    "Who is Dad’s girl? 👨‍👧",
    "Who is all-in-one? 🌟",
    "Who is most sensitive? 🥺",
    "Who gets angry quickly? 😤",
    "Who is funniest? 😂",
    "Who supports the family most? 🤝",
    "Who cooks best? 🍲",
    "Who cares the most? 💖",
    "Who is strict? 😅",
    "Who is soft-hearted? 💕",
    "Who gives best advice? 🧠",
    "Who is everyone's favorite? 🫶",
    "Who understands others the most? 💭",
    "Who is the real queen? 👑",

    "Who wakes up early? 🌅",
    "Who sleeps the most? 😴",
    "Who spends more money? 💸",
    "Who saves money best? 💰",
    "Who is more stylish? 👗",
    "Who takes more selfies? 🤳",
    "Who is more responsible? 🧾",
    "Who is more lazy? 🛌",
    "Who studies more? 📖",
    "Who talks the most? 🗣️",
    "Who is more emotional? 😢",
    "Who is more confident? 😎",
    "Who is more caring to parents? ❤️",
    "Who is better at cooking Maggi? 🍜",
    "Who is more dramatic? 🎭",
    "Who is more friendly? 🤗",
    "Who is more hardworking? 🏃‍♀️",
    "Who is more naughty? 😜",
    "Who is more organized? 📂",
    "Who is the cutest? 🥰"
]

# ---------- OPTIONS ----------
options = ["Reshma 💖", "Sushma 💖", "Joshi 💖"]

# ---------- QUIZ ----------
answers = []

for i, q in enumerate(questions):
    ans = st.radio(f"{i+1}. {q}", options, key=i)
    answers.append(ans)

# ---------- SUBMIT ----------
if st.button("Submit 💌"):

    # Count scores
    score = {"Reshma 💖": 0, "Sushma 💖": 0, "Joshi 💖": 0}

    for ans in answers:
        score[ans] += 1

    # Find winner
    winner = max(score, key=score.get)

    st.balloons()
    st.success("❤️ Quiz Completed ❤️")

    st.write("## 🏆 Winner 👑")
    st.markdown(f"### {winner} is the Queen 👑💖")

    # Fun message
    if "Reshma" in winner:
        st.info("Reshma dominates 😎🔥")
    elif "Sushma" in winner:
        st.info("Sushma is the ultimate queen 👑✨")
    else:
        st.info("Joshi wins everyone's heart 💖🥰")

    # Show scores
    st.write("## 📊 Scores")
    for name, val in score.items():
        st.write(f"{name} : {val}")

    st.write("## 💌 Message")
    st.success("No matter what, we are always the best sisters together 💖👭")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("💖 Made with love for my sisters 💖")
