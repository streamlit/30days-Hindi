import glob
import os
import urllib.request

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)


md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob1("content", "*.md")]
)

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))
st.markdown("# Streamlit के 30 दिन")

days_list = [f"Day {x}" for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox(
    "चुनौती शुरू करें 👇", days_list, key="day", on_change=update_params
)

with st.expander("#30DaysOfStreamlit के बारे में"):
    st.markdown(
        """
    **#30DaysOfStreamlit** एक कोडिंग चुनौती है जिसे Streamlit ऐप बनाने में आपकी मदद करने के लिए डिज़ाइन किया गया है।
    
    विशेष रूप से, आप निम्न में सक्षम होंगे:
    - Streamlit ऐप्स बनाने के लिए एक कोडिंग वातावरण सेट करें
    - अपना पहला Streamlit ऐप बनाएं
    - अपने Streamlit ऐप के लिए उपयोग करने के लिए सभी भयानक इनपुट/आउटपुट विजेट्स के बारे में जानें
    """
    )

# Sidebar
st.sidebar.header("बारे में")
st.sidebar.markdown(
    "[Streamlit](https://streamlit.io) एक Python लाइब्रेरी है जो Python में इंटरैक्टिव, डेटा-ड्रिवन वेब एप्लिकेशन बनाने की अनुमति देती है।"
)

st.sidebar.header("संसाधन")
st.sidebar.markdown(
    """
- [Streamlit प्रलेखन](https://docs.streamlit.io/)
- [प्रवंचक पत्रक](https://docs.streamlit.io/library/cheatsheet)
- [पुस्तक](https://www.amazon.com/dp/180056550X) (डेटा साइंस के लिए Streamlit के साथ शुरुआत करना)
- [ब्लॉग](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (डेटा साइंस के लिए Streamlit में महारत हासिल कैसे करें)
"""
)

st.sidebar.header("Deploy")
st.sidebar.markdown(
    "आप कुछ ही क्लिक में [Streamlit Community Cloud](https://streamlit.io/cloud) का इस्तेमाल करके Streamlit ऐप्लिकेशन को तेज़ी से डिप्लॉय कर सकते हैं।"
)

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f"# 🗓️ {i}")
        j = i.replace(" ", "")
        with open(f"content/{j}.md", "r") as f:
            st.markdown(f.read())
        if os.path.isfile(f"content/figures/{j}.csv") == True:
            st.markdown("---")
            st.markdown("### Figures")
            df = pd.read_csv(f"content/figures/{j}.csv", engine="python")
            for i in range(len(df)):
                st.image(f"content/images/{df.img[i]}")
                st.info(f"{df.figure[i]}: {df.caption[i]}")
