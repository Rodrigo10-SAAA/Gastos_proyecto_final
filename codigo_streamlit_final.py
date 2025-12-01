import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # PREDICCION - COSTO DE ACTIVIDAD ''')
st.image(
    "gastos.jpg",
    caption="RODRIGO SÁNCHEZ ACOSTA - A1615173 : Esta app esta diseñada para calcular el costo de una actividad en base al registro de datos que he llevado a lo largo del semestre ago- dic 2025."
)

st.header('ASPECTOS A CONSIDERAR')

def user_input_features():
    # Entrada
    presupuesto = st.number_input(
        "Presupuesto asignado (en $):",
        min_value=0.0,
        max_value=5000.0,
        value=100.0,
        step=10.0
    )
    tiempo_invertido = st.number_input(
        "Tiempo invertido (en minutos):",
        min_value=0,
        max_value=600,
        value=30,
        step=5
    )
    actividad = st.number_input(
        "Tipo de actividad (0= Alimento, 1=Salud, 2=Academico, 3=Transporte, 4=Entretenimiento, 6= Ahorro:",
        min_value=0,
        max_value=6,
        value=0,
        step=1
    )
    momento = st.number_input(
        "Momento (0 = mañana, 1 = tarde, 2 = noche):",
        min_value=0,
        max_value=2,
        value=1,
        step=1
    )

    user_input_data = {
        "presupuesto": presupuesto,
        "tiempo_invertido": tiempo_invertido,
        "actividad": actividad,
        "momento": momento,
    }

    features = pd.DataFrame(user_input_data, index=[0])
    return features

df = user_input_features()

datos = pd.read_csv('datosv', encoding='latin-1')
X = datos[["prespuesto", "tiempo_invertido", "actividad", "momento"]]
y = datos["costo"]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=1615173
)
LR = LinearRegression()
LR.fit(X_train, y_train)

b1 = LR.coef_
b0 = LR.intercept_

prediccion = (
    b0
    + b1[0] * df['presupuesto']
    + b1[1] * df['tiempo_invertido']
    + b1[2] * df['actividad']
    + b1[3] * df['momento']
)

st.subheader("CALCULO DE COSTO")
st.write('LA PREDICCION DEL COSTO DE LA ACTIVIDAD ES DE :', prediccion)
