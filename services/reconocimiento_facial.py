import cv2
import os

def capture_facial_image():
    # Configura la cámara
    cap = cv2.VideoCapture(0)

    # Captura un fotograma
    ret, frame = cap.read()

    # Comprueba si la captura fue exitosa
    if ret:
        image_path = 'C:/Users/crist/OneDrive/Documents/GitHub/paginaAlcaldia/DataBase/face'  # Ruta donde se guardará la imagen
        cv2.imwrite(image_path, frame)
        return image_path
    else:
        return None
    
def compare_facial_images(image_path1, image_path2):
    # Carga las imágenes desde los archivos
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    if image1 is None or image2 is None:
        return False  # No se pudieron cargar las imágenes

    # Convierte las imágenes a escala de grises para la comparación
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Realiza la comparación de imágenes utilizando el algoritmo de coincidencia
    # Puedes ajustar los parámetros según tus necesidades
    # En este ejemplo, se utiliza el algoritmo TM_CCOEFF_NORMED
    result = cv2.matchTemplate(gray_image1, gray_image2, cv2.TM_CCOEFF_NORMED)

    # Define un umbral de similitud, puedes ajustar este valor según tus necesidades
    similarity_threshold = 0.8

    # Compara el resultado con el umbral de similitud
    if cv2.minMaxLoc(result)[1] >= similarity_threshold:
        return True  # Las imágenes son similares
    else:
        return False  # Las imágenes no son lo suficientemente similares
