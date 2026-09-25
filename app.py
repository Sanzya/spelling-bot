import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="P2 Spelling Practice", layout="wide")

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
# DICTATION 7
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

    st.subheader(f"Word {i+1}")

    if st.button(f"🔊 Say Word {i+1}", key=f"say_{selected_list}_{i}"):

        speech = f"""
        <script>
        var msg = new SpeechSynthesisUtterance(
        "{word}. I repeat. {word}");
        msg.rate = 0.8;
        speechSynthesis.speak(msg);
        </script>
        """

        components.html(speech, height=0)

    answer = st.text_input(
        "Type the spelling",
        key=f"{selected_list}_answer_{i}"
    )

    if answer:

        letters = " ".join(list(word.upper()))

        if answer.strip().lower() == word.lower():

            st.success("✅ Correct!")

            speech = f"""
            <script>
            var msg = new SpeechSynthesisUtterance(
            "Excellent. The spelling is {letters}");
            speechSynthesis.speak(msg);
            </script>
            """

            components.html(speech, height=0)

        else:

            st.error("❌ Try Again")

            speech = f"""
            <script>
            var msg = new SpeechSynthesisUtterance(
            "Not quite. The correct spelling is {letters}");
            speechSynthesis.speak(msg);
            </script>
            """

            components.html(speech, height=0)

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

        speech = f"""
        <script>
        var msg = new SpeechSynthesisUtterance(
        "{sentence}");
        msg.rate = 0.7;
        speechSynthesis.speak(msg);
        </script>
        """

        components.html(speech, height=0)

with col2:
    if st.button("➡ Next Sentence"):

        if st.session_state.current_sentence < len(dictation_sentences)-1:
            st.session_state.current_sentence += 1

with col3:
    if st.button("🔄 Restart Dictation"):
        st.session_state.current_sentence = 0

st.info(
    f"Sentence {st.session_state.current_sentence+1} of {len(dictation_sentences)}"
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
# OPTIONAL: READ ALL
# -------------------------------

if st.button("🎤 Read Full Dictation"):

    full_text = (
        " ".join(dictation_sentences)
    )

    speech = f"""
    <script>
    var msg = new SpeechSynthesisUtterance(
    "{full_text}");
    msg.rate = 0.7;
    speechSynthesis.speak(msg);
    </script>
    """

    components.html(speech, height=0)