{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4c55f6b-008e-4922-91b3-97b3018f2439",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import google.generativeai as genai\n",
    "\n",
    "st.title(\"🧭 Travel Route Finder\")\n",
    "\n",
    "# Input fields\n",
    "start = st.text_input(\"📍 Starting location\")\n",
    "end = st.text_input(\"🎯 Destination location\")\n",
    "\n",
    "# Configure API key\n",
    "genai.configure(api_key=st.secrets[\"GOOGLE_API_KEY\"])\n",
    "\n",
    "model = genai.GenerativeModel(\"gemini-2.5-flash\")\n",
    "\n",
    "# Button\n",
    "if st.button(\"🚀 Find Route\"):\n",
    "    if start and end:\n",
    "        prompt = f\"\"\"\n",
    "        Find a travel route from {start} to {end}.\n",
    "        Include:\n",
    "        - 🚗 Best road route\n",
    "        - 📏 Approx distance & travel time\n",
    "        - 🚌 Nearest bus options (if available)\n",
    "        - 🚆 Nearest train options (if available)\n",
    "        - 🚇 Nearest metro options (if available)\n",
    "        - ⚡ Best route for time, energy & efficiency\n",
    "        Keep it short, simple and human-friendly.\n",
    "        \"\"\"\n",
    "        \n",
    "        response = model.generate_content(prompt)\n",
    "        st.subheader(\"✨ Suggested Route\")\n",
    "        st.write(response.text)\n",
    "\n",
    "    else:\n",
    "        st.warning(\"⚠️ Please enter both locations.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
