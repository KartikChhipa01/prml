import Model1
import DatasetExplain
import Introduction
import streamlit as st
PAGES={
    "Introduction": Introduction,
    "1": Model1,
    "Dataset":DatasetExplain,
    
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()