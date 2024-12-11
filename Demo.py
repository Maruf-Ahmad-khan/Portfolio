import streamlit as st
import base64

class DataScientistProfileApp:
    def __init__(self):
        # Basic profile attributes
        self.title = "Responsive Data Scientist Profile"
        self.header_text = "LET THE DATA GLOW!"
        self.profile_name = "Maruf Khan"
        self.profile_title = "DATA SCIENTIST: THIS IS ME"
        self.profile_description = [
            "💪 enjoys tackling challenging issues in a variety of fields",
            "🌍 is employed in the data science field at the moment.",
            "🔥 overcame difficult tasks to extract valuable insights from finance, sales, affiliate, and digital marketing data.",
            "⚡ uses a variety of data structures, including text, image, graph, and numerical ones.",
            "🌟 in the end, attempts to make the information sparkle!"
        ]
        
        # Links for pages
        self.pages = {
            "CV": "https://digitalresume-zrpmbgpkve3xngfcelnjz3.streamlit.app/",
            "Power BI Reports": "https://maruf-ahmad-khan-campaign-reporting-demo-mlivgc.streamlit.app/",
            "Power BI Weekly and Monthly Reports": "https://geminichatbot-kmvys7catpysctcstxk2np.streamlit.app/",
            "Data Science Project": "Data_Science.html"
        }

    def get_base64_image(self, file_path):
        """Convert an image file to a base64 string."""
        try:
            with open(file_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        except FileNotFoundError:
            return None

    def render_header(self):
        st.markdown(f"<h1 style='text-align: center; color: white;'>{self.header_text}</h1>", unsafe_allow_html=True)

    def render_nav(self):
        # Navigation bar
        st.markdown(
            """
            <nav style='display: flex; justify-content: space-between; background: #333; color: white; padding: 10px;'>
                <ul style='list-style-type: none; display: flex; padding: 0; margin: 0;'>
            """,
            unsafe_allow_html=True
        )
        for page, link in self.pages.items():
            st.markdown(
                f"<li style='margin-right: 20px;'><a href='{link}' style='color: white; text-decoration: none;'>{page}</a></li>",
                unsafe_allow_html=True
            )
        st.markdown("</ul></nav>", unsafe_allow_html=True)

    def render_profile(self):
        st.markdown("<div style='max-width: 800px; margin: auto; background: black; color: white; padding: 20px;'>", unsafe_allow_html=True)

        # Profile Image and Description
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("Shadow Tutorial/images/My pic.jpg", width=350, caption=self.profile_name)
        with col2:
            st.markdown(f"<h1>{self.profile_name}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h2>{self.profile_title}</h2>", unsafe_allow_html=True)
            st.markdown("<ul>", unsafe_allow_html=True)
            for item in self.profile_description:
                st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    def render_footer(self):
        linkedin_icon = self.get_base64_image("Shadow Tutorial/images/linkedn.png")
        github_icon = self.get_base64_image("Shadow Tutorial/images/github.jpeg")
        twitter_icon = self.get_base64_image("Shadow Tutorial/images/twitter.jpeg")

        if linkedin_icon and github_icon:
            # Footer with social links
            footer_html = f"""
            <footer style='background: #000; color: white; text-align: center; padding: 20px;'>
                <p>&copy; 2024 Data Scientist. All rights reserved.</p>
                <div style="display: flex; justify-content: center; gap: 20px; margin-top: 10px;">
                    <a href="https://www.linkedin.com/in/maruf-khan-1516a4224/" target="_blank" style="text-decoration: none; color: white;">
                        <img src="data:image/png;base64,{linkedin_icon}" style="width: 30px; height: 30px; vertical-align: middle;"> LinkedIn
                    </a>
                    <a href="https://github.com/Maruf-Ahmad-khan?tab=followers" target="_blank" style="text-decoration: none; color: white;">
                        <img src="data:image/png;base64,{github_icon}" style="width: 30px; height: 30px; vertical-align: middle;"> GitHub
                    </a>
                     <a href="https://x.com/MarufKh64948760?tab=followers" target="_blank" style="text-decoration: none; color: white;">
                        <img src="data:image/png;base64,{twitter_icon}" style="width: 30px; height: 30px; vertical-align: middle;"> Twitter
                    </a>
                </div>
            </footer>
            """
            st.markdown(footer_html, unsafe_allow_html=True)
        else:
            st.error("Error: Social media icons not found!")

    def run(self):
        # Set page config as the very first Streamlit command
        st.set_page_config(page_title=self.title, layout="wide")
        
        # Call rendering methods
        self.render_header()
        self.render_nav()
        self.render_profile()
        self.render_footer()


if __name__ == "__main__":
    app = DataScientistProfileApp()
    app.run()
