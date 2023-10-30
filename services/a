import cv2
import dlib
import numpy as np

predictor_path = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

image = cv2.imread("person.jpg")

dets = detector(image, 1)
for k, d in enumerate(dets):
    shape = predictor(image, d)
    points = np.empty([68, 2], dtype=int)
    for i in range(68):
        points[i] = (shape.part(i).x, shape.part(i).y)
    for p in range(68):
        cv2.circle(image, (points[p][0], points[p][1]), 1, (0, 255, 0), -1, 8, 0)


cv2.imshow("Fa")