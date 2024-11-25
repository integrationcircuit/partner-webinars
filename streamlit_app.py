import streamlit as st
import requests

def show_registration_form():
    session_1_date = "Platform Deep Dive (Dec 13, 9:30 AM CET)"
    session_2_date = "GenAI Solutions (Dec 20, 9:30 AM CET)"
    
    st.subheader("Webinar Registration")
    
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Full Name (*)", key="name", placeholder="Your preferred name")
        st.text_input("Email  (*)", key="email", placeholder="Your corporate email. Public domains (e.g. gmail, hotmail etc) will not receive an invite.")
        st.text_input("Company (*)", key="company", placeholder="Your company name.")
    with col2:
        st.multiselect(
            "Select Webinars to Attend (*)",
            options=[
                session_1_date,
                session_2_date
            ],
            key="webinar_selection"
        )
        st.selectbox(
            "Your Role (*)",
            options=[
                "Solution Architect",
                "Account Executive",
                "Developer",
                "Sales Engineer",
                "Technical Consultant",
                "Project Manager",
                "Other"
            ],
            key="role",
            placeholder="Select"
        )
    
    col3, col4 = st.columns(2)
    with col3:
        st.text_area("What topics are you most interested in?", key="interests", placeholder="Your topics of interest. Do not need to directly match the agenda.")
    with col4:
        st.text_area("Do you have any specific questions you'd like addressed?", key="questions", placeholder="Your questions you'd like us to address before/during the Q&A or in a separate follow-up.")

    if st.button("Register Now", type="primary"):
        selected_webinars = st.session_state.webinar_selection
        if not selected_webinars:
            st.error("Please select at least one webinar to attend.")
        elif not st.session_state.name or not st.session_state.email or not st.session_state.company:
            st.error("Name, Email and Company are required fields.")
        else:
            register_webinar_attendee()
            # st.success(f"Registration successful! You've registered for {', '.join(selected_webinars)}")
            # st.info("You will receive a confirmation email with calendar invites shortly.")

def register_webinar_attendee():
    try:
        request_params = {
            "name": st.session_state.name,
            "email": st.session_state.email,
            "company": st.session_state.company,
            "sessions": str(st.session_state.webinar_selection).replace("]","").replace("[","").replace("', ","|||").replace("'",""),
            "role": st.session_state.role,
            "interests": st.session_state.interests,
            "questions": st.session_state.questions
        }
        
        response = requests.get(
            url="https://emea.snaplogic.com/api/1/rest/slsched/feed/ConnectFasterInc/0_StanGPT/StanCoE/RegisterWebinarAttendees_Task",
            headers={
                "Authorization": "Bearer AuhKIZXdheJV9aJ5vzmFnJVCfkp5BWsJ"
            },
            params=request_params
        )
        
        if "200" in str(response.status_code):
            st.success("Registration successful! We look forward to welcoming you in the upcoming session(-s)!")
            st.info("You will receive a confirmation email with calendar invites as we get closer to the event date(-s).")
        else:
            st.error("There appears to have been an error. Please try again. If it continues, please message your Partner Account Manager.")
    except:
        st.error("There appears to have been an error. Please try again. If it continues, please message your Partner Account Manager.")
    
    print("done")

def main():
    st.set_page_config(
        page_title="SnapLogic Webinar Series",
        page_icon="🔄",
        layout="wide"
    )

    
    st.title("SnapLogic Partner Enablement Webinar Series")
    st.markdown("""
    Welcome to the SnapLogic Partner Enablement Webinar Series! These sessions are a recurring series tailored for customer-facing technical and sales roles and designed 
    to help you maximize your partnership with SnapLogic.
    """)
    st.markdown("""Running on a monthly basis, these sessions will act as both an initial overview for the early days of your journey as a SnapLogic partner, as well as a refresher series for more tenured relationships.
                """)


    # Main webinar tabs
    with st.container(border=True):
        platform_tab, genai_tab = st.columns([1, 1])
        with platform_tab:
            st.header("Session #1 - The Foundations")
            st.markdown("""
            **Date**: December 13, 2024  
            **Time**: 9:30 AM CET/8:30 AM UTC     
            **Duration**: 90 minutes
            """)

            # Agenda
            st.subheader("What we'll cover")
            agenda_items = {
                "10 mins1": "High Level Overview - SnapLogic Product Suite",
                "30 mins2": "Live Demonstrations - Application Integration & Data Integration Examples",
                "10 mins3": "API Management Overview",
                "10 mins4": "Competitive Positioning & Wrap-Up",
                "30 mins5": "Interactive Q&A Session"
            }

            for duration, topic in agenda_items.items():
                st.markdown(f"**{duration[:-1]}** - {topic}")
                
        with genai_tab:
            st.header("Session #2 - Generative Integration")
            st.markdown("""
            **Date**: December 20, 2024  
            **Time**: 9:30 AM CET/8:30 AM UTC     
            **Duration**: 90 minutes
            """)

            # Agenda
            st.subheader("What we'll cover")
            agenda_items = {
                "10 mins1": "SnapLogic GenAI Features Overview",
                "15 mins2": "SnapGPT & AgentCreator - What, How and Why",
                "25 mins3": "Use Case Catalog & Internal R&D Showcase",
                "10 mins4": "Future Plans & Wrap-Up",
                "30 mins5": "Interactive Q&A Session"
            }

            for duration, topic in agenda_items.items():
                st.markdown(f"**{duration[:-1]}** - {topic}")


    # Registration form at the top
    with st.expander("Registration", expanded=True):
        show_registration_form()
        
if __name__ == "__main__":
    main()