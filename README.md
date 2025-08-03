
# 🔍 Algoritmos de Búsqueda - Visualización con Flask

Este proyecto implementa dos algoritmos de búsqueda: **Búsqueda Secuencial** y **Búsqueda Binaria**, utilizando Flask y Bootstrap para representar visualmente cada paso de los algoritmos.

Es ideal para aprender o enseñar cómo trabajan internamente estos algoritmos de una manera clara, animada e interactiva.

---

## 📋 Información general:

- **Materia:** Estructura de Datos  
- **Profesor:** Kevin David Molina Gómez  
- **Fecha de entrega:** 02/08/2025  

### 🧑‍🤝‍🧑 Integrantes del equipo:
- Carlos Antonio Cortes Torres  
- Luis Alberto Figueroa González  
- Sergio Alexander Antonio Gracida   
- Arath Yahir López Guzmán  
- Oswaldo Martínez Vidaña  
- Ángel David García Blas  

---

## ❓ ¿Qué hace este proyecto?

Implementa dos algoritmos clásicos de búsqueda:

- **Búsqueda Secuencial:** Recorre todos los elementos hasta encontrar el valor.
- **Búsqueda Binaria:** Divide la lista ordenada en mitades para encontrar el valor eficientemente.

Ambos algoritmos se muestran visualmente en tablas con colores y resultados detallados del proceso de búsqueda.

---

## 🧠 ¿Cómo funciona?

1. Se genera una lista aleatoria de números.
2. El usuario ingresa un valor a buscar.
3. El algoritmo recorre o divide la lista para encontrar el elemento.
4. Cada paso se muestra visualmente con una tabla y colores.
5. Se informa si se encontró el valor, su posición y el número total de pasos.

---

## ⚙️ ¿Cómo ejecutar el código?

1. Asegúrate de tener Python 3.8+ instalado.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
4. Abre tu navegador y accede a:  
   [http://localhost:5000](http://localhost:5000)

---

## 🧾 Estructura del proyecto

```
├── app.py                      # Aplicación principal Flask
├── algoritmos_busqueda.py     # Módulo con la lógica de los algoritmos
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Este archivo
└── templates/                 # Plantillas HTML con Bootstrap
    ├── base.html
    ├── index.html
    ├── busqueda_secuencial.html
    └── busqueda_binaria.html
```

---

## 📸 Capturas de pantalla

### Menú Principal
![Menú Principal](https://github.com/CarlosTorres137/Tema-6/blob/830a2a58f1294b76ee696ed6980b9012c433c1d0/Menu%20Principal.png)

---

### Búsqueda Secuencial
![Búsqueda Secuencial](![alt text])

---

### Búsqueda Binaria
![Búsqueda Binaria](![alt text])

---
