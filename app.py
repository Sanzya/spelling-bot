import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="P2 Spelling Practice",
    layout="wide"
)

st.markdown("""
<style>

/* App background */
.stApp {
    background: linear-gradient(180deg, #f8f9ff 0%, #eef2ff 100%);
}

/* Main container */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Hide header */
header[data-testid="stHeader"] {
    display: none;
}

/* Title */
h1 {
    color: #2d3748 !important;
    font-weight: 800 !important;
}

/* Subtitles */
h2, h3 {
    color: #4a5568 !important;
}

/* Info box */
[data-testid="stAlert"] {
    border-radius: 16px !important;
    border: none !important;
}

/* Text area */
textarea {
    border-radius: 16px !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    border: none;
    border-radius: 12px;
    height: 50px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg,#4f46e5,#7c3aed);
}

/* Select box */
.stSelectbox > div > div {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title="GP Memory Coach",
    page_icon="🎓",
    layout="wide"
)

# Hide Streamlit toolbar/header
st.markdown("""
<style>
[data-testid="stHeader"] {
    display: none;
}

[data-testid="stToolbar"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SPEAK FUNCTION
# -----------------------------------

from gtts import gTTS
from io import BytesIO
import streamlit as st

def speak(text):
    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    st.audio(
        audio_buffer.read(),
        format="audio/mp3",
        autoplay=True
    )

# -----------------------------------
# SPELLING LISTS
# -----------------------------------

spelling_lists = {
    "Spelling 19": [
        "different",
        "event",
        "fabulous",
        "flapped",
        "furious",
        "invitations",
        "midnight",
        "swooshing",
        "thumped",
        "wonderful"
    ],
    "Spelling 20": [
        "decorated",
        "everyone",
        "feast",
        "homemade",
        "party",
        "place",
        "pranced",
        "problem",
        "stamped",
        "swung"
    ],
    "Spelling 21": [
        "bully",
        "enclosure",
        "extinct",
        "hunt",
        "intelligent",
        "panicked",
        "roam",
        "scientists",
        "stroll",
        "terrifying"
    ]
}

# -----------------------------------
# DICTATION
# -----------------------------------

dictation_sentences = [
    "It was my eighth birthday.",
    "I invited all my classmates to my party.",
    "Everyone came and had a fabulous time.",
    "They enjoyed the delicious food and games.",
    "It was a wonderful day."
]

# -----------------------------------
# TITLE
# -----------------------------------

st.title("📚 P2 Spelling & Dictation Practice")

selected_list = st.selectbox(
    "Choose Spelling List",
    list(spelling_lists.keys())
)

words = spelling_lists[selected_list]

# -----------------------------------
# SPELLING PRACTICE
# -----------------------------------

st.header("✏️ Spelling Practice")

spelling_score = 0

for i, word in enumerate(words):

    st.markdown(f"### Word {i+1}")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button(
            f"🔊 Say Word {i+1}",
            key=f"say_word_{i}"
        ):
            speak(
                f"The word is {word}. I repeat. {word}."
            )

    with col2:
        answer = st.text_input(
            "Type your spelling",
            key=f"spell_{i}"
        )

    if answer:

        if answer.strip().lower() == word.lower():

            st.success("✅ Correct")
            spelling_score += 1

        else:

            st.error("❌ Incorrect")
            st.write(
                f"Correct spelling: **{word}**"
            )

# -----------------------------------
# SPELLING RESULT
# -----------------------------------

st.divider()

st.subheader("🌟 Spelling Score")

spelling_percent = spelling_score / len(words)

st.progress(spelling_percent)

st.write(
    f"Score: **{spelling_score}/{len(words)}**"
)

spelling_stars = round(spelling_percent * 5)

st.write("⭐" * spelling_stars)

# -----------------------------------
# DICTATION
# -----------------------------------

st.divider()

st.header("📝 Dictation Practice")

dictation_score = 0

for i, sentence in enumerate(dictation_sentences):

    st.markdown(f"### Sentence {i+1}")

    if st.button(
        f"🔊 Read Sentence {i+1}",
        key=f"read_sentence_{i}"
    ):
        speak(sentence)

    user_answer = st.text_area(
        "Write the sentence",
        key=f"dictation_{i}",
        height=80
    )

    if user_answer:

        correct = (
            sentence.lower()
            .replace(".", "")
            .replace(",", "")
            .strip()
        )

        student = (
            user_answer.lower()
            .replace(".", "")
            .replace(",", "")
            .strip()
        )

        if student == correct:

            st.success("✅ Correct")
            dictation_score += 1

        else:

            st.error("❌ Incorrect")

            with st.expander(
                "Show Correct Answer"
            ):
                st.write(sentence)

# -----------------------------------
# DICTATION RESULT
# -----------------------------------

st.divider()

st.subheader("🏆 Dictation Score")

dictation_percent = (
    dictation_score /
    len(dictation_sentences)
)

st.progress(dictation_percent)

st.write(
    f"Score: **{dictation_score}/{len(dictation_sentences)}**"
)

dictation_stars = round(
    dictation_percent * 5
)

st.write(
    "⭐" * dictation_stars
)

# -----------------------------------
# READ FULL DICTATION
# -----------------------------------

st.divider()

if st.button("🎤 Read Full Dictation"):

    full_text = " ".join(
        dictation_sentences
    )

    speak(full_text)

# -----------------------------------
# OVERALL SCORE
# -----------------------------------

st.divider()

st.header("🎯 Overall Achievement")

total_correct = (
    spelling_score +
    dictation_score
)

total_questions = (
    len(words) +
    len(dictation_sentences)
)

overall_percent = (
    total_correct /
    total_questions
)

st.progress(overall_percent)

st.write(
    f"Total Score: **{total_correct}/{total_questions}**"
)

overall_stars = round(
    overall_percent * 5
)

st.write("⭐" * overall_stars)

if total_correct == total_questions:
    st.balloons()
    st.success(
        "🎉 PERFECT SCORE! Amazing work!"
    )
