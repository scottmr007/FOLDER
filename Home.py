import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Me.jpg")
    
with col2:
    st.title("Scott Rutter")
    content = """
    Working on improving Python skills and Data Science/ Machine Learning. Graduated with a degree in Intelligence and Analysis.
    """
    st.info(content)
    
content2 = """
Currently working through, 'Python Mega Course' from Ardit Sulce. I'm in the Monkey see, Monkey do phase.
So, the next several projects will be from the course.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")