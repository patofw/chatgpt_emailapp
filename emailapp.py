import streamlit as st
import pandas as pd
# import random

from scr.email_generator import EmailGenerator
from scr.utils import get_config_params, load_inputs

config = get_config_params()  # Load config


def _save_output(
        file,
        customer: pd.Series,
        res: str,
        total_clients: int,
        clicked: bool = False
 ) -> None:
    msg = ""
    with st.spinner("Saving Results..."):
        if clicked:
            msg = f"Output saved in {config['output_path']}"
            file.write(
                f"{customer['name']};"
                f"{customer['email']};"
                f"{res}"
                "\n"
            )
            _get_next_item(total_clients)
            st.markdown(msg)
            st.session_state.save = "Select"


def _get_next_item(clients: int):
    if st.session_state.stage < clients - 1:
        st.session_state.stage += 1
    else:
        st.text("LAST CLIENT!")
        st.session_state.disable_button = True


def _create_intro_app():
    """
    Generates the intro for the Streamlit App
    """
    st.title(
        "ChatGPT powered Automated Personalized Email Generator App"
    )

    sub_title = """
        <h1 style="font-family:Times-New-Roman; color:Blue ;
        font-size: 20px;">Simple personalized email generator</h1>
    """
    st.markdown(sub_title, unsafe_allow_html=True)

    st.title("Generate Personalized Email")

    st.markdown("Original email template:")


def _email_expander(label: str, text: str):
    """Creates an box expander object in Streamlit

    Args:
        label (str): Name of the box. ie: Email Text
        text (str): Text of the box. ie: Dear Mr Patricio...
    """
    with st.expander(label):
        st.write(text)


def _create_app():
    """Creates the basic Personalization APP in Streamlit
    """

    # Create the intro of the APP.
    _create_intro_app()
    # Load inputs
    email_template, customer_df = load_inputs(config)
    output_res = open(config["output_path"], 'a+')

    # Write the template
    _email_expander("Email template", email_template)
    # Get total amount of customers
    total_clients = len(customer_df)
    st.text(f"We have {total_clients} clients for today...")

    # Set some initial session states.
    if "stage" not in st.session_state:
        st.session_state.stage = 0  # client counter
    # If no more clients, then we don't do more emails.
    if "disable_button" not in st.session_state:
        st.session_state.disable_button = False

    if st.session_state.disable_button:
        st.text("NO MORE CLIENTS IN CSV")

    # Get one customer at the time
    customer = customer_df.iloc[st.session_state.stage]
    # get the right data to personalize the email
    style = st.selectbox(
        'what style of e-mail you want to write',
        ('Formal', 'Informal', 'Funny')
    )
    personalization_map = {
        "name": customer["name"],
        "province": customer["province"],
        "style": style

    }
    # Load the prediction class
    email_generator = EmailGenerator(
        email_template,
        personalization_map
    )
    # One client at the time
    st.markdown(
        f"**Email for {customer['name']} - {customer['email']}**"
    )

    with st.form("Email Generator"):
        submit_button = st.form_submit_button(
            label='Generate Email',
            disabled=st.session_state.disable_button
        )
        response = None

        if submit_button:  # Generate Email personalization
            with st.spinner("Generating Email..."):

                # create the response email
                response = email_generator.generate_email()
                # response = "Exmaple mail" + str(random.randint(0, 100))
                if response:
                    # replace ";" as it can corrupt the resulting file
                    response = response.replace(";", ".")
                st.markdown("# Email Output:")
                _email_expander("Generated Email", response)

                st.markdown("____")
                # Save results or Skip client
                st.subheader(
                    "Automatically saving output..."
                )
                _save_output(
                    output_res,
                    customer,
                    response,
                    total_clients,
                    clicked=True
                )


def main():
    # For this example, just create the app
    # But you could imagine adding more functions
    # to this main()
    _create_app()

# When running it, launch the main function.


if __name__ == "__main__":
    main()
