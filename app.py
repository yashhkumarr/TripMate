import streamlit as st
import os
from dotenv import load_dotenv
from portia import (
    Config,
    DefaultToolRegistry,
    LLMProvider,
    LogLevel,
    Portia,
    StorageClass,
    PlanRunState,
)
from portia.cli import CLIExecutionHooks
from portia.open_source_tools.browser_tool import BrowserTool, BrowserInfrastructureOption
from portia import open_source_tool_registry
import logging

# Load environment variables from a .env file at the start
load_dotenv()

# --- Page & Logger Configuration ---
st.set_page_config(
    layout="wide",
    page_title="Tripmate"
)
logging.basicConfig(level=logging.INFO) # Added basic logging for debugging

# --- Agent Configuration ---
@st.cache_resource
def setup_portia_agent():
    """Sets up and caches the Portia agent using environment variables."""
    # Retrieve API keys from environment variables
    portia_key = os.getenv("PORTIA_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")

    if not all([portia_key, gemini_key, tavily_key]):
        st.error("Cannot initialize agent. One or more API keys are missing from the environment variables.")
        return None

    try:
        # Set environment variables required by Portia and underlying tools
        os.environ["PORTIA_API_KEY"] = portia_key
        os.environ["GEMINI_API_KEY"] = gemini_key
        os.environ["TAVILY_API_KEY"] = tavily_key

        my_config = Config.from_default(
            llm_provider=LLMProvider.GOOGLE,
            default_model="gemini-1.5-flash",
            storage_class=StorageClass.CLOUD,
            storage_dir="./production_states",
            default_log_level=LogLevel.DEBUG,
            default_log_sink="./agent_audit.log",
            json_log_serialize=True,
        )

        portia_agent = Portia(
            config=my_config,
            tools=DefaultToolRegistry(my_config) + open_source_tool_registry + [
                BrowserTool(infrastructure_option=BrowserInfrastructureOption.REMOTE)
            ],
            execution_hooks=CLIExecutionHooks(),
        )
        return portia_agent
    except Exception as e:
        logging.error(f"Failed to initialize Portia agent: {e}")
        st.error(f"Failed to initialize the agent. Please check your API keys and configuration. Error: {e}")
        return None

# --- Main Application UI ---
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: -2rem -2rem 2rem -2rem;
        padding: 3rem 2rem;
        border-radius: 0 0 20px 20px;
    }
    .main-header h1 {
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .main-header p {
        font-size: 1.2rem;
        color: rgba(255,255,255,0.9);
        margin: 0;
        font-style: italic;
    }
    .form-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #e9ecef;
        margin-bottom: 2rem;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e9ecef;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e9ecef;
        transition: all 0.3s ease;
    }
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
</style>

<div class="main-header">
    <h1>Tripmate</h1>
    <p>AI-Powered Travel Planning Assistant</p>
</div>
""", unsafe_allow_html=True)

# Initialize the agent
portia = setup_portia_agent()

if not portia:
    st.markdown("""
    <div style="background: #e2e3e5; color: #383d41; padding: 1.5rem; border-radius: 10px; border: 1px solid #d6d8db; margin: 2rem 0; text-align: center;">
        <h4 style="margin: 0 0 1rem 0; color: #383d41;">Setup Required</h4>
        <p style="margin: 0; color: #6c757d;">Please ensure your API keys are set in a `.env` file to start planning your trip.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()


