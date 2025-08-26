import streamlit as st

# ==========================
# Mock User Database
# ==========================
USER_CREDENTIALS = {
    "admin": "password123",
    "onasi": "upstream2025"
}


# ==========================
# Login Page
# ==========================
def login():
    st.title(" Login to Upstream Live")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login successful ✅")
            st.rerun()
        else:
            st.error("Invalid username or password ")


# ==========================
# Dashboard Content
# ==========================
def dashboard_content():
    # Example metrics
    st.metric("Total Wells", 120)
    st.metric("Active Rigs", 18)
    st.metric("Production Rate", "85,000 bbl/day")

    # Example chart
    import pandas as pd
    import numpy as np
    import altair as alt

    data = pd.DataFrame({
        "Day": pd.date_range("2025-01-01", periods=10),
        "Production": np.random.randint(70, 100, size=10)
    })

    chart = alt.Chart(data).mark_line(point=True).encode(
        x="Day",
        y="Production"
    ).properties(title="Daily Production Trend")

    st.altair_chart(chart, use_container_width=True)


# ==========================
# Dashboard Page
# ==========================
def dashboard():
    # Sidebar with settings
    st.sidebar.title("️ Settings")
    settings_option = st.sidebar.selectbox("Choose Action", ["Profile", "Preferences", "Logout"])

    if settings_option == "Logout":
        st.session_state["logged_in"] = False
        st.rerun()

    st.title(" Upstream Live Dashboard")
    st.subheader(f"Welcome Back, {st.session_state['username'].capitalize()} 👋")

    # Search bar
    search_query = st.text_input(" Search Data")
    if search_query:
        st.info(f"Showing results for: **{search_query}**")
        # Here you can add filtering logic based on the search input

    # Show main dashboard content
    dashboard_content()


# ==========================
# Main App Logic
# ==========================
def main():
    st.set_page_config(page_title="Upstream Live", layout="wide")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        dashboard()
    else:
        login()


if __name__ == "__main__":
    main()
