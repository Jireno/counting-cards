import streamlit as st

st.title("Blackjack Card Counter")
st.write("Seleziona una carta per aggiornare il Running Count.")

conteggio_hi_lo = {2: +1, 3: +1, 4: +1, 5: +1, 6: +1, 
                   7: 0, 8: 0, 9: 0, 10: -1, 11: -1}

if "running_count" not in st.session_state:
    st.session_state.running_count = 0

def aggiorna_conteggio(carta):
    st.session_state.running_count += conteggio_hi_lo.get(carta, 0)

for card in range(2, 12):
    if st.button(f"Carta {card}"):
        aggiorna_conteggio(card)

st.write(f"**Running Count Attuale:** {st.session_state.running_count}")
