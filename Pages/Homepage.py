from openai import OpenAI
from PIL import Image
import streamlit as st                                         
import json
import requests
from streamlit_lottie import st_lottie

# Initialize OpenAI client with API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Arcane Cypher: Next Generation NFTS", page_icon=":robot_face:", layout="wide")
st.sidebar.success("slect a page")

def generate_images(img_description):
    img_response=client.images.generate(
            model="dall-e-3",
            prompt=img_description,
            size="1024x1024",
            quality="high",
            n=1 
        
    )
    image_url = img_response.data[0].url
    return image_url


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding1 = load_lottiefile("lottiefiles/Animation - 1714958714611.json")  
lottie_bg1 = load_lottieurl("https://lottie.host/5096f5ac-5fb7-48f3-a13b-4c658f0cc52e/RnC4lmt3xD.json")


# Display the background Lottie animation
st_lottie(
    lottie_bg1,
    speed=0.5,
    reverse=False,
    loop=True,
    quality="high",
    height="100%",
    width="100%",
    key="background"
)

# Embed the Google Fonts with css code
st.markdown("""
    <style>
    html body > div:first-child > div:first-child {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -9999 !important; /* Extreme specificity and priority */
    }
    </style>
""", unsafe_allow_html=True)

st.title("NFT Generator Tool :male_mage:")
# Use a container to wrap the subheader
st.markdown('<div class="container"><h2>Tokenized NFTs Powered By AI</h2></div>', unsafe_allow_html=True)

# Adding more vertical space
st.markdown("#")
st.markdown("#")
st.markdown("#")

#####################################################################################################################
col1, col2 = st.columns([10, 5])


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("lottiefiles/Animation - 1714929179608.json")
lottie_hello = load_lottieurl("https://lottie.host/f1e45f7e-0e6b-40b6-85fd-92917eef0eeb/rnpUOaFSl3.json")

with col1:
    st.write("Arcane Cypher is a cutting-edge dApp leveraging artificial intelligence to create unique, AI-generated NFTs tokenized on the Ethereum blockchain. This innovative platform not only allows users to generate one-of-a-kind NFT artworks based on their input but also features a dynamic NFT marketplace. Here, users can explore and purchase 'loot boxes,' which evolve into distinctive NFT art upon minting. These evolving NFTs offer a novel and interactive way for collectors and enthusiasts to engage with digital art. All NFTs created and purchased through Arcane Cypher can be seamlessly traded on OpenSea, enabling easy access to a broader marketplace and community. Arcane Cypher is your gateway to exploring and owning evolving digital art in this blockchain era!!")


with col2:
    st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="high",
    height="250px",
    width="350px",
    key=None,
)

img_description = st.text_input("Enter a description for the NFT you want to generate:")

# Create a button to generate images
if st.button("Create NFT") and img_description:
    with st.spinner(text='Generating image...'):
        generate_image=generate_images(img_description)
        st.image(generate_image)