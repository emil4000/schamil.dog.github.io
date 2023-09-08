import streamlit as st
import pandas as pd
import datetime


# Beispiel-Daten für Lebensmittel und Vitamine
food_data = {
    "Lebensmittel": ["Apfel", "Banane", "Karotte", "Spinat", "Ei"],
    "Vitamine": ["Vitamin A, C", "Vitamin B6, C", "Vitamin A, K", "Vitamin A, C, K", "Vitamin D, B12"]
}

food_df = pd.DataFrame(food_data)

# Streamlit App
st.title("Lebensmittel-Vitamin-Checker")

# Eingabefeld für Lebensmittel
selected_food = st.selectbox("Wähle ein Lebensmittel:", food_df["Lebensmittel"])

# Suche nach dem ausgewählten Lebensmittel
selected_food_vitamins = food_df.loc[food_df["Lebensmittel"] == selected_food, "Vitamine"].values[0]

# Anzeige der Vitamine
st.subheader("Vitamine in ausgewähltem Lebensmittel:")
st.write(selected_food_vitamins)

# Streamlit App
st.title("Essens- und Kalorienverbrauchs-Tracker")

# Datensatz für die Essensaufzeichnung
data = pd.DataFrame(columns=["Datum", "Essen", "Menge (g)"])
data_file = "food_records.csv"

# Eingabefelder für Essensaufzeichnung
st.subheader("Essen aufzeichnen")
today = datetime.date.today()
date = st.date_input("Datum:", today)
food = st.text_input("Art des Essens:")
amount = st.number_input("Menge (g):", min_value=1)

if st.button("Aufzeichnen"):
    data = data.append({"Datum": date, "Essen": food, "Menge (g)": amount}, ignore_index=True)
    data.to_csv(data_file, index=False)
    st.success("Essen erfolgreich aufgezeichnet!")

# Tabelle anzeigen
st.subheader("Aufgezeichnetes Essen")
if not data.empty:
    st.dataframe(data)

# Kalorienverbrauch-Rechner
st.subheader("Kalorienverbrauch-Rechner")
weight = st.number_input("Gewicht (kg):", min_value=1)
duration = st.number_input("Dauer (min):", min_value=1)
calories_burned = st.number_input("Verbrannte Kalorien:", min_value=0)

if st.button("Berechnen"):
    calories_burned = (weight * 3.5 * duration) / 200 + calories_burned
    st.success(f"Verbrannte Kalorien: {calories_burned:.2f} kcal")

# Streamlit App starten
if __name__ == "__main__":
    st.set_page_config(layout="wide")
