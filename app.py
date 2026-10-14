import streamlit as st

st.set_page_config(
    page_title="Udyam Access AI",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Udyam Access AI")
st.subheader("AI-Assisted Financing Discovery for MSMEs")

st.write(
    "A prototype to help small businesses explore "
    "potential financing opportunities."
)

st.divider()

st.header("Dashboard Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Target Users", "MSMEs")
col2.metric("Purpose", "Financing Discovery")
col3.metric("Mode", "Demo")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a page",
    ["Home", "Business Profile", "Financing Explorer"]
)

if page == "Home":
    st.header("Welcome!")
    st.write(
        "Explore potential financing options based on "
        "your business profile and financing needs."
    )
    st.info("Select Business Profile from the sidebar to begin.")

elif page == "Business Profile":
    st.header("Business Profile")
    st.caption("Sample business for demonstration only.")

    business_name = st.text_input(
        "Business Name",
        value="ABC Manufacturing Unit"
    )

    business_type = st.selectbox(
        "Business Type",
        ["Manufacturing", "Services", "Trading"]
    )

    turnover = st.number_input(
        "Annual Turnover (₹ lakh)",
        min_value=0.0,
        value=25.0,
        step=1.0
    )

    purpose = st.selectbox(
        "Financing Purpose",
        [
            "Purchase machinery",
            "Working capital",
            "Business expansion"
        ]
    )

    if st.button("Save Demo Profile"):
        st.session_state["business"] = business_name
        st.session_state["business_type"] = business_type
        st.session_state["turnover"] = turnover
        st.session_state["purpose"] = purpose
        st.success("Demo business profile saved!")

    if "business" in st.session_state:
        st.subheader("Saved Business Details")
        st.write("Business:", st.session_state["business"])
        st.write("Type:", st.session_state["business_type"])
        st.write(
            "Annual Turnover:",
            f"₹{st.session_state['turnover']:,.2f} lakh"
        )
        st.write("Purpose:", st.session_state["purpose"])

elif page == "Financing Explorer":
    st.header("Financing Explorer")

    st.write("Explore potential financing routes for your business.")

    st.warning(
        "These are illustrative options, not confirmed scheme "
        "matches or loan eligibility decisions."
    )

    st.subheader("Potential Options")

    st.markdown("""
    **1. MSME Business Financing**

    Explore financing for business operations and expansion.

    **2. Machinery Financing**

    Investigate financing options for equipment purchases.

    **3. Credit Guarantee Support**

    Check whether an applicable credit guarantee scheme is available.

    **4. Government MSME Schemes**

    Review current official scheme guidelines and eligibility.
    """)

    st.caption(
        "Verify current conditions with the relevant official "
        "scheme provider or lending institution."
    )
  
