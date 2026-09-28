import streamlit as st
from gtts import gTTS
from io import BytesIO

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="P2 Spelling Practice",
    layout="wide"
)

# -----------------------------------
# AUDIO FUNCTION
# -----------------------------------

@st.cache_data
def generate_audio(text):
    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)

    return audio_buffer.getvalue()

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

    st.subheader(f"Word {i+1}")

    if st.button(
        f"🔊 Say Word {i+1}",
        key=f"audio_{selected_list}_{i}"
    ):
        audio = generate_audio(
            f"The word is {word}. I repeat. {word}."
        )

        st.audio(
            audio,
            format="audio/mp3"
        )

    answer = st.text_input(
        "Type the spelling",
        key=f"spell_{selected_list}_{i}"
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

st.divider()

# -----------------------------------
# SPELLING SCORE
# -----------------------------------

st.subheader("🌟 Spelling Score")

spelling_percent = spelling_score / len(words)

st.progress(spelling_percent)

st.write(
    f"Score: **{spelling_score}/{len(words)}**"
)

st.write(
    "⭐" * round(spelling_percent * 5)
)

# -----------------------------------
# DICTATION SECTION
# -----------------------------------

st.divider()

st.header("📝 Dictation Practice")

dictation_score = 0

for i, sentence in enumerate(dictation_sentences):

    st.subheader(f"Sentence {i+1}")

    if st.button(
        f"🔊 Read Sentence {i+1}",
        key=f"dictation_audio_{i}"
    ):
        audio = generate_audio(sentence)

        st.audio(
            audio,
            format="audio/mp3"
        )

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
                "Show Correct Sentence"
            ):
                st.write(sentence)

# -----------------------------------
# DICTATION SCORE
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

st.write(
    "⭐" * round(dictation_percent * 5)
)

# -----------------------------------
# READ FULL DICTATION
# -----------------------------------

st.divider()

if st.button("🎤 Read Full Dictation"):

    audio = generate_audio(
        " ".join(dictation_sentences)
    )

    st.audio(
        audio,
        format="audio/mp3"
    )

# -----------------------------------
# OVERALL RESULT
# -----------------------------------

st.divider()

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

st.header("🎯 Overall Achievement")

st.progress(overall_percent)

st.write(
    f"Total Score: **{total_correct}/{total_questions}**"
)

st.write(
    "⭐" * round(overall_percent * 5)
)

if total_correct == total_questions:
    st.balloons()
    st.success(
        "🎉 PERFECT SCORE! Excellent work!"
    )
