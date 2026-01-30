import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Community CRM", layout="wide")
st.title("🚀 Business Emotion CRM - Online")

url = "https://docs.google.com/spreadsheets/d/1vpu16Y_H093fk708541Ptw01h1wEt1PF1FRG6RsXSao/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

# Lettura dati sicura
try:
    df = conn.read(spreadsheet=url)
    if df.empty or "Mercato" not in df.columns:
        df = pd.DataFrame(columns=["Nome", "Mercato", "Emozione"])
except:
    df = pd.DataFrame(columns=["Nome", "Mercato", "Emozione"])

with st.sidebar:
    st.header("👤 Nuovo Contatto")
    nome = st.text_input("Nome e Cognome")
    mercato = st.selectbox("Tipo Mercato", ["Freddo", "Tiepido", "Caldo"])
    emozione = st.selectbox("Colore Emozione", ["🔴 Rosso", "🟡 Giallo", "🟢 Verde", "🔵 Blu"])
    
    if st.button("➕ SALVA NEL CLOUD"):
        if nome:
            nuovo = pd.DataFrame([[nome, mercato, emozione]], columns=["Nome", "Mercato", "Emozione"])
            updated_df = pd.concat([df, nuovo], ignore_index=True)
            conn.update(spreadsheet=url, data=updated_df)
            st.success("Dati salvati! Ricarica la pagina.")
            st.rerun()

# Visualizzazione Tabelle
col1, col2, col3 = st.columns(3)
with col1:
    st.error("❄️ FREDDO")
    st.dataframe(df[df["Mercato"] == "Freddo"])
with col2:
    st.warning("🔥 TIEPIDO")
    st.dataframe(df[df["Mercato"] == "Tiepido"])
with col3:
    st.success("☀️ CALDO")
    st.dataframe(df[df["Mercato"] == "Caldo"])



