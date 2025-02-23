<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Yoga Pose Detector</title>
</head>
<body>
    <h1>🧘 Yoga Pose Detector</h1>
    <p>Welcome to the Yoga Pose Detector project! This application leverages computer vision and machine learning to identify various yoga poses in real-time using OpenCV, MediaPipe, and Flask.</p>
    <h2>📚 Project Overview</h2>
    <p>The Yoga Pose Detector provides an interactive experience to help users improve their yoga practice by identifying and tracking the duration of specific yoga poses. The system supports multiple yoga poses and offers a user-friendly web interface.</p>
<h2>✨ Features</h2>
    <ul>
        <li>Real-time yoga pose detection 🕒</li>
        <li>Support for multiple yoga poses 🧘‍♀️</li>
        <li>Timer functionality to track the duration of poses ⏱️</li>
        <li>User-friendly web interface 🌐</li>
    </ul>
    
 <h2>📂 Directory Structure</h2>
    <pre>
YogaPoseDetector/
├── app.py
├── static/
│   ├── styles.css
│   └── yoga.jpg
├── templates/
│   ├── index.html
│   └── home.html
├── pose_detector.py
└── timer.py
    </pre>
    
 <h2>⚙️ Setup and Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone &lt;repository_url&gt;</code></pre>
        <li>Navigate to the project directory:</li>
        <pre><code>cd YogaPoseDetector</code></pre>
        <li>Install the required libraries:</li>
        <pre><code>pip install opencv-python mediapipe flask numpy</code></pre>
    </ol>
    
<h2>🚀 Running the Application</h2>
    <ol>
        <li>Navigate to the project directory:</li>
        <pre><code>cd YogaPoseDetector</code></pre>
        <li>Run the Flask application:</li>
        <pre><code>python app.py</code></pre>
        <li>Open your web browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> to see the homepage.</li>
        <li>Click the "Start Yoga Pose Detector" button or use the navbar to access the Yoga Pose Detector.</li>
    </ol>
    
<h2>📌 Usage</h2>
    <p>On the homepage, you can find an overview of the project. Click the "Start Yoga Pose Detector" button to access the Yoga Pose Detector.</p>
    <ul>
        <li>Video Feed: The video feed from your webcam should appear on the webpage. 📷</li>
        <li>Start Timer: Click the "Start Timer" button to start the timer when you begin a pose. 🕒</li>
        <li>Stop Timer: Click the "Stop Timer" button to stop the timer when you finish a pose. 🛑</li>
        <li>Switch Asanas: Use the dropdown menu to switch between different asanas. The application will detect and display the name of the asana you're performing. ↔️</li>
    </ul>
    
<h2>🤝 Contributing</h2>
    <p>Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.</p>
    
<h2>📜 License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
