import streamlit as st
import plotly.express as px
from backend import get_overall_level, get_sentence_levels

st.title("ToneTeller")
st.header("I will analyze the tone of your text")

text = st.text_area("Enter text here: ")

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


    
    


    #try:
    sentences_scores = get_sentence_levels(text)
    count = [i for i in range(len(sentences_scores))]


    overall = [score['compound'] for score in sentences_scores]
    overall_count = [i for i in range(len(overall))]

    col3, middle1, col4 = st.columns([0.5, 2, 0.5])

    with middle1:
        overall_graph = px.bar(x = overall_count, y = overall, labels = {"x": "Sentence Number", "y": "Emotion Level"})
        st.plotly_chart(overall_graph, use_container_width=True)


    col1, middle, col2 = st.columns([2, 0.5, 2])

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
    
    
    with col1:
        graph = px.line(x = count, y = s_positivity, labels = {"x": "Sentence Number", "y": "Positivity"})
        st.plotly_chart(graph, use_container_width=True)

    with col2:
        graph2 = px.line(x = count, y = s_negativity, labels = {"x": "Sentence Number", "y": "Negativity"})
        st.plotly_chart(graph2, use_container_width=True)
    # except:
    #     st.error("Make sure you use punctuation to end your sentence(s).")




