import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime

# Load sample sales data and train a simple model
sales = pd.read_csv('data/sales_sample.csv')
sales['date'] = pd.to_datetime(sales['date'])
sales['dayofweek'] = sales['date'].dt.dayofweek
X = sales[['temperature', 'is_holiday', 'event', 'dayofweek']]
y = sales['pizzas_sold']
model = LinearRegression()
model.fit(X, y)

st.title("🍕 Carlo KI-Assistent")

# User inputs for today's conditions
heute = st.date_input("Datum", datetime.date.today())
temp = st.number_input("Temperatur (°C)", value=20)
feiertag = st.checkbox("Feiertag", value=False)
veranstaltung = st.checkbox("Event in der Nähe", value=False)

if st.button("Nachfrage vorhersagen"):
    dayofweek = heute.weekday()
    prediction = model.predict([[temp, int(feiertag), int(veranstaltung), dayofweek]])[0]
    gaeste = int(prediction * 1.2)
    pizzen = int(prediction)
    st.markdown(f"""
### 🤖 Carlo sagt:
**Bongiorno Chef Phillip!**
Heute ist **{heute.strftime('%A, der %d. %B')}** – wir erwarten **{gaeste} Gäste**.
Geplant sind **{pizzen} ganze Pizzen** bei {temp} °C.

Ich habe die Prep-Liste für die Küche und die Aufgaben fürs Front House auf die
Pads gespielt.
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
