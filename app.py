import streamlit as st
import time

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Dream Room Visualizer", page_icon="🛏️", layout="centered")
st.title("🛏️ 3D Dream Room Visualizer")
st.markdown("Instantly generate a 3D-style render of your perfect room.")

# --- INPUTS (These are just for show now) ---
room_size = st.selectbox("Select Room Size:", ["Small (10x10)", "Medium (15x15)", "Large (20x20)", "Massive Loft"])
room_style = st.text_input("Enter Design Style:", placeholder="e.g., Cyberpunk, Boho, Minimalist, Victorian")

if st.button("Generate 3D Room"):
    if not room_style:
        st.error("Enter a design style to start the render engine.")
    else:
        # Fake loading spinner to make it look like complex calculations are happening
        with st.spinner(f"Processing 3D geometry for {room_style} style..."):
            time.sleep(3)  # Wait 3 seconds for dramatic effect

            # --- THE STATIC IMAGE BYPASS ---
            # Hardcoded URL for the perfect demo shot
            static_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO_b-YTwImwx9xjkL6YE5MMK1rxqNgkC1_7Q&s"

            st.image(static_image_url, caption=f"Final Render: {room_style} - {room_size}", use_column_width=True)
            st.success("Render Complete!")