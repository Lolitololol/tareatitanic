import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("database_titanic.csv")

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
# Mi primera aplicación interactiva
## Gráficos usando la base de datos del Titanic
""")

# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    st.write("# Opciones")
    
    # Bins no puede ser 0 → mínimo 1 para evitar error
    div = st.slider('Número de bins:', 1, 10, 2)
    
    st.write("Bins =", div)

# ================================
#          LAYOUT CON COLUMNAS
# ================================
col1, col2 = st.columns(2)

# --------- Gráfico 1: Histograma ----------
with col1:
    fig1, ax1 = plt.subplots()
    ax1.hist(df["Age"], bins=div)
    ax1.set_xlabel("Edad")
    ax1.set_ylabel("Frecuencia")
    ax1.set_title("Histograma de edades")
    st.pyplot(fig1)

# --------- Gráfico 2: Hombres vs Mujeres ----------
with col2:
    df_male = df[df["Sex"] == "male"]
    cant_male = len(df_male)

    df_female = df[df["Sex"] == "female"]
    cant_female = len(df_female)

    fig2, ax2 = plt.subplots()
    ax2.bar(["Masculino", "Femenino"], [cant_male, cant_female], color="red")
    ax2.set_xlabel("Sexo")
    ax2.set_ylabel("Cantidad")
    ax2.set_title("Distribución de hombres y mujeres")
    st.pyplot(fig2)

# ================================
#     grafico de sobrevivientes por sexo
#  Supervivientes por sexo
# ================================
st.write("## Supervivientes por sexo")

surv_male = df[df["Sex"]=="male"]["Survived"].sum()
surv_female = df[df["Sex"]=="female"]["Survived"].sum()

fig3, ax3 = plt.subplots()
ax3.bar(["Masculino", "Femenino"], [surv_male, surv_female], color=["blue", "pink"])
ax3.set_ylabel("Número de sobrevivientes")
ax3.set_title("Supervivientes por sexo")
st.pyplot(fig3)

# ================================
#   Tabla de datos cargados
# ================================
st.write("## Muestra de datos cargados")
st.table(df.head())
