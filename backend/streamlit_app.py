import streamlit as st

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

from idea_agent import generate_startup_idea
from market_agent import market_research
from business_agent import business_plan
from finance_agent import finance_analysis
from marketing_agent import marketing_strategy
from mentor_agent import mentor_advice
from legal_agent import legal_guide

st.set_page_config(page_title="LaunchMate AI", layout="wide")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    choice = st.sidebar.selectbox(
        "Select",
        ["Login", "Signup"]
    )

    st.title(choice)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if choice == "Signup":

        if st.button("Create Account"):

            if username in st.session_state.users:
                st.error("Username already exists")
            else:
                st.session_state.users[username] = password
                st.success("Signup Successful")

    elif choice == "Login":

        if st.button("Login"):

            if (
                username in st.session_state.users
                and st.session_state.users[username] == password
            ):
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Username or Password")

    st.stop()
   
if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.title("🚀 LaunchMate AI")
st.subheader("Your Intelligent Startup Co-Founder")


startup_idea = st.text_input("Enter Your Startup Idea")

if st.button("Generate Complete Report"):

    if not startup_idea:
        st.warning("Please enter a startup idea")
    else:

        with st.spinner("Generating..."):

            idea = generate_startup_idea(startup_idea)
            market = market_research(startup_idea)
            business = business_plan(startup_idea)
            finance = finance_analysis(startup_idea)
            marketing = marketing_strategy(startup_idea)
            mentor = mentor_advice(startup_idea)
            legal = legal_guide(startup_idea)

        st.header("💡 Startup Idea")
        st.write(idea)

        st.header("📊 Market Research")
        st.write(market)

        st.header("💼 Business Plan")
        st.write(business)

        st.header("💰 Finance Analysis")
        st.write(finance)

        st.header("📢 Marketing Strategy")
        st.write(marketing)

        st.header("🧠 Mentor Advice")
        st.write(mentor)

        st.header("⚖️ Legal Guide")
        st.write(legal)