import cv2
import mediapipe as mp
import math
import time
from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np

class GestureAnalyzer(QThread):
    processed_image_signal = pyqtSignal(object)
    result_str_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.running = True
        self.capture = cv2.VideoCapture(0)  # 使用攝像頭進行捕捉
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.last_gesture = None
        self.last_time = 0

    def vector_2d_angle(self, v1, v2):
        v1_x = v1[0]
        v1_y = v1[1]
        v2_x = v2[0]
        v2_y = v2[1]
        try:
            angle_ = math.degrees(math.acos((v1_x*v2_x + v1_y*v2_y) / (((v1_x**2 + v1_y**2)**0.5) * ((v2_x**2 + v2_y**2)**0.5))))
        except:
            angle_ = 180
        return angle_

    # 根據傳入的 21 個節點座標，得到該手指的角度
    def hand_angle(self, hand_):
        angle_list = []
        # thumb 大拇指角度
        angle_ = self.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[2][0])), (int(hand_[0][1])- int(hand_[2][1]))),
            ((int(hand_[3][0])- int(hand_[4][0])), (int(hand_[3][1])- int(hand_[4][1])))
        )
        angle_list.append(angle_)
        # index 食指角度
        angle_ = self.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[6][0])), (int(hand_[0][1])- int(hand_[6][1]))),
            ((int(hand_[7][0])- int(hand_[8][0])), (int(hand_[7][1])- int(hand_[8][1])))
        )
        angle_list.append(angle_)
        # middle 中指角度
        angle_ = self.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[10][0])), (int(hand_[0][1])- int(hand_[10][1]))),
            ((int(hand_[11][0])- int(hand_[12][0])), (int(hand_[11][1])- int(hand_[12][1])))
        )
        angle_list.append(angle_)
        # ring 無名指角度
        angle_ = self.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[14][0])), (int(hand_[0][1])- int(hand_[14][1]))),
            ((int(hand_[15][0])- int(hand_[16][0])), (int(hand_[15][1])- int(hand_[16][1])))
        )
        angle_list.append(angle_)
        # pink 小拇指角度
        angle_ = self.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[18][0])), (int(hand_[0][1])- int(hand_[18][1]))),
            ((int(hand_[19][0])- int(hand_[20][0])), (int(hand_[19][1])- int(hand_[20][1])))
        )
        angle_list.append(angle_)
        return angle_list

    def get_thumb_direction(self, finger_points):
        # 取得大拇指的起始點和結束點
        thumb_start = finger_points[0]
        thumb_end = finger_points[4]

        # 計算大拇指的向量
        thumb_vector = (thumb_end[0] - thumb_start[0], thumb_end[1] - thumb_start[1])

        # 根據大拇指的向量判斷方向
        if abs(thumb_vector[0]) > abs(thumb_vector[1]):  # 水平較大
            if thumb_vector[0] > 0:
                return "Right"
            else:
                return "Left"
        else: 
            if thumb_vector[1] > 0:
                return "Down"
            else:
                return "Up"
                
    def hand_pos(self, finger_points,finger_angle):
        f1 = finger_angle[0]   # 大拇指角度
        f2 = finger_angle[1]   # 食指角度
        f3 = finger_angle[2]   # 中指角度
        f4 = finger_angle[3]   # 無名指角度
        f5 = finger_angle[4]   # 小拇指角度

        # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
        if f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
            return self.get_thumb_direction(finger_points)
        elif f1 >= 50 and f2 >= 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
            return "Don't Be Rude!!!"
        elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
            return 'Rock!'
        elif f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
            return '0'
        elif f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
            return 'Pinky'
        elif f1 >= 50 and f2 < 50 and f3 >= 50 and f4 < 50 and f5 < 50:
            return 'Lotus'
        elif f1 >= 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
            return '1'
        elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
            return '2'
        elif f1 >= 50 and f2 >= 50 and f3 < 50 and f4 < 50 and f5 < 50:
            return 'ok'
        elif f1 < 50 and f2 >= 50 and f3 < 50 and f4 < 50 and f5 < 50:
            return 'ok'
        elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 > 50:
            return '3'
        elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
            return '4'
        elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
            return '5'
        elif f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
            return '6'
        elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
            return '7'
        elif f1 < 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
            return '8'
        elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 >= 50:
            return '9'
        else:
            return ''

    def add_mosaic_on_middle_finger(self, finger_points):
        finger_points_np = np.array(finger_points)
        x_max = np.max(finger_points_np[:, 0]) + 20
        y_max = np.max(finger_points_np[:, 1]) + 20
        x_min = np.min(finger_points_np[:, 0]) - 20
        y_min = np.min(finger_points_np[:, 1]) - 20
        
        # 加入檢查邊界
        x_max = min(x_max, w)  # w 是圖片的寬度
        y_max = min(y_max, h)  # h 是圖片的高度
        x_min = max(x_min, 0)  # 確保 x_min 不會小於 0
        y_min = max(y_min, 0)  # 確保 y_min 不會小於 0
        
        # 計算馬賽克的寬高
        mosaic_w = x_max - x_min
        mosaic_h = y_max - y_min
        
        # 如果這個區域的寬度或高度為 0，則跳過
        if mosaic_w <= 0 or mosaic_h <= 0:
            return

        # 切割出區域並縮放
        mosaic = img[y_min:y_max, x_min:x_max]
        
        if mosaic.size == 0:  # 確保切割區域有效
            return

        # 縮放至 8x8
        mosaic = cv2.resize(mosaic, (8, 8), interpolation=cv2.INTER_LINEAR)

        # 再縮放回原始區域大小
        mosaic = cv2.resize(mosaic, (mosaic_w, mosaic_h), interpolation=cv2.INTER_NEAREST)

        # 替換回原圖
        img[y_min:y_max, x_min:x_max] = mosaic
    
    def run(self):
        with self.mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.5) as hands:

            while self.running:
                ret, frame = self.capture.read()
                if not ret:
                    continue
                global img
                img = cv2.flip(frame, 1)
                img = cv2.resize(img, (500, 300)) 
                global h, w
                h, w, _ = img.shape
                img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = hands.process(img2)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            img,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())

                        finger_points = []
                        for i in hand_landmarks.landmark:
                            x = int(i.x * w)
                            y = int(i.y * h)
                            finger_points.append((x, y))

                        if finger_points:
                            finger_angle = self.hand_angle(finger_points)
                            text = self.hand_pos(finger_points, finger_angle)
                            if text == "Don't Be Rude!!!":
                                self.add_mosaic_on_middle_finger(finger_points)
                                self.result_str_signal.emit(text)
                            if text == self.last_gesture:
                                if time.time() - self.last_time > 2:
                                    self.result_str_signal.emit(text)
                                    self.last_time = time.time()
                            else:
                                self.last_gesture = text
                                self.last_time = time.time()
                                
                self.processed_image_signal.emit(img)

    def stop(self):
        self.running = False
        self.capture.release()
        self.wait()
