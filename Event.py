import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Event Registration",
    page_icon="📅",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:42px;
    color:#4CAF50;
    font-weight:bold;
}
.sub-text{
    text-align:center;
    color:gray;
    font-size:18px;
}
.stButton>button{
    width:100%;
    background-color:#4CAF50;
    color:white;
    font-size:18px;
    border-radius:8px;
}
.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📢 About Event")
st.sidebar.write("This platform allows users to register for upcoming tech events.")
st.sidebar.write("### Available Events")
st.sidebar.write("• Python Workshop")
st.sidebar.write("• AI Seminar")
st.sidebar.write("• Web Development Bootcamp")

# Title
st.markdown("<p class='main-title'>📅 Event Registration</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Register for exciting tech events</p>", unsafe_allow_html=True)

# Event Banner
st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c")

st.divider()

# Form
with st.form("registration_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email Address")

    with col2:
        phone = st.text_input("📱 Phone Number")
        gender = st.radio("⚧ Gender", ["Male", "Female", "Other"])

    city = st.selectbox(
        "🏙 Select City",
        ["Hyderabad", "Bangalore", "Chennai", "Pune"]
    )

    event = st.selectbox(
        "🎯 Select Event",
        ["Python Workshop", "AI Seminar", "Web Development Bootcamp"]
    )

    skills = st.multiselect(
        "💻 Your Skills",
        ["Python", "Machine Learning", "HTML", "CSS", "JavaScript"]
    )

    date = st.date_input("📅 Select Event Date")

    submit = st.form_submit_button("Register Now 🚀")

# Result
if submit:
    if name and email and phone:
        st.success("🎉 Registration Successful!")

        st.write("### 📋 Registration Details")
        st.write(f"👤 **Name:** {name}")
        st.write(f"📧 **Email:** {email}")
        st.write(f"📱 **Phone:** {phone}")
        st.write(f"⚧ **Gender:** {gender}")
        st.write(f"🏙 **City:** {city}")
        st.write(f"🎯 **Event:** {event}")
        st.write(f"💻 **Skills:** {', '.join(skills)}")
        st.write(f"📅 **Date:** {date}")

    else:
        st.error("⚠️ Please fill all required fields.")

st.divider()

# Footer
st.markdown("<p class='footer'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)