import streamlit as st

st.title("I'm a cat `<h1>`")
st.header("This is a header `<h2>`")
st.subheader(body="This is a subheader中見出し"
             ,anchor="title string `<h1>`",
             help="This is a help string",
             divider=True
             )
st.caption("This is a caption string `<h6>`")
st.text('''
I'm a cat
I don't have a name yet.
I don't know where I come from. I don't even know where I'm going.
I just live today and don't think about tomorrow.
'''
)
st.code('''
import streeamlit as st
st.snow()
'''
,language='python'
,line_numbers=True
        )
# st.snow()