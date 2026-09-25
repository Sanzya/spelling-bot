import streamlit as st
from gtts import gTTS
from io import BytesIO

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="P2 Spelling Practice",
    layout="wide"
)

# Make audio player smaller
st.markdown("""
<style>
audio {
    width: 250px;
    height: 35px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TEXT TO SPEECH
# -------------------------------

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
        format="audio/mp3"
    )

# -------------------------------
# SPELLING LISTS
# -------------------------------

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

# -------------------------------
# DICTATION
# -------------------------------

dictation_sentences = [
    "It was my eighth birthday.",
    "I invited all my classmates to my party.",
    "Everyone came and had a fabulous time.",
    "They enjoyed the delicious food and games.",
    "It was a wonderful day."
]

# -------------------------------
# TITLE
# -------------------------------

st.title("📚 P2 Spelling Practice")

selected_list = st.selectbox(
    "Choose Spelling List",
    list(spelling_lists.keys())
)

words = spelling_lists[selected_list]

# -------------------------------
# SPELLING PRACTICE
# -------------------------------

st.header(selected_list)

for i, word in enumerate(words):

    st.subheader(f"Word {i + 1}")

    if st.button(
        f"🔊 Say Word {i + 1}",
        key=f"say_{selected_list}_{i}"
    ):
        speak(f"{word}. I repeat. {word}")

    answer = st.text_input(
        "Type the spelling",
        key=f"{selected_list}_answer_{i}"
    )

    if answer:

        letters = " ".join(list(word.upper()))

        if answer.strip().lower() == word.lower():

            st.success("✅ Correct!")

            speak(
                f"Excellent. The spelling is {letters}"
            )

        else:

            st.error("❌ Try Again")

            speak(
                f"Not quite. The correct spelling is {letters}"
            )

# -------------------------------
# DICTATION PRACTICE
# -------------------------------

st.divider()

st.header("📝 Dictation 7")

if "current_sentence" not in st.session_state:
    st.session_state.current_sentence = 0

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("🔊 Read Current Sentence"):

        sentence = dictation_sentences[
            st.session_state.current_sentence
        ]

        speak(sentence)

with col2:

    if st.button("➡ Next Sentence"):

        if st.session_state.current_sentence < len(dictation_sentences) - 1:
            st.session_state.current_sentence += 1

with col3:

    if st.button("🔄 Restart Dictation"):

        st.session_state.current_sentence = 0

st.info(
    f"Sentence {st.session_state.current_sentence + 1} of {len(dictation_sentences)}"
)

st.write(
    "The student listens first, then writes the sentence."
)

st.text_area(
    "Type your dictation here",
    height=250,
    key="dictation_answer"
)

# -------------------------------
# READ FULL DICTATION
# -------------------------------

if st.button("🎤 Read Full Dictation"):

    full_text = " ".join(dictation_sentences)

    speak(full_text)
`
