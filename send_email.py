import streamlit as st
import smtplib

#st.title("Email Form")

def send_email():
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    subject = st.text_input("Subject")
    body = st.text_area("Body")
    
    if st.button("Send Email"):
        message = f"Subject: {subject}\n\n{body}"
        
        # Connect to SMTP server and send email
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login("sender@email.com", "password")
        smtp.sendmail("sender@email.com", "receiver@email.com", message.encode("utf-8"))
        smtp.quit()
        
        st.success("Email Sent!")