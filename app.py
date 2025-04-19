# app.py
import streamlit as st

st.set_page_config(page_title="MU/TH/UR 6000", layout="centered")

st.markdown("""
# 👁 MU/TH/UR 6000 Interface  
*Weyland-Yutani Corporation — Synthetic Intelligence Terminal*
""")

# Styled access input
st.markdown("### ENTER CLEARANCE CODE:")
access_code = st.text_input(" ", placeholder="██████████", type="password")

# Define codes
PLAYER_CODE = "SCIENTIST-LEVEL-3"
GM_CODE = "MUTHUR-ACCESS-PRIME"

# Session state for role
if "role" not in st.session_state:
    st.session_state.role = None

# Role assignment
if access_code == PLAYER_CODE:
    st.session_state.role = "player"
elif access_code == GM_CODE:
    st.session_state.role = "gm"

# Show the appropriate interface
if st.session_state.role == "player":
    st.success("Access Granted: SCIENTIST LEVEL 3")
    st.markdown("**QUERY MU/TH/UR:**")
    query = st.text_input("Your question:")
    if query:
        st.session_state["latest_query"] = query
        st.info("Query transmitted to MU/TH/UR... Await response.")
elif st.session_state.role == "gm":
    st.success("Access Granted: MU/TH/UR SYSTEM ADMINISTRATOR")
    st.markdown("**INCOMING PLAYER QUERY:**")
    query = st.session_state.get("latest_query", None)
    if query:
        st.code(query)
        response = st.text_area("MU/TH/UR Response:")
        if st.button("Transmit Response"):
            st.session_state["latest_response"] = response
            st.success("Response transmitted.")
    else:
        st.info("Awaiting incoming query...")
elif access_code and not st.session_state.role:
    st.error("ACCESS DENIED. INVALID CLEARANCE CODE.")

