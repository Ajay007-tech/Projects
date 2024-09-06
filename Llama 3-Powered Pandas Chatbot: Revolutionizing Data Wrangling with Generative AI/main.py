
import streamlit as st
import pandas as pd
import json
from groq import Groq

# Initialize Groq client with your API key
client = Groq(api_key="groq_api_key")

# Function to send data to Llama 3 and get the response
def ask_llama_3(user_question, dataset_as_string):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"Here are the first 10 rows of the dataset: {dataset_as_string}"},
            {"role": "user", "content": f"{user_question}"},
            {"role": "system","content":"Don't use df_sample to show output use entire data to show oupput use df variable directly where it contain entire data "}
        ],
        model="llama-3.1-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title("Llama 3 CSV Data Query System")
st.write("Upload a CSV file, and ask a question about the data. Only the first 10 rows will be used.")

# Step 1: File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Step 2: Load dataset and take only the first 10 rows
    df = pd.read_csv(uploaded_file)
    df_sample = df.head(10)
    
    st.write("First 10 rows of your dataset:")
    st.dataframe(df_sample)
    
    # Step 3: Convert the first 10 rows to a JSON-like string
    dataset_as_string = df_sample.to_json(orient='records')
    
    # Show the dataset as a JSON-like string (truncated for display purposes)
    st.write("First 10 rows in JSON format (truncated for display):")
    st.text(dataset_as_string[:1000] + "...")  # Only showing the first 1000 characters

    # Step 4: User inputs their question
    user_question = st.text_input("Ask a question about your dataset (e.g., 'Show employees in the HR department')")

    if user_question:
        st.write("Processing your question...")

        # Step 5: Ask Llama 3 using the dataset and user question
        response = ask_llama_3(user_question, dataset_as_string)

        # Step 6: Display Llama 3's response
        st.write("Answer from Llama 3:")
        st.write(response)

        # Step 7: Ask the user if they want the Pandas query
        show_query = st.checkbox("Do you want to see the Pandas query?")
        if show_query:
            st.code(response)  # Assuming the response contains the Pandas query
