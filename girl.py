import streamlit as st 

# APP Branding
st.set_page_config(page_title="Rajasekhar-Understanding Mindset",page_icon="❤️🧠❤️")
st.title("Rajasekhar:Understanding a Girl's Mindset") 
st.write("Welcom! Here to help you understand emotional sets.")

# Interactive Quiz section
st.header("Communication style Quiz")
scenario =st.radio("If she says Im fine but looks upset,True is ?",["She's actually fine","Need more space","Need to talk","Tired"])

if st.button("Check perspective"):
    if scenario == "Need to talk": 
        st.success("Correct! Often,'I'm fine'is a prompt for deeper listening.")
    else:
        st.info("Actually, it often means she is waiting for you to show you care.")
st.sidebar.header("Emotional compass")
# Use the custom CSS class for the emoji container
st.markdown('<div class="rotating-emoji">😊😢🤔💖</div>', unsafe_allow_html=True)
st.write("**Rajsekhar's Tips & Tools**")
    
st.subheader("Navigation")
st.radio("Go To", ["Home", "Quizzes", "Articles", "Community"])

st.subheader("App Status")
    # Example of dynamic sidebar content
status_placeholder = st.empty()
status_placeholder.info("App running smoothly...")

        
st.subheader("Rajasekhar's Top 3  Tips")
st.markdown("""
1. **Active Listening:** Don't just wait to talk; listen to understand her emotions.
2. **Validate Feelings:** Even if you don't agree, acknowledge that her feelings are real to her.
3. **Ask, Don't Assume:** If you aren't sure what she thinks, ask open-ended questions.
""")

 # --- Custom CSS for Rotation Animation ---
# We inject CSS directly into the app using st.markdown with unsafe_allow_html=True
st.markdown("""
<style>
/* Define the animation */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Apply the animation to a specific class */
.rotating-emoji {
    display: inline-block;
    animation: spin 4s linear infinite; /* 4 seconds duration, linear timing, infinite loop */
    font-size: 50px; /* Adjust size as needed */
}
</style>
""", unsafe_allow_html=True)
         