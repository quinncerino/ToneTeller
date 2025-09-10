import streamlit as st
import plotly.express as px
from backend import get_overall_level, get_sentence_levels

st.title("ToneTeller")
st.header("I will analyze the tone of your text")

text = st.text_input("Enter text here: ")

if text:
    scores_list = get_overall_level(text)
    print(scores_list)

    positivity = []
    for item in scores_list:
        positivity.append(item['pos'])
    st.subheader(f"Positivity: {positivity[0]}")

    negativity = []
    for item in scores_list:
        negativity.append(item['neg'])
    st.subheader(f"Negativity: {negativity[0]}")




    try:
        sentences_scores = get_sentence_levels(text)

        s_positivity = []
        #i = 0
        for item in sentences_scores:
            s_positivity.append(item['pos'])
        #st.subheader(f"Positivity: {s_positivity[i]}")

        s_negativity = []
        for item in sentences_scores:
            s_negativity.append(item['neg'])
        #st.subheader(f"Negativity: {s_negativity[i]}")
        #i += 1
        
        count = [(i + 1) for i in range(len(sentences_scores))]
        
        graph = px.line(x = count, y = s_positivity, labels = {"x": "Sentence Number", "y": "Positivity"})
        st.plotly_chart(graph)

        graph2 = px.line(x = count, y = s_negativity, labels = {"x": "Sentence Number", "y": "Negativity"})
        st.plotly_chart(graph2)
    except:
        st.error("Make sure you use punctuation to end your sentence(s).")




