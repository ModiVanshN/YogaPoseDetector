import cv2
import mediapipe as mp
from timer import Timer
import numpy as np

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

def classify_pose(landmarks):
    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                     landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, 
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, 
                  landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, 
                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, 
                 landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
    right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, 
                   landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

    left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
                  landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
                  landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, 
                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
    right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, 
                   landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
    
    left_leg_angle = calculate_angle(left_shoulder, left_hip, left_ankle)
    right_leg_angle = calculate_angle(right_shoulder, right_hip, right_ankle)
    left_arm_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
    right_arm_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

    # Check if the arms are raised
    hands_raised = left_wrist[1] < left_shoulder[1] and right_wrist[1] < right_shoulder[1]

    # Asana classification
    if (left_leg_angle > 170 and right_leg_angle > 170 and 
        left_arm_angle > 160 and right_arm_angle > 160 and hands_raised):
        return "Tadasana (Mountain Pose)"
    elif (left_leg_angle < 100 and right_leg_angle < 100):
        return "Utkatasana (Chair Pose)"
    elif (left_leg_angle > 150 and right_leg_angle > 150 and
          left_arm_angle > 170 and right_arm_angle > 170 and not hands_raised):
        return "Savasana (Corpse Pose)"
    elif (left_leg_angle > 140 and right_leg_angle > 140 and
          left_arm_angle < 90 and right_arm_angle < 90):
        return "Virabhadrasana I (Warrior I Pose)"
    elif (left_leg_angle > 140 and right_leg_angle > 140 and
          left_arm_angle > 140 and right_arm_angle > 140):
        return "Virabhadrasana II (Warrior II Pose)"
    elif (left_leg_angle < 90 and right_leg_angle > 150 and
          left_arm_angle > 150 and right_arm_angle < 90):
        return "Virabhadrasana III (Warrior III Pose)"
    elif (left_leg_angle > 150 and right_leg_angle > 150 and
          left_arm_angle < 80 and right_arm_angle > 170):
        return "Vrksasana (Tree Pose)"
    elif (left_leg_angle < 90 and right_leg_angle > 150 and
          left_arm_angle > 150 and right_arm_angle > 170):
        return "Trikonasana (Triangle Pose)"
    elif (left_leg_angle > 140 and right_leg_angle > 140 and
          left_arm_angle > 150 and right_arm_angle < 90):
        return "Bhujangasana (Cobra Pose)"
    elif (left_leg_angle > 140 and right_leg_angle > 140 and
          left_arm_angle < 90 and right_arm_angle > 150):
        return "Adho Mukha Svanasana (Downward Dog Pose)"
    else:
        return "Pose not recognized"

def detect_pose(timer):
    cap = cv2.VideoCapture(0)
    
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            print("Frame captured:", ret)
            if not ret:
                print("Failed to grab frame")
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                
                landmarks = results.pose_landmarks.landmark
                pose_name = classify_pose(landmarks)
                
                cv2.putText(image, pose_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                
                # Display timer
                elapsed_time = timer.get_elapsed_time()
                cv2.putText(image, f'Time: {elapsed_time:.2f}s', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            else:
                cv2.putText(image, "Please show your whole body", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
            ret, buffer = cv2.imencode('.jpg', image)
            image = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
    
    cap.release()
