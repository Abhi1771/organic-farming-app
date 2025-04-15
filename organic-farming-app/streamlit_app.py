import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Organic Farming Platform", layout="wide")
st.title("🌱 Organic Farming Support & Marketing Platform")

# Sidebar navigation
menu = st.sidebar.radio("Navigate", ["Home", "Educational Resources", "Post a Product", "Marketplace", "Community Forum", "Loan/Donation Assistance"])

# Dummy storage for products and posts (can later connect to Firebase)
if 'products' not in st.session_state:
    st.session_state.products = []
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = []

# Home
if menu == "Home":
    st.header("Welcome to the Digital Platform for Organic Farmers")
    st.markdown("""
        This platform is a one-stop destination for:
        - 🌿 Learning organic practices and sustainable farming
        - 🛍️ Showcasing and selling organic products
        - 💬 Interacting with the farming community
        - 💰 Applying for loans and donations
    """)

# Educational Resources
elif menu == "Educational Resources":
    st.header("📚 Learn Organic Farming")

    st.markdown("Organic farming uses natural methods to grow crops while maintaining soil fertility and ecological balance. Below are essential topics:")

    # Compact Topic 1
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**🌾 Organic Fertilizers**  \nUse compost, green manure, bone meal, and biofertilizers.")
    with col2:
        st.video("https://m.youtube.com/watch?v=lRyXlvIJFWI&pp=ygUPI2FncmljdXR1cmVzb2ls")

    # Compact Topic 2
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**🐛 Natural Pest Control**  \nNeem oil spray, crop rotation, and intercropping techniques help manage pests.")
    with col2:
        st.video("https://www.youtube.com/watch?v=97nlKseDges")

    # Compact Topic 3
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**🌱 Soil Health & Crop Rotation**  \nRotate crops like legumes and cereals to maintain biodiversity and enrich soil.")
    with col2:
        st.video("https://www.youtube.com/watch?v=WIfYj1_96R0")

    # Compact Topic 4
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**🌍 Climate Smart Agriculture**  \nUse drought-resistant crops, rainwater harvesting, agroforestry, and smart irrigation.")
    with col2:
        st.video("http://www.youtube.com/watch?v=pEWJ69SEb6Q")

    # Types of Organic Farming - List
    st.markdown("**🧬 Types of Organic Farming**")
    st.markdown("""
- **Pure Organic Farming** – Only natural inputs like compost and green manure  
- **Integrated Organic Farming** – Mixes crops, animals, and recycling  
- **Permaculture** – Mimics natural ecosystems  
- **Biodynamic Farming** – Uses lunar calendar; treats farm as a living organism  
- **Natural Farming** – 'Zero Budget Farming' by Subhash Palekar
""")

    st.markdown("[🌐 Learn more on FAO Organic Agriculture](https://www.fao.org/organic-agriculture/en/)")



# Post a Product
elif menu == "Post a Product":
    st.header("🧺 Post Your Organic Product")
    with st.form("product_form"):
        name = st.text_input("Product Name")
        desc = st.text_area("Product Description")
        price = st.number_input("Price (₹)", min_value=1)
        submitted = st.form_submit_button("Post Product")
        if submitted and name and desc:
            st.session_state.products.append({"name": name, "desc": desc, "price": price})
            st.success("✅ Product posted successfully!")

# Marketplace
elif menu == "Marketplace":
    st.header("🛒 Organic Marketplace")
    if st.session_state.products:
        for item in st.session_state.products:
            with st.expander(f"{item['name']} - ₹{item['price']}"):
                st.write(item['desc'])
    else:
        st.info("No products available yet. Be the first to post!")

# Community Forum
elif menu == "Community Forum":
    st.header("💬 Community Forum")
    with st.form("forum_form"):
        user = st.text_input("Your Name")
        post = st.text_area("Ask a question or share something")
        post_submit = st.form_submit_button("Post")
        if post_submit and user and post:
            st.session_state.forum_posts.append({"user": user, "post": post})
            st.success("✅ Post submitted!")

    for fpost in reversed(st.session_state.forum_posts):
        st.markdown(f"**{fpost['user']} says:** {fpost['post']}")
        st.markdown("---")

# Loan/Donation Assistance
elif menu == "Loan/Donation Assistance":
    st.header("💰 Apply for Loan / Request Donation")
    with st.form("loan_form"):
        fname = st.text_input("Full Name")
        purpose = st.text_area("Purpose of Loan/Donation")
        amount = st.number_input("Amount Needed (₹)", min_value=100)
        loan_submit = st.form_submit_button("Apply")
        if loan_submit and fname and purpose:
            st.success(f"✅ Application submitted for ₹{amount}. We will reach out to {fname} soon.")
