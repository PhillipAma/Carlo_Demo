import streamlit as st
import datetime

heute = datetime.date.today()
wetter = "14 °C und Sonne"
gaeste = 160
pizzen = 100

st.markdown(f"""
### 🤖 Carlo sagt:
**Bongiorno Chef Phillip!**  
Heute ist **{heute.strftime('%A, der %d. %B')}** – wir erwarten **{gaeste} Gäste**.  
Geplant sind **{pizzen} ganze Pizzen** bei {wetter}.

Ich habe die Prep-Liste für die Küche und die Aufgaben fürs Front House auf die Pads gespielt.  
👉 Möchtest du sie sehen?
""")

station = st.selectbox("Wähle eine Station:", ["Front House", "Prep-Küche", "Pizza Station"])

if station == "Front House":
    st.subheader("📍 Front House – Aufgaben")
    st.markdown("""
- Eingangsbereich und Tische desinfizieren  
- Kreidetafel mit Tagesangebot aufstellen  
- QR-Menüs prüfen  
- Eistee-Spender befüllen
""")

elif station == "Prep-Küche":
    st.subheader("👨‍🍳 Prep-Küche – Zutatenliste")
    st.markdown("""
- Teig: 12 kg (inkl. 10 % Puffer)  
- Tomatensauce: 9 Liter  
- Mozzarella: 7 kg  
- Basilikum & Öl: bereitstellen
""")

elif station == "Pizza Station":
    st.subheader("🔥 Pizza Station – Setup")
    st.markdown("""
- Station aufbauen (Teig, Saucen, Toppings)  
- Schaufel & Messer bereitstellen  
- 10 Margheritas bis 11:30 vorproduzieren  
- 30× Slice, 20× Half, 50× Whole vorbereiten
""")
