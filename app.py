import streamlit as st

class ContactPage:
    """Class to represent the contact page."""

    def __init__(self):
        self.title = "Contact Page"
        self.home_link = "https://portfolio-lpymrdq5w8enefstpltenm.streamlit.app/"

    def set_page_config(self):
        """Set the page configuration."""
        st.set_page_config(page_title=self.title, layout="wide")

    def render_header(self):
        """Render the header section with navigation."""
        st.markdown(
            """
            <style>
            .header-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #000;
                padding: 20px;
                color: white;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            }
            .logo-nav {
                display: flex;
                align-items: center;
            }
            .logo-nav img {
                width: 120px;
                margin-right: 20px;
            }
            .nav-links {
                list-style: none;
                display: flex;
                margin: 0;
                padding: 0;
                gap: 15px;
            }
            .nav-links a {
                text-decoration: none;
                color: #fff;
                font-weight: bold;
                padding: 10px 20px;
                border: 2px solid #fff;
                border-radius: 5px;
                transition: background-color 0.3s, color 0.3s;
            }
            .nav-links a:hover {
                background-color: #fff;
                color: #000;
            }
            </style>
            <div class="header-container">
                <ul class="nav-links">
                    <li><a href="{self.home_link}" target="https://portfolio-lpymrdq5w8enefstpltenm.streamlit.app/">Home</a></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def render_intro(self):
        """Render the introduction section."""
        st.markdown(
            """
            <style>
            .contact-intro {
                text-align: center;
                padding: 50px 0;
                background-color: #cfe2ff;
            }
            .contact-intro h1 {
                margin: 0;
                font-size: 36px;
            }
            </style>
            <section class="contact-intro">
                <h1>Contact</h1>
                <p>Have a project you'd like to discuss? Let's make something great together!</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    def render_contact_form(self):
        """Render the contact form."""
        st.markdown(
            """
            <style>
            .contact-form {
                background-color: #bbecbb;
                padding: 50px 0;
                text-align: center;
            }
            .form-container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
                background-color: #c0efa9;
                border-radius: 10px;
            }
            .form-container p {
                margin-bottom: 20px;
                color: #666;
            }
            .form-container label {
                display: block;
                margin-bottom: 5px;
                color: #333;
            }
            .form-container input,
            .form-container textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            .form-container textarea {
                resize: vertical;
                height: 150px;
            }
            .form-container button {
                width: 100%;
                padding: 15px;
                border: none;
                background-color: #007bff;
                color: #fff;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            .form-container button:hover {
                background-color: #0056b3;
            }
            </style>
            <section class="contact-form">
                <div class="form-container">
                    <p>Use the form below to let me know a little more about your objectives and I'll get back to you.</p>
                </div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        # Streamlit Input Form
        with st.form("contact_form"):
            st.text_input("Full Name", placeholder="Your Full Name")
            st.text_input("Email Address", placeholder="Your Email Address")
            st.text_area("Message", placeholder="Your Message")
            submitted = st.form_submit_button("Send")
            if submitted:
                st.success("Thank you for your message! I'll get back to you soon.")

    def run(self):
        """Run the contact page."""
        self.set_page_config()
        self.render_header()
        self.render_intro()
        self.render_contact_form()


# Run the Contact Page
if __name__ == "__main__":
    page = ContactPage()
    page.run()
