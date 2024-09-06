
# RAG-Powered Data Query System with Llama 3 and Streamlit

This project is a **Retrieval-Augmented Generation (RAG)**-based system where users can upload datasets (CSV format) and ask questions about the data. The system will analyze the data, generate answers, and even provide corresponding Pandas queries upon request. The system utilizes the **Llama 3 70B Versatile model** for answering questions with data context, and it is deployed via **Streamlit** for easy user interaction.

## Key Features:
- Upload CSV files for real-time data analysis.
- Answer questions based on the uploaded dataset using **Llama 3**.
- Utilize **Retrieval-Augmented Generation (RAG)** to provide context from the dataset for accurate responses.
- Provide Pandas code snippets for data queries upon user request.
- Simple web interface using **Streamlit**.

## Technologies Used:
- **Groq API**: For Llama 3 70B Versatile model integration.
- **Llama 3**: For natural language query processing and generative AI.
- **RAG (Retrieval-Augmented Generation)**: For using dataset context to provide accurate, data-driven responses.
- **Streamlit**: For web-based user interaction.
- **Pandas**: For dataset processing and manipulation.

## How It Works:

1. **Data Upload**: Users can upload a CSV file (e.g., employee data) via the Streamlit interface.
2. **Context Generation**: The uploaded dataset is converted into a JSON-like text string to serve as context for the Llama 3 model.
3. **Ask Questions**: Users ask questions in natural language (e.g., "Show me employees in the HR department").
4. **RAG-Based Response**: Llama 3 uses the context from the dataset to provide an answer to the user’s query.
5. **Pandas Query Generation**: Optionally, users can request the equivalent Pandas query for the question.

## Installation

### Requirements
- Python 3.8+
- Groq API Key (for accessing Llama 3)
- Streamlit
- Pandas

### Install Dependencies

```bash
pip install streamlit pandas groq
```

### Set Up Groq API Key

1. Get your **Groq API Key** from [Groq](https://groq.com) and replace `"your_groq_api_key"` in the code with your actual API key.
   
2. Ensure your key has access to the **Llama 3 70B Versatile model**.

### Running the Project

1. Clone the repository or download the files.
2. Place your CSV dataset in the same directory (or upload it through Streamlit during runtime).
3. Run the application:

```bash
streamlit run main.py
```

4. Open the provided localhost URL in your browser.

## Usage

1. **Upload your dataset**: Click on the "Upload CSV file" button to upload your CSV file.
2. **Ask your question**: Type a question in natural language, for example, "Show employees working in the HR department".
3. **Get the answer**: Llama 3 processes your query and provides an answer based on the data.
4. **Get Pandas Query**: If needed, request the equivalent Pandas query to reproduce the result in code.

## Example Scenario

1. **Dataset**: An employee dataset with columns like `employee_name`, `department`, `salary`.
   
2. **User Query**: "Show employees who work in the HR department."

3. **Answer**: The system displays the names of employees working in HR and optionally provides the Pandas code:

    ```python
    df[df["department"] == "HR"]["employee_name"]
    ```

## Future Improvements

- **More Advanced Retrieval**: Implement advanced retrieval techniques for more complex queries.
- **Larger Datasets**: Optimize the system to handle larger datasets efficiently.
- **Caching & Async Processing**: For improved performance with repeated queries.

## License

This project is open-source and free to use under the MIT License.

---

