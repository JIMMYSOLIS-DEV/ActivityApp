import streamlit as st
import cv2
import numpy as np

# Set up the Streamlit app title
st.title("Real-time Video Capture with OpenCV")

# Start the webcam capture
cap = cv2.VideoCapture(0)  # 0 is the default camera

# Ensure the webcam opened successfully
if not cap.isOpened():
    st.error("Could not open webcam")
else:
    st.write("Press the button below to start/stop the webcam feed.")

    # Placeholder for the video frame display
    frame_placeholder = st.empty()

    # State management for the video feed
    video_feed_active = st.session_state.get("video_feed_active", False)

    # Create a button to start/stop the webcam feed
    stop_button = st.button("Stop Video Feed" if video_feed_active else "Start Video Feed")

    # Toggle the video feed state
    if stop_button:
        video_feed_active = not video_feed_active
        st.session_state["video_feed_active"] = video_feed_active

    if video_feed_active:
        # Capture and display video
        while video_feed_active:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to grab frame")
                break

            # Convert the frame to RGB (OpenCV uses BGR by default)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the frame using Streamlit's st.image
            frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

            # Check the button state again in each loop to update it
            stop_button = st.button("Stop Video Feed", key=f"stop_button_{np.random.randint(1, 100000)}")
            if stop_button:
                video_feed_active = False
                st.session_state["video_feed_active"] = False
                break

    # Release the capture object when done
    cap.release()
