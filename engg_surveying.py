# **Checking Enginnering Surveying I by Sir Ahmed**
# Convert Quadrantal Bearing to Azimuth Angle
# Convert Azimuth Angle to Quadrantal Bearing
# Gives step by step calculation
# A perfect blend of aesthetic UI and intuitive UX.
# complete short guide of topics 
# made by student of Sir

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

st.sidebar.title("👷🏻‍♂️ Engg Surveying I")
tabs = st.sidebar.radio("", ["Azimuth to Bearing", "Bearing to Azimuth", "Dedicated to", "Profile Leveling", "Contour Line", "About App", "About Us", "About Me"])

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
                st.success("My Professor Dr. M. Ahmed taught me.😊")
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
    # About App Section
    def about_app():
        st.markdown("""
        # 👷🏻‍♂️ **Engineering Surveying I**  
        #### **By Sir Ahmed**
                    
        ## **About App**  

        ### 📌 **Key Features:**  

        ✔️ **Convert Quadrantal Bearing to Azimuth Angle**  
        → Instantly transform quadrantal bearings into their corresponding azimuth angles using a structured approach.  

        ✔️ **Convert Azimuth Angle to Quadrantal Bearing**  
        → Quickly determine the correct quadrantal bearing from a given azimuth angle.  

        ✔️ **Step-by-step calculations**  
        → Each conversion includes a clear breakdown of calculations, ensuring transparency and ease of learning.  

        ✔️ **Aesthetic UI combined with an intuitive UX**  
        → Designed with clarity in mind, the interface is visually appealing and easy to navigate for a seamless experience.  

        ✔️ **Comprehensive short guide covering fundamental concepts**  
        → Includes essential explanations, making it a quick reference tool for students and professionals.  

         **Built for engineering students and professionals, this app enhances accuracy and efficiency in surveying calculations.**  

         **Master surveying conversions effortlessly!**  
        """, unsafe_allow_html=True)

    # Call the function to display the about section
    col1, col2, col3 = st.columns([1.2,7.6,1.2])
    with col2:
        about_app()

elif tabs == "Dedicated to":
    # st.write("# 🏅 Syed Muhammad Abdullah Abdulbadeeii")
    col1, col2, col3 = st.columns([1.5,7,1.5])
    with col2:

        # Main Heading with Dedication
        st.write("# 🌟 Dedicated to Favourite Teacher – Dr. Muhammad Ahmed")
        st.markdown("### A Visionary Leader in Urban Resilience and Sustainability")

        # Adding Dr. Muhammad Ahmed's Image
        st.image("https://raw.githubusercontent.com/smaasui/SMAASU/refs/heads/main/file.png", caption="Dr. Muhammad Ahmed")

        # Section 1: Introduction
        st.header("🏅 About Dr. Muhammad Ahmed")
        st.write("""
        Dr. Muhammad Ahmed is an **Assistant Professor in the Department of Urban and Infrastructure Engineering at NED University** 
        and the **Director of the Centre for Environment and Social Sustainability (CESS)**. With **15+ years of expertise**, he specializes in:  
        - **Geographical Information Systems (GIS)**  
        - **Remote Sensing**  
        - **Urban and Regional Planning**  
        - **Seismic Hazard Mitigation**  

        His research integrates **technology with disaster resilience and infrastructure planning**, contributing to **regional, national, and international projects** in seismic hazard assessment, traffic engineering, and environmental sciences.
        """)

        # Section 2: Research Contributions and Leadership
        st.header("🏅 Research Contributions & Academic Leadership")
        st.write("Dr. Ahmed has been involved in multiple high-impact projects, including:")
        projects = {
            "Disaster Resilience Improvement in Pakistan (DRIP)": "Funded by HEC (PKR 78.94M)",
            "Toyota Road Improvement Project": "Sponsored by Indus Motors (PKR 11.89M)",
            "Seismic Risk Assessment of Major Hospitals in Karachi": "In collaboration with UNDP",
            "Flood and Seismic Risk Assessment for Karachi and Quetta": "Funded by the World Bank"
        }

        for project, details in projects.items():
            st.markdown(f"- **{project}** – {details}")

        st.write("He has supervised numerous **Ph.D. and Master’s theses**, covering topics such as:")
        st.markdown("""
        - **AI-driven Road Safety using UAV Aerial Footage**  
        - **GIS-Based Frameworks for Coastal Urban Planning**  
        - **Probabilistic Seismic Hazard Analysis for Infrastructure Resilience**  
        """)

        # Section 3: Publications and International Engagement
        st.header("🏅 Publications & Global Recognition")
        st.write("Dr. Ahmed has authored several research papers in renowned journals, including:")
        publications = [
            "📝 **Decoding Informal Settlements in Karachi using Machine Learning Algorithms** – Remote Sensing in Earth Systems Sciences (2024)",
            "📝 **From Stationary to Nonstationary UAVs: Deep-Learning-Based Vehicle Speed Estimation** – Algorithms (2024)",
            "📝 **Probabilistic Seismic Hazard Analysis-Based Zoning Map of Pakistan** – Journal of Earthquake Engineering (2022)"
        ]

        for pub in publications:
            st.markdown(pub)

        st.write("""
        He has represented **Pakistan and NED University** in **global research forums** held in **Turkey, Jordan, the UK, and Portugal**.  
        He is also an **affiliate member of the Earthquake Engineering Research Institute (EERI)** and has contributed to **national curriculum development** in Remote Sensing, GIS, and Disaster Management.
        """)

        # Footer
        st.markdown("---")
        st.markdown("📢 **Dr. Muhammad Ahmed continues to inspire the next generation of engineers and researchers in urban resilience, disaster preparedness, and sustainable infrastructure.** 🚀")


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
        st.write("# 🚀 Areas of Expertise")
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
        st.write("# 🌍 My Vision & Journey")
        st.markdown(
            """
            As the founder of **SMAASU Corporation**, I have led groundbreaking initiatives such as **Data Duster**, a web-based platform revolutionizing data processing and automation. 
            My entrepreneurial journey is fueled by a relentless drive to **bridge the gap between technology and urban development**, delivering impactful solutions that **redefine the future of cities and industries**.
            
            **I believe in innovation, sustainability, and the power of technology to transform lives.** Through my work, I strive to create solutions that not only drive efficiency but also foster inclusivity and social well-being.
            
            **Let’s collaborate to build a brighter, more progressive future!**
            """
        )
        
    st.write("# 🔗 Engineering connections !")
    st.link_button("🔗 Stay connected on LinkedIn!", "https://www.linkedin.com/in/smaasui/")


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

if tabs == "Profile Leveling":
    col1, col2, col3 = st.columns([2,6,2])
    with col2:

        st.write("# **Releasing Coming Soon...** 🚀")
        st.write("#### Stay tuned!")
if tabs == "Contour Line":
    col1, col2, col3 = st.columns([2,6,2])
    with col2:

        st.write("# **Releasing Coming Soon...** 🚀")
        st.write("#### Stay tuned!")



            
