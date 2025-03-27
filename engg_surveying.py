# **Checking Enginnering Surveying I by Sir Ahmed**
# Convert Quadrantal Bearing to Azimuth Angle
# Convert Azimuth Angle to Quadrantal Bearing
# Gives step by step calculation
# A perfect blend of aesthetic UI and intuitive UX.
#

import streamlit as st
import re
import time
import base64

# Page Configuration
st.set_page_config(
    page_title="Engg Surveying I", 
    page_icon="🧭", 
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://www.google.com/search?q=help",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": """# SMAASU Corporation©️  
        https://g.co/kgs/VvQB8W9
        App Version 0.617"""}
    )

def set_bg_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_image()  # Apply the background image
# https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg
# Sidebar
st.sidebar.title("👷🏻‍♂️ Engg Surveying I")
tabs = st.sidebar.radio("", ["Azimuth to Bearing", "Bearing to Azimuth", "Profile Leveling", "Contour Line", "About App", "About Us", "About Me"])

if tabs == "Azimuth to Bearing":
    # function for checking each requirement
    col1, col2, col3 = st.columns([2,6,2])
    
    with col2:
        st.write("# 👷🏻‍♂️ Engineering Surveying I ")
        st.write(" Azimuth Angle to Quadrantal Bearing Converter & Guide")
        
        tab1, tab2 = st.tabs(["🧭 Converter", "📕 Guide"])
            
        with tab1:   
            #Take the Azimuth Angle as an input 
            st.write("### Azimuth to Bearing Angle Converter")
            azimuth = st.number_input("Enter Azimuth Angle")

            #Normalize the Positive and Negative Angles 
            if azimuth >=360:
                azimuth = azimuth%360
            elif azimuth < 0:
                azimuth = (360-abs(azimuth))%360
                
            st.write(f"###### Azimuth Normalize to {azimuth:.2f}")

            if azimuth == 0:
                st.write(f"### Quadrant : North")
            elif azimuth == 90:
                st.write(f"### Quadrant : East")
            elif azimuth == 180:
                st.write(f"### Quadrant : South")
            elif azimuth == 270:
                st.write(f"### Quadrant : West")
            elif azimuth >90 and azimuth<180:
                st.write(f"### {abs(azimuth-180):.2f}˚ SE (from South to East)")
            elif azimuth > 180 and azimuth < 270:
                st.write(f"### {abs(azimuth-180):.2f}˚ SW (from South to West)")
            elif azimuth > 270 and azimuth < 360:
                st.write(f"### {abs(azimuth-360):.2f}˚ NW (from North to West)")
            elif azimuth > 0 and azimuth < 90:
                st.write(f"### {abs(azimuth):.2f}˚ NE (from North to East)")
        with tab2:
            st.header("Azimuth to Bearing Conversion")
            st.write("Azimuth is an angle measured **clockwise from North (0°) to 360°**.")
            st.write("Bearing is a compass direction expressed in **North/South and East/West** (e.g., N 45° E).")
            
            st.subheader(" Conversion Rules:")
            st.markdown("""
            - **0° - 90°** → **N (Azimuth) E**
            - **90° - 180°** → **S (180° - Azimuth) E**
            - **180° - 270°** → **S (Azimuth - 180°) W**
            - **270° - 360°** → **N (360° - Azimuth) W**
            """)
            
            st.subheader(" Quick Examples:")
            st.table({"Azimuth": [45, 135, 225, 315], "Bearing": ["N 45° E", "S 45° E", "S 45° W", "N 45° W"]})
            
            st.write(" **Formula for Manual Calculation:**")
            st.code("Bearing = N/S (adjusted angle) E/W")
            st.write(" **Try it out and convert azimuth to bearing instantly!**")

elif tabs == "Bearing to Azimuth":
    # function for checking each requirement
    col1, col2, col3 = st.columns([2,6,2])
    with col2:
        st.write("# 👷🏻‍♂️ Engineering Surveying I ")
        st.write("Quadrantal Bearing to Azimuth Angle Converter & Guide")
        
        tab1, tab2 = st.tabs(["🧭 Converter", "📕 Guide"])
        with tab1:   
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                bearing = st.number_input("Enter Quadrantal Bearing Angle")
            with sub_col2:
                quadrant = st.selectbox("Select Quadrantal Bearing", ["North to East", "South to East", "South to West", "North to West"])

            #Removing decimal places if number is round byt converting to integer
            if bearing == int(bearing):
                bearing = int(bearing)
            
            #Normalize the Positive and Negative Angles 
            # if bearing >= 90:
            #     bearing = bearing%90
            # elif bearing < 0:
            #     bearing = (90-abs(bearing))%90
                
            st.write(f"###### Azimuth Normalize to {bearing:.2f}")

            if quadrant =="North to East":
                st.write(f"### Azimuth Angle : {abs(bearing):.2f}˚")
                st.warning("Only this case it will remain same. ")
                st.success("My Professor Dr. Ahmed taught me.😊")
            elif quadrant =="South to East":
                st.write(f"### Azimuth Angle : {abs(180-bearing):.2f}˚")
                st.write(f"After converting Quadrantal Bearing South to East, the Azimuth will become {abs(bearing):.2f}˚")
                # Calculation Stuff
                st.write(f"### Calculation :")
                st.write(f"South to East = 180˚ - {abs(bearing):.2f}˚")
                st.write(f"South to East = {abs(180-bearing):.2f}˚")
            elif quadrant =="South to West":
                st.write(f"### Azimuth Angle : {abs(180+bearing):.2f}˚")
                st.write(f"After converting Quadrantal Bearing South to West, the Azimuth will become {abs(bearing):.2f}˚")
                # Calculation Stuff
                st.write(f"### Calculation :")
                st.write(f"South to East = 180˚ + {abs(bearing):.2f}˚")
                st.write(f"South to East = {abs(180+bearing):.2f}˚")
            elif quadrant =="North to West":
                st.write(f"### Azimuth Angle : {abs(360-bearing):.2f}˚")
                st.write(f"After converting Quadrantal Bearing South to East, the Azimuth will become {abs(bearing):.2f}˚")
                # Calculation Stuff
                st.write(f"### Calculation :")
                st.write(f"South to East = 360˚ - {abs(bearing):.2f}˚")
                st.write(f"South to East = {abs(360-bearing):.2f}˚")
        
        with tab2:                        
            st.header(" Bearing to Azimuth Conversion")
        
            st.write("Bearing is a compass direction expressed in **North/South and East/West** (e.g., N 45° E).")
            st.write("Azimuth is an angle measured **clockwise from North (0°) to 360°**.")
            
            st.subheader(" Conversion Rules:")
            st.markdown("""
            - **N X° E** → **Azimuth = X°**
            - **S X° E** → **Azimuth = 180° - X°**
            - **S X° W** → **Azimuth = 180° + X°**
            - **N X° W** → **Azimuth = 360° - X°**
            """)
            
            st.subheader("Quick Examples:")
            st.table({"Bearing": ["N 45° E", "S 45° E", "S 45° W", "N 45° W"], "Azimuth": [45, 135, 225, 315]})
            
            st.write(" **Formula for Manual Calculation:**")
            st.code("Azimuth = Adjusted Angle (Based on Quadrant)")
            st.write(" **Try it out and convert bearing to azimuth instantly!**")

elif tabs == "About App":
    col1, col2, col3 = st.columns([1.5,7,1.5])
    with col2:
        # About App Section
        st.markdown(
            """
            # 🔐 Password Sentinel 
            ## Your Ultimate Password Strength Analyzer

            Developed by **SMAASU Corporation**, Password Sentinel is an advanced web application designed to evaluate and enhance password security. This tool provides real-time password analysis, strength classification, and security suggestions to help you create unbreakable passwords.

            ## ✨ Key Features:
            - 🛡 **Strength Assessment** – Checks uppercase, lowercase, numbers, and special characters.
            - 📊 **Password Strength Rating** – Categorizes passwords as **Weak, Moderate, or Strong**.
            - ⏳ **Crack Time Estimation** – Predicts how long a brute-force attack would take.
            - ⚠ **Requirement Suggestions** – Highlights missing security requirements.
            - 🔑 **Strong Password Generator** – Suggests highly secure passwords if needed.
            - 🔐 **Security Tips** – Educates users on best password practices.

            🚀 **Ensure your passwords are robust and secure with Password Sentinel!**  
            """,
            unsafe_allow_html=True
        )
            
elif tabs == "About Me":
    st.write("# 🏅 Syed Muhammad Abdullah Abdulbadeeii")
    col1, col2, col3 = st.columns([4.5,1,4.5])
    with col1:
    # Personal Title 🏅🌟💡🌱🌍👤
        st.write("\n\n")
        st.markdown(
        "<img src='https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg' width='550'>",
        unsafe_allow_html=True)

        # st.image("https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg", use_container_width=True, width=100)
        # Expertise & Interests
        st.write("\n\n")
        st.header("🚀 Areas of Expertise")
        st.markdown(
            """
            - 🏗️ **Civil Engineering & Smart Infrastructure** – Engineering sustainable and innovative urban solutions.
            - 💻 **Software & Web Development** – Creating intelligent digital solutions to optimize efficiency.
            - 🤖 **Artificial Intelligence & Data Science** – Harnessing AI-driven technologies for smarter decision-making.
            - 📊 **Data Processing & Automation** – Streamlining complex workflows through advanced automation.
            - 🚀 **Entrepreneurship & Technological Innovation** – Spearheading startups that drive meaningful change.
            - ❤️ **Philanthropy & Social Impact** – Advocating for and supporting communities in need.
            """
        )


    with col3:
        st.write("# 🌱 About Me")
        # Introduction
        st.markdown(
            """
            I am **Syed Muhammad Abdullah Abdulbadeeii**, a **Civil Engineering Student at NED University of Engineering & Technology, Entrepreneur, Innovator, and Philanthropist**. 
            With a deep passion for **Artificial Intelligence, Architecture, and Sustainable Urbanization**, I am committed to pioneering **Transformative Solutions** that seamlessly integrate technology with real-world applications.
            
            My work is driven by a vision to **Build a Smarter, More Sustainable Future**, where cutting-edge innovations enhance efficiency, improve urban living, and empower businesses. 
            Beyond my professional pursuits, I am dedicated to **philanthropy**, striving to **uplift Muslims and support underprivileged communities**, fostering a society rooted in compassion, empowerment, and progress.
            """
        )
        
        # Vision & Journey
        st.header("🌍 My Vision & Journey")
        st.markdown(
            """
            As the founder of **SMAASU Corporation**, I have led groundbreaking initiatives such as **Data Duster**, a web-based platform revolutionizing data processing and automation. 
            My entrepreneurial journey is fueled by a relentless drive to **bridge the gap between technology and urban development**, delivering impactful solutions that **redefine the future of cities and industries**.
            
            **I believe in innovation, sustainability, and the power of technology to transform lives.** Through my work, I strive to create solutions that not only drive efficiency but also foster inclusivity and social well-being.
            
            **Let’s collaborate to build a brighter, more progressive future!**
            """
        )

elif tabs == "About Us":
    col1, col2, col3 = st.columns([1.5,7,1.5])
    with col2:

        # Company Title
        st.write("# 🏢 About SMAASU Corporation")

        # Introduction
        st.markdown(
            """
            **SMAASU Corporation** is a forward-thinking company committed to innovation in **technology, architecture, and sustainable urbanization**.
            Our vision is to create cutting-edge solutions that simplify workflows, enhance productivity, and contribute to a smarter, more efficient future.
            """
        )

        # Mission Section
        st.header("🌍 Our Mission")
        st.markdown(
            """
            At **SMAASU Corporation**, we aim to:
            - 🚀 **Develop pioneering software solutions** that enhance business efficiency.
            - 🏗️ **Revolutionize architecture and urban planning** with smart, sustainable designs.
            - 🌱 **Promote sustainability** in every project we undertake.
            - 🤝 **Empower businesses and individuals** with next-gen technology.
            """
        )

        # Core Values Section
        st.header("💡 Our Core Values")
        st.markdown(
            """
            - **Innovation** – Continuously pushing boundaries with cutting-edge technology.
            - **Sustainability** – Building a future that is eco-friendly and efficient.
            - **Excellence** – Delivering top-tier solutions with precision and quality.
            - **Integrity** – Upholding transparency and trust in every endeavor.
            """
        )

        # Call to Action
        st.markdown(
            """
            🚀 **Join us on our journey to create a smarter, more sustainable world with SMAASU Corporation!**
            """,
            unsafe_allow_html=True
        )
        st.link_button("🔗 Visit SMAASU Corporation", "https://g.co/kgs/VvQB8W9")



            