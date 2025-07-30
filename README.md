# Carlo Demo

Dieses Repository demonstriert einen einfachen Prototyp eines KI-Assistenzsystems für Gastronomiebetriebe. Die Anwendung basiert auf [Streamlit](https://streamlit.io/) und nutzt historische Beispieldaten, um eine grobe Nachfrageprognose für Pizzen zu erstellen.

## Installation

```bash
pip install -r requirements.txt
```

## Anwendung starten

```bash
streamlit run Carlo_app.py
```

Im Browser können Temperatur, Datum, Feiertag und Event ausgewählt werden. Anschließend zeigt Carlo eine prognostizierte Menge an benötigten Pizzen sowie die Aufgaben für die ausgewählte Station an.
