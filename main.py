import streamlit as st

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