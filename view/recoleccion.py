# librerias
import cv2
import numpy
import mediapipe
import os
# import face_recognition
import math
# import pilow
import imutils
from tkinter import *
from PIL import Image,ImageTk


OutFolderPathUser = 'C:/Users/crist/OneDrive/Documents/GitHub/paginaAlcaldia/database/user'
OutFolderPathFace = 'C:/Users/crist/OneDrive/Documents/GitHub/paginaAlcaldia/database/face'

info = []

pantalla = Tk()
pantalla.geometry("1280x720")
pantalla.title("Reconociomiento Granada")
pantalla.mainloop()