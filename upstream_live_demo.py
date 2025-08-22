import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px


st.set_page_config(page_title="Upstream Live Demo", layout="wide")

st.title(" Upstream Live – Real-Time Petroleum Monitoring")
st.markdown("### Nigeria's Petroleum Data, Live & Secure (Demo Version)")


if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Production", "Pressure", "GasFlaring"])


def generate_data():
    current_time = pd.Timestamp.now().strftime("%H:%M:%S")
    production = np.random.randint(8000, 12000)  # barrels/day
    pressure = np.random.randint(600, 1200)      # psi
    flaring = np.random.randint(20, 100)         # mscfd
    return {"Time": current_time, "Production": production, "Pressure": pressure, "GasFlaring": flaring}


placeholder = st.empty()

for _ in range(30):
    new_row = generate_data()
    st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)

    with placeholder.container():
        col1, col2, col3 = st.columns(3)


        col1.metric("Production (bbl/day)", new_row["Production"])
        col2.metric("Pipeline Pressure (psi)", new_row["Pressure"])
        col3.metric("Gas Flaring (mscfd)", new_row["GasFlaring"])


        if new_row["Production"] < 9000:
            st.error("️ Low Production Alert!")
        if new_row["Pressure"] > 1000:
            st.warning("️ High Pipeline Pressure!")
        if new_row["GasFlaring"] > 80:
            st.info("️ High Gas Flaring Detected!")


        fig1 = px.line(st.session_state.data, x="Time", y="Production", title="Production Over Time")
        fig2 = px.line(st.session_state.data, x="Time", y="Pressure", title="Pipeline Pressure Over Time")
        fig3 = px.line(st.session_state.data, x="Time", y="GasFlaring", title="Gas Flaring Over Time")

        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig3, use_container_width=True)

    time.sleep(1)
