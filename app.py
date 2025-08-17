
import streamlit as st
from classifier import process_symptom
# st.set_page_config(page_title="AI Hospital Symptom Classifier")
st.set_page_config(
    page_title="AI Hospital Symptom Classifier",
    page_icon="favicon.png",  # Use the emoji 🏥 or a local PNG file
)
st.title("AI Hospital Symptom Classifier")

symptom = st.text_input("Describe your symptom (e.g., 'fever', 'headache', 'anxiety'):")

if symptom:
    with st.spinner('Analyzing your symptom...'):
        final_state = process_symptom(symptom)
    answer = final_state.get("answer", "")
    
    # Display color-coded messages based on category keywords in answer
    if "emergency" in answer.lower():
        st.error(answer)
        if st.button("Call Emergency Help"):
            st.write("🚑 Connecting you to Emergency Services...")
    elif "mental health" in answer.lower() or "counselor" in answer.lower():
        st.info(answer)
        if st.button("Contact Counselor"):
            st.write("📞 Connecting you to a Counselor...")
    else:
        st.success(answer)
        if st.button("Contact Nurse"):
            st.write("🩺 Connecting you to Nursing Staff...")
else:
    st.info("Please enter your symptom above to get started.")
