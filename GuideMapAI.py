import streamlit as st
import google.generativeai as genai

st.title("🧭 Travel Route Finder")

# Input fields
start = st.text_input("📍 Starting location")
end = st.text_input("🎯 Destination location")

# Configure API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# Button
if st.button("🚀 Find Route"):
    if start and end:
        prompt = f"""
        Find a travel route from {start} to {end}.
        Include:
        - 🚗 Best road route
        - 📏 Approx distance & travel time
        - 🚌 Nearest bus options (if available)
        - 🚆 Nearest train options (if available)
        - 🚇 Nearest metro options (if available)
        - ⚡ Best route for time, energy & efficiency
        Keep it short, simple and human-friendly.
        """
        
        response = model.generate_content(prompt)
        st.subheader("✨ Suggested Route")
        st.write(response.text)

    else:
        st.warning("⚠️ Please enter both locations.")
