import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from nltk.corpus import words


from password_generators import (
    RandomPasswordGenerator,
    MemorablePasswordGenerator,
    PinCodeGenerator,
)

st.image(str(ROOT_DIR / "images/banner.jpeg"))
st.title(":zap: Password Generator App")

col1, col2 = st.columns(2)

with col1:
    option = st.radio(
        "Password Type", ("Pin Code", "Random Password", "Memorable Password")
    )

    if option == "Random Password":
        length = st.slider("Length", min_value=4, max_value=32, value=8, step=4)
        include_numbers = st.toggle("Include Numbers")
        include_symbols = st.toggle("Include Symbols")

        generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
    elif option == "Memorable Password":
        no_of_words = st.slider("Number of Words", min_value=2, max_value=10, value=5)
        separator = st.text_input("Separator", value="-")
        capitalization = st.toggle("Capitalization")

        generator = MemorablePasswordGenerator(
            no_of_words, separator, capitalization, words.words()
        )
    else:
        length = st.slider("Length", min_value=8, max_value=32, value=4, step=4)

        generator = PinCodeGenerator(length)


with col2:
    button = st.button("Generate Password", type="primary")

    if button:
        password = generator.generate()
        st.write("Your password is:")
        st.subheader(rf"``` {password} ```")
