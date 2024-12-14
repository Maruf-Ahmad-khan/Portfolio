import streamlit as st
import streamlit.components.v1 as components  # Explicit import for components.v1

# Set page title
st.set_page_config(
    page_title="Power BI Report of Mall Clustering",
    layout="wide",  # Use the wide layout for better utilization of screen space
)

# Add title
st.title("Mall Clustering Dashboard")

# Power BI Embed URL
power_bi_embed_url = "https://app.powerbi.com/reportEmbed?reportId=96dc3012-6ca4-4185-bfe5-612c58c9b557&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b "

# HTML code to embed Power BI in an iframe
html_code = f"""
<iframe 
    title="Power BI Dashboard of Mall Clustering" 
    width="100%" 
    height="800"  # Increased height for better viewing
    src="{power_bi_embed_url}" 
    frameborder="0" 
    allowFullScreen="true">
</iframe>
"""

# Render the iframe in Streamlit
components.html(html_code, height=800)  # Match the iframe height here

st.title("Linear Regression Analysis")
power_bi_embed_url = "https://app.powerbi.com/reportEmbed?reportId=75ee586c-8990-4ddd-86db-d5a4ec331744&autoAuth=true&ctid=4a36bb2f-1c55-49e0-9a23-6281dfd38c6b"

# HTML code to embed Power BI in an iframe
html_code = f"""
<iframe 
    title="Power BI Dashboard of Linear Regression Analysis" 
    width="100%" 
    height="800"  # Increased height for better viewing
    src="{power_bi_embed_url}" 
    frameborder="0" 
    allowFullScreen="true">
</iframe>
"""

# Render the iframe in Streamlit
components.html(html_code, height=800)  # Match the iframe height here
