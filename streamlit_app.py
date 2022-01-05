import streamlit as st
import wget

def fetch(url):
    try:
        return wget.download(url)
    except Exception:
        return {}

def main():
  st.title("My Streamlit App!")
  with st.form("app_form"):
    status_code = st.radio("Pick a status code", ('101','102','405','406','407','416','417','500','502','521'))
    submitted = st.form_submit_button("Submit")
    if submitted:
      st.write(f"You pressed status code {status_code} and submit!")
      # Streamlit Support: calling URL and filtering status_code in the URL as paramter based on selection, also handling bad status_code.
      targetURL = fetch(f"https://http.cat/{status_code}")
      if targetURL:
        st.image(targetURL)
      else:
        st.error("Error! Bad Status_Code in the selection")
if __name__ == '__main__':
  main()  