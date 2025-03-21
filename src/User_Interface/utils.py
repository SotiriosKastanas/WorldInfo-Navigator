import streamlit as st

def add_css1():
    st.markdown(
        """
        <style>
        div[data-testid="stToolbar"] {display: none;}
        
        /* Chat Container */
        .chat-container {
            max-width: 700px;
            margin: auto;
        }

        /* User Message */
        .user-message {
            background-color: #D3D3D3   ;
            color: black;
            padding: 10px 15px;
            border-radius: 18px;
            max-width: 80%;
            display: inline-block;
            text-align: left;
        }

        /* Assistant Message */
        .assistant-message {
            background-color: #f1f1f1;
            color: black;
            padding: 10px 15px;
            border-radius: 18px;
            max-width: 80%;
            display: inline-block;
            text-align: left;
        }

        /* Message Container */
        .message-container {
            display: flex;
            margin-bottom: 10px;
        }

        .message-user {
            justify-content: flex-end;
        }

        .message-assistant {
            justify-content: flex-start;
        }

        /* Message Timestamp */
        .message-timestamp {
            font-size: 12px;
            color: gray;
            margin-top: 5px;
        }
        </style>
        """, unsafe_allow_html=True
    )


def add_top_right_info(email):
    st.markdown(f"""
    <style>
    header[data-testid="stHeader"]::after {{
        content: "User: {email}";
        /* Line breaks for \\A */
        white-space: pre-line;
        
        position: absolute;
        right: 2rem;
        top: 10px;
        
        /* Styling */
        font-size: 14px;
        font-weight: bold;
        color: white;
        background: #2E3B4E;
        padding: 10px 15px;
        border-radius: 12px;
    }}
    </style>
    """, unsafe_allow_html=True)

def sidebar():
    with st.sidebar:
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"] {
                background-color: #2E3B4E; /* Dark Blue */
                color: white;
            }
            [data-testid="stSidebar"] * {
                color: white !important;  /* Ensures all text inside is white */
            }

            /* Styled Welcome Message */
            .welcome-text {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                color: #FFD700; /* Gold color */
                padding: 10px;
                border-radius: 10px;
                background: rgba(255, 255, 255, 0.1); /* Subtle transparent background */
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                margin-top: 10px;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
        
        # AI Robot Image
        st.markdown('<div class="welcome-text"> Welcome to the WorldInfo Navigator 🌎 </div>', unsafe_allow_html=True)
        st.markdown('---')
        st.image('../data/images_ui/sss.png', width=350)
        st.markdown('---')

def add_css():
    st.markdown(
        """
        <style>
        div[data-testid="stToolbar"] {display: none;}
        </style>
        """, unsafe_allow_html=True
    )
