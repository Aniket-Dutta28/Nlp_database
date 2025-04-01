import streamlit as st
import pandas as pd
import sqlite3
import google.generativeai as genai
import os 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#funtion to load google genai model and provide sql query as responce 

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([prompt[0],question])
    return response.text

## funtion to retrive query from the sql database 

def get_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

## define the prompt
prompt = ["""
    yor are an expert converting Englsih language to sql query 
    The SQL database has a table called Student with the following columns:
    - id: integer
    - name: text
    - age: integer
    - marks: integer
    example:
    **Question:** "What is the average marks of the students?"  
   **SQL Query:** "SELECT AVG(marks) FROM Student;"  

    **Question:** "How many students are in the database?"  
    **SQL Query:** "SELECT COUNT(*) FROM Student;"  

    **Question:** "What are the names of students in the Science stream?"  
    **SQL Query:** "SELECT name FROM Student WHERE stream = 'Science';"  

    **Question:** "List all students in class 12 sorted by marks in descending order."  
    **SQL Query:** "SELECT * FROM Student WHERE class = 12 ORDER BY marks DESC;"  

    **Question:** "Who is the topper (student with the highest marks)?"  
    **SQL Query:** "SELECT name FROM Student WHERE marks = (SELECT MAX(marks) FROM Student);"  

    **Question:** "How many students are in each stream?"  
    **SQL Query:** "SELECT stream, COUNT(*) FROM Student GROUP BY stream;"  

    **Question:** "What is the average marks in the Commerce stream?"  
    **SQL Query:** "SELECT AVG(marks) FROM Student WHERE stream = 'Commerce';" 
    also the sql code should not have ```sql or ``` in the beginning and end of the query and sql word in the out put     

"""

]


## create a streamlit app

# Configure page settings
st.set_page_config(
    page_title="SQL Query Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content([prompt[0], question])
        return response.text
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

# Function to execute SQL query
def get_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"SQL Error: {str(e)}")
        return None

# Define the prompt
prompt = ["""
You are an expert in converting English questions to SQL queries.
The database has a Student table with these columns:
- student_id (INTEGER PRIMARY KEY)
- name (TEXT)
- class (INTEGER)
- stream (TEXT)
- marks (FLOAT)

Convert the following question to a SQL query.
Return only the SQL query without any explanations or formatting.

Examples:
Question: "Show students in Science stream"
SELECT * FROM Student WHERE stream = 'Science';

Question: "Average marks by stream"
SELECT stream, AVG(marks) as average_marks FROM Student GROUP BY stream;
"""]

def main():
    # Sidebar
    with st.sidebar:
        st.image("https://www.svgrepo.com/show/374160/sql.svg", width=100)
        st.title("Query Guide")
        
        st.markdown("### Example Questions")
        examples = [
            "Show all students in Science stream",
            "What is the average marks by stream?",
            "Who are the top 10 students?",
            "Show students with marks above 90",
            "How many students are in each class?"
        ]
        for ex in examples:
            st.markdown(f"- {ex}")
        
        st.markdown("### Table Schema")
        st.code("""
        Student Table:
        - student_id (INTEGER PRIMARY KEY)
        - name (TEXT)
        - class (INTEGER)
        - stream (TEXT)
        - marks (FLOAT)
        """)

    # Main content
    st.title("🤖 SQL Query Assistant")
    st.markdown("### Convert English to SQL Query")
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        question = st.text_area(
            "Enter your question in plain English:",
            height=100,
            placeholder="Example: Show me all students in Science stream with marks above 90"
        )
        
        submit = st.button("🔍 Generate Query")

    if submit and question:
        with st.spinner("Generating SQL query..."):
            response = get_gemini_response(question, prompt)
            
            if response:
                st.markdown("### Generated SQL Query")
                st.code(response, language='sql')
                
                with st.spinner("Executing query..."):
                    data = get_sql_query(response, "student.db")
                    
                    if isinstance(data, pd.DataFrame):
                        st.markdown("### Query Results")
                        
                        # Show record count
                        st.markdown(f"*Found {len(data)} records*")
                        
                        # Display the dataframe with styling
                        st.dataframe(
                            data,
                            use_container_width=True,
                            hide_index=True
                        )
                        
                        # Add statistics if there are numeric columns
                        numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
                        if not data.empty and len(numeric_cols) > 0:
                            st.markdown("### Statistics")
                            st.dataframe(
                                data[numeric_cols].describe(),
                                use_container_width=True
                            )
                        
                        # Download button
                        csv = data.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Results",
                            data=csv,
                            file_name="query_results.csv",
                            mime="text/csv"
                        )

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Built with ❤️ using Streamlit and Google Gemini AI</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()