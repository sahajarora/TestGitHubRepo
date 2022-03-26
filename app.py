import pandas as pd 
import streamlit as st 
from st_aggrid import AgGrid

st.set_page_config(page_title="IB File", layout="wide") 
st.title("IB File")

shows = pd.read_csv("./usa.txt",on_bad_lines='warn',sep="|")  

AgGrid(shows)