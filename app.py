import streamlit as st 
import tiktoken 

GPT_35_TURBO_PROMPT_COST = 0.0015 
GPT_35_TURBO_COMPLETIONS_COST = 0.002 
GPT4_PROMPT_COST = 0.03 
GPT4_COMPLETIONS_COST = 0.06

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    print(num_tokens)
    return num_tokens

def main():
    st.set_page_config(layout="wide")
    st.title("LLM Cost Calculations")
    
    prompt_text = st.text_area("Prompt Text", height=300)

    if len(prompt_text) > 0:
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.subheader("Basic Information")
            st.info("Your Input Prompt: " + prompt_text)
            token_counts = num_tokens_from_string(prompt_text, "cl100k_base")
            st.success("Token Count: " + str(token_counts))
        
        with col2:
            st.subheader("Execute a Simulation")
            option = st.selectbox('Select an LLM?', ('GPT-3.5-Turbo', 'GPT-4'))
            average_number_of_employees = st.slider("Average number of Employees", 0, 200, 0)
            average_prompt_frequency = st.slider("Average number of Prompt Frequency (Per Day)/Employee", 0, 300, 0)
            average_prompt_tokens = st.slider("Average Prompt Tokens Length", 0, 300, 0)
            average_completions_tokens = st.slider("Average Completions Tokens Length", 0, 1000, 0)

        with col3:
            st.subheader("Cost Analysis")
            if option == 'GPT-3.5-Turbo':
                cost_per_day = average_number_of_employees * average_prompt_frequency * average_prompt_tokens * GPT_35_TURBO_PROMPT_COST + average_number_of_employees * average_prompt_frequency * average_completions_tokens * GPT_35_TURBO_COMPLETIONS_COST
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + str(cost_per_day) + " $")
                st.success("Cost Per Month: " + str(cost_per_month) + " $")
                st.success("Cost Per Year: " + str(cost_per_year) + " $")

                st.write("This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk.")
            elif option == 'GPT-4':
                cost_per_day = average_number_of_employees * average_prompt_frequency * average_prompt_tokens * GPT4_PROMPT_COST + average_number_of_employees * average_prompt_frequency * average_completions_tokens * GPT4_COMPLETIONS_COST
                cost_per_month = cost_per_day * 30
                cost_per_year = cost_per_month * 12
                st.success("Cost Per Day: " + str(cost_per_day) + " $")
                st.success("Cost Per Month: " + str(cost_per_month) + " $")
                st.success("Cost Per Year: " + str(cost_per_year) + " $")
                st.write("This calculation is based on the assumptions. This app don't take any responsibility for the accuracy of the calculation. Please use this app at your own risk.")
            else:
                st.error("Please select an LLM")


if __name__ == "__main__":
    main()
