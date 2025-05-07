import streamlit as st

MONGO_URI = st.secrets["MONGO"]["URI"]
MONGO_DB_NAME = st.secrets["MONGO"]["DB_NAME"]
MONGO_COLLECTION_NAME = st.secrets["MONGO"]["COLLECTION_NAME"]