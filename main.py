import streamlit as st
import plotly.express as px
from backend import get_sentence_levels, get_words, get_emojis, get_filtered_words
import pandas as pd


st.title("ToneTeller")
st.header("I will analyze the tone of your text 🔮✨")

text = st.text_area("Enter text here: ")

if text:

    try:
        sentences_scores = get_sentence_levels(text)[1:]
        count = [i for i in range(len(sentences_scores))]
        emoji = ["✨🔮✨" for i in count]


        overall = [score['compound'] for score in sentences_scores]
        overall_count = [(i+1) for i in range(len(overall))]
        tones = [get_words(score) for score in overall]
        emotions_emojis = [get_emojis(score) for score in overall]

        st.divider()

        st.header("✨💫🔮 Your Sentiment Fortune: 🔮🌙✨")

        #st.divider()
        st.subheader("📊 Overall Sentiment by Sentence")
        col5, middle2, col6 = st.columns([0.5, 2, 0.5])
       #with middle2:
        tones_graph = px.bar(x = overall_count, y = overall, text = emoji, hover_name = [tones[i]+emotions_emojis[i] for i in range(len(overall))], labels = {"x": "Sentence Number", "y": "Compound Sentiment"})
        st.plotly_chart(tones_graph, width='stretch')


        st.divider()
        st.subheader("🗂️ Tone Analysis Table")
        col3, middle1, col4 = st.columns([0.5, 2, 0.5])
        #with middle1:
        df = pd.DataFrame({"Sentence #": overall_count, "Compound Score": overall, "Tone": tones, "Emotions": emotions_emojis})
        st.dataframe(df, width='stretch', hide_index = True)

        
        st.divider() 
        st.subheader("📈 Positivity vs Negativity 📉 Trends")
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
            graph = px.line(x = count, y = s_positivity, labels = {"x": "Sentence Number", "y": "Positivity"}, title = "Positivity 😄😍🤩😁🎉")
            st.plotly_chart(graph, width='stretch')

        with col2:
            graph2 = px.line(x = count, y = s_negativity, labels = {"x": "Sentence Number", "y": "Negativity"}, title = "Negativity 😞💔😢😡😤")
            st.plotly_chart(graph2, width='stretch')

        st.divider()
        st.subheader("📋 Word Frequency Analysis")
        st.caption("(Excluding English stopwords)")

        words = [item[0] for item in get_filtered_words(text.lower())]
        counts = [item[1] for item in get_filtered_words(text.lower())]
        df2 = pd.DataFrame({"Word": words, "Frequency": counts})
        st.dataframe(df2, width='stretch', hide_index = True)

    except:
        st.error("Make sure you use punctuation to end your sentence(s).")




