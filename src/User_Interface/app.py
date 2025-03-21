import streamlit as st
import sys
import datetime


sys.path.append("../src")
from agents.agents import agents
from agents.setup import llm_configuration
from User_Interface.utils import sidebar, add_top_right_info, add_css

##### INITIALIZE #####
st.session_state['user_avatar'] = '../data/images_ui/user_avatar.png'
st.session_state['assistant_avatar'] = '../data/images_ui/assistant_avatar.png'
st.set_page_config(page_title = 'WorldInfo Navigator 🌎', page_icon= '../data/images_ui/sss.png')

llm_config = llm_configuration()
user_proxy, orchestrator_agent, times_agent, weather_agent, countries_info_agent, manager = agents(llm_config)

if 'is_input_disabled' not in st.session_state:
    st.session_state.is_input_disabled = False
######################
def interface():
    st.title('WorldInfo Navigator 🌎')

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    for entry in st.session_state.chat_history:
        if entry['role'] == 'user':
            with st.chat_message('user', avatar=st.session_state['user_avatar']):
                st.markdown(entry['content'])
                st.caption(f"{entry['timestamp']}")
        elif entry['role'] == 'assistant':
            with st.chat_message('assistant', avatar = st.session_state['assistant_avatar']):
                st.markdown(entry['content'])
                st.caption(f"{entry['timestamp']}") 
    user_input = st.chat_input("Type your message here...", disabled=st.session_state.is_input_disabled)

    if (user_input):
        st.session_state.is_input_disabled = True
        question_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state['user_input'] = user_input
        st.session_state['question_timestamp'] = question_timestamp
        st.session_state.chat_history.append({"role": "user", "content": user_input, 'timestamp': question_timestamp})
        st.rerun()


def manage_response(user_input, response, question_timestamp, answer_timestamp):
    response = response.replace('\n', ' ')
    del st.session_state['user_input']
    st.session_state.is_input_disabled = False
    st.rerun()

def get_response(message):
    response = user_proxy.initiate_chat(manager, message=message)
    if response.chat_history[-1]['content'] == 'TERMINATE':
        answer = response.chat_history[-2]['content']
    else:
        answer = response.chat_history[-1]['content']
    answer = answer.replace("TERMINATE", "")
    return answer

def user_message(user_input):
    if 'user_input' in st.session_state:

        question_timestamp = st.session_state.question_timestamp
        try:
            with st.spinner('loading...'):
                response = get_response(user_input)
                answer_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.chat_history.append({"role": "assistant", "content": response, 'timestamp': answer_timestamp})
                manage_response(user_input, response, question_timestamp, answer_timestamp)
        except Exception:
            error_message = (
                "An error occured"
            )
            with st.chat_message('assistant'):
                st.markdown(error_message)
            st.session_state.chat_history.append({'role': 'assistant', 'content': error_message})
            manage_response(user_input, error_message, question_timestamp, answer_timestamp)
            del st.session_state['user_input']

def main(email):
    add_css() 
    if "chat_history" not in st.session_state or not st.session_state.chat_history:
        pass

    interface()

    if 'user_input' in st.session_state:
        user_message(st.session_state['user_input'])


if __name__ == '__main__':
    if "email_entered" not in st.session_state:
        st.session_state["email_entered"] = False
    if not st.session_state.email_entered:
        email = st.text_input("Enter your email address")
        if email:
            st.session_state.email = email
            st.session_state.email_entered = True
            st.rerun()
    else:
        email = st.session_state.email
        add_css()
        add_top_right_info(email)
        sidebar()
        main(email)
