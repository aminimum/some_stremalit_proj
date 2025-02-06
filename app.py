import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# st.title("Visualization")

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)

# st.pyplot(fig)


option = st.sidebar.selectbox(
    "Choose partition",
    ("Home", "Analyze", "Settings")
)

if option == "Home":
    st.title("Home")
elif option == "Analyze":
    st.title("Analyze")
else:
    st.title("Settings")
