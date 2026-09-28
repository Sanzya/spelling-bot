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
# TEXT TO SPEECH
# -----------------------------------

import base64
from gtts import gTTS
from io import BytesIO
import streamlit.components.v1 as components

def speak(text):
    tts = gTTS(text=text, lang="en", slow=False)

    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)

    audio_bytes = mp3_fp.getvalue()
    audio_base64 = base64.b64encode(audio_bytes).decode()

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

score = 0

for i, word in enumerate(words):

    st.subheader(f"Word {i+1}")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button(
            f"🔊 Say Word",
            key=f"say_{i}"
        ):
            speak(
                f"{word}. I repeat. {word}"
            )

    with col2:

        answer = st.text_input(
            "Type the spelling here",
            key=f"answer_{selected_list}_{i}"
        )

    if answer:

        if answer.strip().lower() == word.lower():

            st.success("✅ Correct")

            score += 1

        else:

            st.error("❌ Incorrect")

            st.caption(
                f"Correct spelling: **{word}**"
            )

# -----------------------------------
# SPELLING RESULT
# -----------------------------------

st.divider()

star_count = round((score / len(words)) * 5)

st.subheader("🌟 Spelling Score")

st.progress(score / len(words))

st.write(
    f"Score: **{score}/{len(words)}**"
)

st.write(
    "⭐" * star_count
)

if score == len(words):
    st.balloons()
    st.success("Amazing! Perfect score!")

# -----------------------------------
# DICTATION PRACTICE
# -----------------------------------

st.divider()

st.header("📝 Dictation Practice")

dictation_score = 0

for i, sentence in enumerate(dictation_sentences):

    st.subheader(
        f"Sentence {i+1}"
    )

    if st.button(
        f"🔊 Read Sentence {i+1}",
        key=f"dictation_audio_{i}"
    ):
        speak(sentence)

    user_sentence = st.text_area(
        "Type what you hear",
        key=f"dictation_{i}",
        height=80
    )

    if user_sentence:

        normalized_answer = (
            user_sentence.strip()
            .lower()
            .replace(".", "")
        )

        normalized_sentence = (
            sentence.strip()
            .lower()
            .replace(".", "")
        )

        if normalized_answer == normalized_sentence:

            st.success("✅ Correct")

            dictation_score += 1

        else:

            st.error("❌ Not quite right")

            with st.expander(
                "Show Correct Sentence"
            ):
                st.write(sentence)

# -----------------------------------
# DICTATION RESULT
# -----------------------------------

st.divider()

st.subheader("🏆 Dictation Score")

st.progress(
    dictation_score /
    len(dictation_sentences)
)

st.write(
    f"Score: **{dictation_score}/{len(dictation_sentences)}**"
)

dictation_stars = round(
    (dictation_score /
     len(dictation_sentences)) * 5
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
# OVERALL RESULT
# -----------------------------------

st.divider()

total_correct = score + dictation_score
total_questions = len(words) + len(dictation_sentences)

st.header("🎯 Overall Achievement")

st.progress(
    total_correct / total_questions
)

st.write(
    f"Total Score: **{total_correct}/{total_questions}**"
)

overall_stars = round(
    (total_correct /
     total_questions) * 5
)

st.write(
    "⭐" * overall_stars
)

if total_correct == total_questions:
    st.balloons()
    st.success(
        "🌟 PERFECT! You got everything correct!"
    )
