import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64
import streamlit.components.v1 as components

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="P2 Spelling Practice",
    layout="wide"
)

# -----------------------------------
# SPEAK FUNCTION (NO AUDIO BAR)
# -----------------------------------

def speak(text):
    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)

    audio_base64 = base64.b64encode(
        mp3_fp.getvalue()
    ).decode()

    components.html(
        f"""
        <audio autoplay>
            data:audio/mp3;base64,{audio_base64}
        </audio>
        """,
        height=0,
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
# DICTATION SENTENCES
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
# SPELLING SECTION
# -----------------------------------

st.header("✏️ Spelling Practice")

spelling_score = 0

for i, word in enumerate(words):

    st.markdown(f"### Word {i+1}")

    if st.button(
        f"🔊 Say Word {i+1}",
        key=f"say_word_{i}"
    ):
        speak(
            f"The word is {word}. I repeat. {word}."
        )

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

# -----------------------------------
# SPELLING SCORE
# -----------------------------------

st.divider()

st.subheader("🌟 Spelling Result")

st.progress(
    spelling_score / len(words)
)

st.write(
    f"Score: {spelling_score}/{len(words)}"
)

stars = round(
    spelling_score / len(words) * 5
)

st.write("⭐" * stars)

# -----------------------------------
# DICTATION SECTION
# -----------------------------------

st.divider()

st.header("📝 Dictation Practice")

dictation_score = 0

for i, sentence in enumerate(dictation_sentences):

    st.markdown(f"### Sentence {i+1}")

    if st.button(
        f"🔊 Read Sentence {i+1}",
        key=f"dict_audio_{i}"
    ):
        speak(sentence)

    user_answer = st.text_area(
        "Write the sentence",
        key=f"dictation_answer_{i}",
        height=80
    )

    if user_answer:

        actual = (
            sentence.lower()
            .replace(".", "")
            .strip()
        )

        student = (
            user_answer.lower()
            .replace(".", "")
            .strip()
        )

        if student == actual:

            st.success("✅ Correct")

            dictation_score += 1

        else:

            st.error("❌ Incorrect")

            with st.expander(
                "Show Correct Answer"
            ):
                st.write(sentence)

# -----------------------------------
# DICTATION SCORE
# -----------------------------------

st.divider()

st.subheader("🏆 Dictation Result")

st.progress(
    dictation_score /
    len(dictation_sentences)
)

st.write(
    f"Score: {dictation_score}/{len(dictation_sentences)}"
)

dictation_stars = round(
    dictation_score /
    len(dictation_sentences) * 5
)

st.write("⭐" * dictation_stars)

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
# OVERALL RESULT
# -----------------------------------

st.divider()

total_score = (
    spelling_score +
    dictation_score
)

total_questions = (
    len(words) +
    len(dictation_sentences)
)

st.header("🎯 Overall Achievement")

st.progress(
    total_score /
    total_questions
)

st.write(
    f"Total Score: {total_score}/{total_questions}"
)

overall_stars = round(
    total_score /
    total_questions * 5
)

st.write("⭐" * overall_stars)

if total_score == total_questions:
    st.balloons()
    st.success(
        "🎉 Perfect Score! Excellent work!"
    )
