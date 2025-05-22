import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simple Batch Reactor Simulator")

# Inputs
C0 = st.number_input("Initial Concentration (mol/L)", value=100.0)
k = st.number_input("Rate Constant k (1/hr)", value=0.3)
t_final = st.number_input("Total Time (hr)", value=10.0)

# Time points
t = np.linspace(0, t_final, 100)
C = C0 * np.exp(-k * t)  # First-order reaction: C = C0 * e^(-kt)

# Plot
st.subheader("Concentration vs Time")
fig, ax = plt.subplots()
ax.plot(t, C, label="C(t)")
ax.set_xlabel("Time (hr)")
ax.set_ylabel("Concentration (mol/L)")
ax.grid(True)
ax.legend()
st.pyplot(fig)
