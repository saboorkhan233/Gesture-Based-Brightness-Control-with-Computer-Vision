# Gesture-Based Brightness Control with Computer Vision  

Adjust your device's screen brightness intuitively using just hand gestures! This mini-project leverages **Computer Vision** to track hand movements and dynamically control brightness based on the distance between your thumb and index finger.  

---

## 🚀 Features  
- **Real-time Hand Tracking**: Utilizes **MediaPipe Hands** for precise gesture recognition.  
- **Dynamic Brightness Control**: Adjusts screen brightness based on fingertip distance.  
- **User-Friendly Interface**: Provides visual feedback with annotated live video.  

---

## 🛠️ Technologies and Libraries Used  
- **OpenCV**: For video capture and visualization.  
- **MediaPipe**: For real-time hand tracking and gesture detection.  
- **Screen Brightness Control**: For dynamically adjusting device brightness.  
- **NumPy** and **Math**: For efficient data processing and calculations.  

---

## 🧠 How It Works  
1. **Hand Detection**:  
   - MediaPipe tracks hand landmarks in real time.  
   - Detects thumb and index finger tips for further processing.  

2. **Distance Calculation**:  
   - Computes the Euclidean distance between the thumb and index finger tips.  

3. **Brightness Adjustment**:  
   - Normalizes the distance to a percentage (0–100%).  
   - Adjusts device brightness using the **Screen Brightness Control** library.  

4. **Live Feedback**:  
   - Displays the distance and brightness level on the video feed for better interaction.  

---

## 📜 Usage  

### Prerequisites  
- Python 3.7 or higher  
- A webcam-enabled device  

### Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/gesture-brightness-control.git  
   cd gesture-brightness-control  
Running the Project
Run the Python script to start the application:

## Main File:
python main.py  
Press 'q' to quit the application

## 💻 Learn More
Check out the full project implementation and code in the repository to explore how gestures redefine human-computer interaction.

## 🔗 Connect
Feel free to connect with me on LinkedIn(www.linkedin.com/in/saboor-tahir-a323b7247) or explore more of my projects on GitHub(https://github.com/saboorkhan233).
