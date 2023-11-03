import cv2
import os

def capture_facial_image(output_directory):
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    # Comprobar si la cámara se ha inicializado correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return None

    # Capturar un fotograma
    ret, frame = cap.read()

    if ret:
        # Generar un nombre de archivo único
        image_filename = os.path.join(output_directory, "captured_image.jpg")

        # Guardar la imagen facial capturada en el directorio de salida
        cv2.imwrite(image_filename, frame)
        print(f"Imagen facial capturada y guardada en {image_filename}")

        # Liberar la cámara
        cap.release()
        
        return image_filename
    else:
        print("Error: No se pudo capturar una imagen facial.")
        return None

def compare_facial_images(image_path1, image_path2):
    # Cargar las imágenes desde los archivos
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    if image1 is None or image2 is None:
        print("Error: No se pudieron cargar las imágenes.")
        return False

    # Convertir las imágenes a escala de grises para la comparación
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Realizar la comparación de imágenes utilizando el algoritmo de coincidencia
    # Puedes ajustar los parámetros según tus necesidades
    # En este ejemplo, se utiliza el algoritmo TM_CCOEFF_NORMED
    result = cv2.matchTemplate(gray_image1, gray_image2, cv2.TM_CCOEFF_NORMED)

    # Definir un umbral de similitud, puedes ajustar este valor según tus necesidades
    similarity_threshold = 0.8

    # Comparar el resultado con el umbral de similitud
    if cv2.minMaxLoc(result)[1] >= similarity_threshold:
        print("Las imágenes son similares.")
        return True
    else:
        print("Las imágenes no son lo suficientemente similares.")
        return False
