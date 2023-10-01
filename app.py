import streamlit as st 
import tiktoken

GPT_35_TURBO_PROMPT_COST = 0.0015
GPT_35_TURBO_COMPLETIONS_COST = 0.002
GPT4_PROMPT_COST = 0.03
GPT4_COMPLETIONS_COST = 0.06

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    print(num_tokens)
    return num_tokens

def main():
    st.set_page_config(layout="wide")

    st.title("LLM Cost Calculations")
    
    choice = st.sidebar.selectbox("Choose the approach", ["Taker", "Shaper"])
    
    if choice == "Taker":

        prompt_text = st.text_area("Enter your Prompts...")

        if prompt_text is not None:
            col1, col2, col3 = st.columns([1,1,1])
            
            with col1:
                if len(prompt_text) > 0:
                    st.info("Your Input Prompt Sample: " + prompt_text)
                token_counts = num_tokens_from_string(prompt_text, "cl100k_base")
                st.info("Total Token Count: "+ str(token_counts))
                
            with col2:
                st.warning("Execute a Scenario for Cost")
                option = st.selectbox('Select the LLM?',('GPT-3.5-Turbo', 'GPT-4'))
                average_number_of_employees = st.slider("Average Number of Employees", 0, 200, 0)
                average_prompt_frequency = st.slider('Average Prompt Frequency (Per Day)/Employee', 0, 300, 0)
                average_prompt_tokens = st.slider('Average Prompt Tokens Length', 0, 300, 0)
                average_completions_tokens = st.slider('Average Completions Tokens Length', 0, 1000, 0)
            
            with col3:
                st.success("Total Cost Calculations")
                if option == "GPT-3.5-Turbo":
                    PROMPT_COST = GPT_35_TURBO_PROMPT_COST
                    COMPLETIONS_COST = GPT_35_TURBO_COMPLETIONS_COST
                elif option == "GPT-4":
                    PROMPT_COST = GPT4_PROMPT_COST
                    COMPLETIONS_COST = GPT4_COMPLETIONS_COST
                    
                prompt_token_cost_per_day = (average_number_of_employees*average_prompt_frequency)*average_prompt_tokens*PROMPT_COST
                completion_cost_per_day = (average_number_of_employees*average_prompt_frequency)*average_completions_tokens*COMPLETIONS_COST 
                total_cost_per_day = prompt_token_cost_per_day + completion_cost_per_day
                monthly_cost_per_day = total_cost_per_day*30
    
                st.write("Total Prompt Cost Per Day", prompt_token_cost_per_day, "$")  
                st.write("Total Completions Cost Per Day", completion_cost_per_day, "$")
                st.subheader(f"Total Cost Per Day: ${total_cost_per_day:.2f}")
                st.subheader(f"Total Cost Per Month: ${monthly_cost_per_day:.2f}")
                
                
    elif choice == "Shaper":
        st.subheader("Coming Soon...")
        
        
        

            
if __name__ == "__main__":
    main()
