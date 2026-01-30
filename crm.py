import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetConnection

st.set_page_config(page_title="Community CRM", layout="wide")
st.title("🚀 Business Emotion CRM - Online")

# QUI INCOLLERAI IL TUO LINK TRA LE VIRGOLETTE
url = "https://docs.google.com/spreadsheets/d/1wpul6Y_H09Jfk7O0S41PtwDlh1wEtiPF1fRG6RsXSao/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetConnection)

# Caricamento dati
try:
    df = conn.read(spreadsheet=url)
except:
    df = pd.DataFrame(columns=["Nome", "Mercato", "Emozione"])

with st.sidebar:
    st.header("👤 Nuovo Contatto")
    nome = st.text_input("Nome e Cognome")
    mercato = st.selectbox("Tipo Mercato", ["Freddo", "Tiepido", "Caldo"])
    emozione = st.selectbox("Colore Emozione", ["🔴 Rosso", "🟡 Giallo", "🟢 Verde", "🔵 Blu"])
    
    if st.button("➕ SALVA NEL CLOUD"):
        if nome:
            nuovo_contatto = pd.DataFrame([[nome, mercato, emozione]], columns=["Nome", "Mercato", "Emozione"])
            updated_df = pd.concat([df, nuovo_contatto], ignore_index=True)
            conn.update(spreadsheet=url, data=updated_df)
            st.success("Dati salvati sul Cloud!")
            st.rerun()

# Visualizzazione Tabelle
col1, col2, col3 = st.columns(3)
col1.error("❄️ FREDDO")
col1.table(df[df["Mercato"] == "Freddo"])

col2.warning("🔥 TIEPIDO")
col2.table(df[df["Mercato"] == "Tiepido"])

col3.success("☀️ CALDO")
col3.table(df[df["Mercato"] == "Caldo"])
Non ce n'è
