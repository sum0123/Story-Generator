import numpy as np
import pandas as pd
import os
import re
import string
import nltk
import streamlit as st

# nltk.download("all")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
from model import make_markov_model
from data_preprocess import read_all_stories, clean_txt


story_path = r"sherlock\sherlock"
stories = read_all_stories(story_path)
cleaned_stories = clean_txt(stories)
markov_model = make_markov_model(cleaned_stories)


def generate_story(markov_model, limit, start):
    n = 0
    curr_state = start
    next_state = None
    story = ""
    story += curr_state + " "
    while n < limit:
        next_state = random.choices(
            list(markov_model[curr_state].keys()),
            list(markov_model[curr_state].values()),
        )

        curr_state = next_state[0]
        story += curr_state + " "
        n += 1
    return story


# for i in range(20):
#     print(str(i) + ". ", generate_story(markov_model, limit=20, start="dear holmes"))


# Main function to run Streamlit app
def main():
    st.title("Markov Model Story Generator")
    limit = st.number_input(
        "Enter the limit for story generation",
        min_value=1,
        max_value=100,
        value=20,
        step=1,
    )
    start = st.text_input("Enter the starting text")

    if st.button("Enter"):
        st.write("Generated Story:")
        st.write(generate_story(markov_model, limit, start))


# if __name__ == "__main__":
#     nltk.download("punkt")
#     nltk.download("stopwords")
#     with open("your_text_file.txt", "r") as file:2
#         text_data = file.read()
#     markov_model = build_markov_model(text_data)
#     main()
if __name__ == "__main__":
    main()
