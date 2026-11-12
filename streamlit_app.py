import streamlit as st
from transformers import pipeline

st.title("Translating application")

st.image("images/eng_to_ger.png")

st.write("Model used for translation isL 'Helsinki-NLP/opus-mt-en-de' ")
st.write("✨Thanks to Hugging Face for the model :3✨")

st.write("----------------")
st.write("So just to make sure everything would work correctly for this app:")
st.write("- Install the libraries")
st.code("pip install -r requirements.txt")
st.write("- After that the program should work correctly✨")
st.write("Oh, and sadly the program won't work on transformers v5")
st.write("It's a bit harder there, sorry T-T")
st.write("----------------")

text = st.text_area(label="Enter text here please")
if text:
    text = text.strip()
    if text == "":
        st.write("You didn't enter any text? Why?")
    else:
        st.write("Thanks for the text, translating it now!")

        st.write("(づ ◕‿◕ )づ work-work-work")

        answer = ""
        try:
            model = pipeline(task="translation", model="Helsinki-NLP/opus-mt-en-de")
            answer = model(text)[0]["translation_text"]
        except IndexError as e:
            st.write("IT'S TOO LONG (つ﹏⊂)")
            st.write(e)

        if (answer != text and answer != "" and
                answer.lower() != text.lower()):
            st.write("---------------------------")
            st.write("ᕙ(⇀‸↼‶)ᕗ I did it!")
            st.write("Here you go: ")
            st.write(f"--> {answer}")
        else:
            st.write("---------------------------")
            st.write("Sooooo uhm ╥﹏╥")
            st.write("I couldn't translate it unfortunately")
            st.write("Are you sure it's in english? Or maybe it doesn't really need translation?")


st.write("---------------------------")
st.markdown(":gray[The program made by s30355 - Maryia K. <3]")