col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;">
        <h2 style="color: white; margin: 0; font-size: 1.8rem; font-weight: 600;">Plan Your Trip</h2>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        form_col1, form_col2 = st.columns(2)
    with form_col1:
        origin = st.text_input("FROM", "New York")
        start_date = st.text_input("START DATE", "15 Oct 2025")
        duration = st.text_input("DURATION", "7 days")
    with form_col2:
        destination = st.text_input("TO", "Paris")
        return_date = st.text_input("RETURN DATE", "22 Oct 2025")
        budget = st.text_input("BUDGET", "Approx $2000")

    st.markdown("---")
    trip_type = st.radio("TRIP TYPE", ["Solo", "Family", "Friends", "Business"], horizontal=True)
    accommodation = st.radio("ACCOMMODATION", ["Budget", "Luxury", "Flexible"], horizontal=True)
    food_preferences = st.radio("FOOD PREFERENCES", ["Veg", "Non Veg", "Flexible"], horizontal=True)
    st.markdown("---")

    activities = st.text_input("ACTIVITIES", "Museums, historic sites, local cuisine tours")
    emails_input = st.text_input("EMAILS", "example1@gmail.com, example2@gmail.com")
    custom_instructions = st.text_area("CUSTOM INSTRUCTIONS", "Focus on cultural experiences and avoid tourist traps. Include at least one day trip outside the main city.")

    st.markdown("""
    <style>
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)
    
    if st.button("Generate Travel Plan", use_container_width=True):
        st.markdown('</div>', unsafe_allow_html=True)
        required_fields = { "Origin": origin, "Destination": destination, "Start Date": start_date,
                            "Return Date": return_date, "Duration": duration, "Budget": budget, "Emails": emails_input }
        missing = [field for field, value in required_fields.items() if not value.strip()]

        if missing:
            st.markdown(f"""
            <div style="background: #fff3cd; color: #856404; padding: 1rem; border-radius: 10px; border: 1px solid #ffeaa7; margin: 1rem 0;">
                <h4 style="margin: 0; color: #856404;">Please fill all required fields: {', '.join(missing)}</h4>
            </div>
            """, unsafe_allow_html=True)
        else:
            emails = [email.strip() for email in emails_input.split(',')]

            task = f"""
            Make a Travel Plan with the following details:
            - Origin: {origin} - Destination: {destination} - Start Date: {start_date} - Return Date: {return_date}
            - Duration: {duration} - Trip Type: {trip_type} - Budget: {budget} - Accommodation Preference: {accommodation}
            - Activities & Interests: {activities} - Dining Preferences: {food_preferences} - Custom Instructions: {custom_instructions}
            - Expected Final Output: A detailed day-by-day itinerary, travel options, and recommendations.
            - Once the plan is generated, email a comprehensive report to the following addresses: {", ".join(emails)}.
            - Add these events to a calendar.
            - Send calendar invitations to these emails: {", ".join(emails)}
            """

            with col2:
                st.markdown("""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;">
                    <h2 style="color: white; margin: 0; font-size: 1.8rem; font-weight: 600;">AI Agent Status</h2>
                </div>
                """, unsafe_allow_html=True)
                plan_steps_container = st.container()
                final_output_container = st.container()

                # --- Agent Planning Stage ---
                try:
                    with plan_steps_container:
                        st.markdown("""
                        <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; border-left: 4px solid #667eea; margin-bottom: 1rem;">
                            <h3 style="color: #333; margin: 0; font-size: 1.4rem; font-weight: 600;">Planning Phase</h3>
                        </div>
                        """, unsafe_allow_html=True)
                        with st.spinner('AI Agent is generating your travel plan...'):
                            plan = portia.plan(task)
                            plan_output = plan.pretty_print()
                            st.text_area("Generated Plan Steps", plan_output, height=300)
                            st.session_state.plan_generated = plan # Store plan for execution
                except Exception as e:
                    logging.error(f"An error occurred during planning: {e}")
                    st.error(f"An error occurred during the planning phase: {e}")
                    st.stop() # Stop execution if planning fails

                # --- Agent Execution Stage ---
                try:
                    with final_output_container:
                        st.markdown("""
                        <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; border-left: 4px solid #28a745; margin-bottom: 1rem;">
                            <h3 style="color: #333; margin: 0; font-size: 1.4rem; font-weight: 600;">Execution Phase</h3>
                        </div>
                        """, unsafe_allow_html=True)
                        with st.spinner('AI Agent is executing your plan and sending communications...'):
                            plan_to_run = st.session_state.get("plan_generated")
                            if plan_to_run:
                                plan_run = portia.run_plan(plan_to_run, end_user="Streamlit User")

                                # Check the final state of the agent run
                                if plan_run and plan_run.state == PlanRunState.COMPLETE:
                                    final_summary = (
                                        f"Plan successfully executed!\n\nA detailed travel itinerary for your {trip_type} trip "
                                        f"from {origin} to {destination} has been generated and sent to: {emails_input}."
                                    )
                                    st.markdown("""
                                    <div style="background: #d4edda; color: #155724; padding: 1rem; border-radius: 10px; border: 1px solid #c3e6cb; margin: 1rem 0;">
                                        <h4 style="margin: 0; color: #155724;">Execution Complete!</h4>
                                    </div>
                                    """, unsafe_allow_html=True)
                                    st.text_area("Execution Summary", final_summary, height=150)
                                else:
                                    failed_state = plan_run.state.value if plan_run else 'N/A'
                                    st.markdown(f"""
                                    <div style="background: #f8d7da; color: #721c24; padding: 1rem; border-radius: 10px; border: 1px solid #f5c6cb; margin: 1rem 0;">
                                        <h4 style="margin: 0; color: #721c24;">Agent run failed to complete. Final state: {failed_state}</h4>
                                    </div>
                                    """, unsafe_allow_html=True)
                            else:
                                st.error("No plan was available to execute.")
                except Exception as e:
                    logging.error(f"An error occurred during execution: {e}")
                    st.error(f"An error occurred during the plan execution phase: {e}")
