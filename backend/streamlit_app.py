import streamlit as st

from idea_agent import generate_startup_idea
from market_agent import market_research
from business_agent import business_plan
from finance_agent import finance_analysis
from marketing_agent import marketing_strategy
from mentor_agent import mentor_advice
from legal_agent import legal_guide

st.set_page_config(page_title="LaunchMate AI", layout="wide")

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