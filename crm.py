import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Community CRM", layout="wide")
st.title("🚀 Business Emotion CRM - Community Edition")

# Nome del file dove verranno salvati i dati
DB_FILE = "database_crm.csv"

# Funzione per caricare i dati dal file
def carica_dati():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    return pd.DataFrame(columns=["Nome", "Mercato", "Emozione"])

# Inizializziamo i dati prendendoli dal file
if 'agenda' not in st.session_state:
    st.session_state.agenda = carica_dati()

with st.sidebar:
    st.header("👤 Nuovo Contatto")
    nome = st.text_input("Nome e Cognome")
    mercato = st.selectbox("Tipo Mercato", ["Freddo", "Tiepido", "Caldo"])
    emozione = st.selectbox("Colore Emozione", ["🔴 Rosso", "🟡 Giallo", "🟢 Verde", "🔵 Blu"])
    
    if st.button("➕ SALVA NEL DATABASE"):
        if nome:
            nuovo = pd.DataFrame([[nome, mercato, emozione]], columns=["Nome", "Mercato", "Emozione"])
            # Aggiorna la memoria dell'app
            st.session_state.agenda = pd.concat([st.session_state.agenda, nuovo], ignore_index=True)
            # Salva fisicamente sul file CSV
            st.session_state.agenda.to_csv(DB_FILE, index=False)
            st.success(f"Salvato e archiviato!")

# Visualizzazione colonne
st.markdown("---")
col1, col2, col3 = st.columns(3)

def mostra_tabella(tipo, colonna, colore_box):
    dati_filtrati = st.session_state.agenda[st.session_state.agenda["Mercato"] == tipo]
    colonna.markdown(f"### {colore_box} {tipo.upper()}")
    colonna.table(dati_filtrati[["Nome", "Emozione"]])

mostra_tabella("Freddo", col1, "❄️")
mostra_tabella("Tiepido", col2, "🔥")
mostra_tabella("Caldo", col3, "☀️")

# Tasto per scaricare tutto in Excel/CSV
st.sidebar.markdown("---")
csv = st.session_state.agenda.to_csv(index=False).encode('utf-8')
st.sidebar.download_button("📥 Scarica Database (Excel)", csv, "database_crm.csv", "text/csv")