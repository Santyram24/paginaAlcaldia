# Usa la imagen base de Python
FROM python:3.11.3

# Establece el directorio de trabajo en el contenedor
WORKDIR C:\\Users\\jddur\\OneDrive\\Documentos\\GitHub\\paginaAlcaldia

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

