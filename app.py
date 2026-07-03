"""
Tienda de servicios digitales - versión Python (Flask)
=======================================================
Mismo sitio que ya tenías en HTML/JS, pero ahora los datos editables
(negocio, servicios, testimonios) viven aquí, en Python.

Cómo correrlo:
    pip install flask
    python app.py
Luego abre http://127.0.0.1:5000 en tu navegador.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)

# ======================================================================
# 1. EDITA AQUÍ -> DATOS DEL NEGOCIO
# ======================================================================
NEGOCIO = {
    "nombre": "Precios Competitivos",
    "whatsapp": "51924481118",      # código de país + número, sin + ni espacios
    "yapePhone": "924 481 118",     # número que se muestra para yapear manualmente
    "instagram": "https://instagram.com/tunegocio",
    "facebook": "https://facebook.com/tunegocio",
}

# ======================================================================
# 2. EDITA AQUÍ -> TUS SERVICIOS
# Agrega, quita o modifica los diccionarios de esta lista. Cada uno
# genera automáticamente una tarjeta en la sección "Catálogo".
# ======================================================================
SERVICIOS = [
    {
        "nombre": "NETFLIX",
        "precio": 14.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Películas y series ilimitadas.\n✔ Estrenos exclusivos.\n✔ Perfiles personalizados.\n✔ Disponible en todos tus dispositivos.\n✔ Calidad HD/Full HD/4K (según el plan).\n✔ Contenido para toda la familia.",
        "imagen": "images/netflix1.jpg",
        "use_as_background": True,
    },
    {
        "nombre": "DISNEY PREMIUN",
        "precio": 11.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Películas y series de Disney, Pixar, Marvel y Star Wars.\n✔ Contenido para toda la familia.\n✔ Estrenos exclusivos.\n✔ Calidad HD y 4K (según el plan).",
        "imagen": "images/disney.jpg",
    },
    {
        "nombre": "PRIME VIDEO",
        "precio": 5.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Series y películas exclusivas de Amazon.\n✔ Estrenos frecuentes.\n✔ Contenido internacional.\n✔ Disponible en múltiples dispositivos.",
        "imagen": "images/PRIME VIDEO.png",
    },
    {
        "nombre": "HBO MAX",
        "precio": 7.00,
        "entrega": "Entrega en 24h",
        "desc": "✔ Series originales de HBO.\n✔ Películas taquilleras.\n✔ Universo DC y Warner Bros.\n✔ Estrenos exclusivos.",
        "imagen": "images/hbomax.jpg",
    },
    {
        "nombre": "CRUNCHYROLL",
        "precio": 5.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Miles de episodios de anime.\n✔ Estrenos en simulcast.\n✔ Subtítulos en español.\n✔ Amplio catálogo de anime.",
        "imagen": "images/CRUNCHYROLL1.png",
    },
    {
        "nombre": "SPOTIFY",
        "precio": 9.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Música sin anuncios.\n✔ Descargas para escuchar sin internet.\n✔ Saltos ilimitados.\n✔ Máxima calidad de audio.",
        "imagen": "images/spotify1.png",
    },
    {
        "nombre": "VIX PREMIUN",
        "precio": 4.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Series y películas en español.\n✔ Deportes en vivo (según disponibilidad).\n✔ Novelas y contenido exclusivo.\n✔ Sin anuncios en contenido Premium.",
        "imagen": "images/VIX PREMIUN.jpg",
    },
    {
        "nombre": "DGO-MUNDIAL",
        "precio": 19.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Partidos en vivo.\n✔ Canales deportivos premium.\n✔ Cobertura completa del Mundial.\n✔ Acceso desde cualquier dispositivo.",
        "imagen": "images/DGO-MUNDIAL.png",
    },
    {
        "nombre": "CANVA PRO",
        "precio": 3.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Millones de plantillas premium.\n✔ Herramientas de IA para diseño.\n✔ Fondo transparente y redimensionado mágico.\n✔ Recursos gráficos e imágenes premium.",
        "imagen": "images/canva1.png",
    },
    {
        "nombre": "CHATGPT PLUS",
        "precio": 13.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Dispositivo - Se Brinda Correo y Contraseña Listo para Usar\n✔ Garantía Por 30 días",
        "imagen": "images/chatgpt",
    },
    {
        "nombre": "GEMINI PRO",
        "precio": 9.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Se activa A tu Correo 💌\n✔ Garantía por 30 días",
        "imagen": "images/geminipro",
    }
]

# ======================================================================
# 3. EDITA AQUÍ -> TESTIMONIOS
# ======================================================================
TESTIMONIOS = [
    {
        "texto": "Al principio dudaba por los precios tan bajos, pero la cuenta de Netflix me llegó al toque por WhatsApp. Ya llevo 3 meses renovando con ellos y cero caídas. Totalmente recomendado.",
        "autor": "Renzo Benavides",
        "estrellas": 5,
    },
    {
        "texto": "Excelente servicio! Compré el combo de Disney+ y Prime Video para mis hijos. La atención es súper amable y la entrega fue instantánea. Me ahorro un montón de plata al mes.",
        "autor": "Fiorella Cárdenas",
        "estrellas": 5,
    },
    {
        "texto": "Lo máximo. Estaba buscando dónde ver el partido el fin de semana y me salvaron con una cuenta al instante. El soporte responde rápido si tienes dudas. 10 de 10.",
        "autor": "Giancarlo Espinoza",
        "estrellas": 5,
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        negocio=NEGOCIO,
        servicios=SERVICIOS,
        testimonios=TESTIMONIOS,
        negocio_json=json.dumps(NEGOCIO),
        servicios_json=json.dumps(SERVICIOS),
        testimonios_json=json.dumps(TESTIMONIOS),
    )


if __name__ == "__main__":
    app.run(debug=True)
