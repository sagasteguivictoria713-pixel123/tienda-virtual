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
        "nombre": "NETFLIX PREMIUN",
        "tipo": "perfil",
        "precio": 14.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Películas, series y producciones exclusivas de Netflix.\n✔ Descarga tus títulos favoritos y míralos sin conexión.\n✔ Calidad de video hasta 4K Ultra HD + HDR.\n✔ Audio espacial disponible en títulos compatibles.",
        "imagen": "images/netflix1.jpg",
        "use_as_background": True,
    },
    {
        "nombre": "DISNEY PREMIUN",
        "tipo": "perfil",
        "precio": 9.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Canales de ESPN y deportes en vivo.\n✔ Películas y series de Disney, Pixar, Marvel y Star Wars.\n✔ Calidad de video hasta 4K UHD y HDR.\n✔ Descarga contenido para verlo sin conexión.",
        "imagen": "images/disneypremiun.jpg",
    },
    {
        "nombre": "DISNEY STANDARD",
        "tipo": "perfil",
        "precio": 7.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Películas y series de Disney, Pixar, Marvel y Star Wars.\n✔ Descarga contenido y disfruta sin conexión.\n✔ Calidad de video hasta Full HD 1080p.\n✔ No incluye los canales de ESPN disponibles en Disney+ Premium.",
        "imagen": "images/disneystandard.jpg",
    },
    {
        "nombre": "PRIME VIDEO",
        "tipo": "perfil",
        "precio": 5.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Películas, series y producciones Amazon Original.\n✔ Descarga contenido y disfruta sin conexión.\n✔ Calidad de video HD y Ultra HD en dispositivos compatibles.\n✔ Disponible en Smart TV, celular, tablet y computadora.",
        "imagen": "images/primevideo.jpg",
    },
    {
        "nombre": "HBO MAX",
        "tipo": "perfil",
        "precio": 6.50,
        "entrega": "Entrega en 24h",
        "desc": "✔ Series originales de HBO.\n✔ Películas taquilleras.\n✔ Universo DC y Warner Bros.\n✔ Estrenos exclusivos.",
        "imagen": "images/hbo.jpg",
    },
    {
        "nombre": "CRUNCHYROLL",
        "tipo": "perfil",
        "precio": 5.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Miles de episodios de anime.\n✔ Estrenos en simulcast.\n✔ Subtítulos en español.\n✔ Amplio catálogo de anime.",
        "imagen": "images/CRUNCHYROLL1.png",
    },
    {
        "nombre": "SPOTIFY PREMIUN",
        "tipo": "perfil",
        "precio": 9.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Música sin anuncios.\n✔ Descargas para escuchar sin internet.\n✔ Saltos ilimitados.\n✔ Máxima calidad de audio.",
        "imagen": "images/spotify1.png",
    },
    {
        "nombre": "YOUTUBE PREMIUN 12 MESES",
        "tipo": "perfil",
        "precio": 150.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Entregamos correo y contraseña listos para usar.\n✔ Disfruta videos y música sin anuncios.\n✔ Descarga contenido y míralo sin conexión.\n✔ Reproducción en segundo plano con YouTube Music Premium.",
        "imagen": "images/youtube.jpg",
    },
    {
        "nombre": "VIX PREMIUN",
        "tipo": "perfil",
        "precio": 3.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Series y películas en español.\n✔ Deportes en vivo (según disponibilidad).\n✔ Novelas y contenido exclusivo.\n✔ Sin anuncios en contenido Premium.",
        "imagen": "images/VIX PREMIUN.jpg",
    },
    {
        "nombre": "PARAMOUNT+",
        "tipo": "perfil",
        "precio": 8.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Películas taquilleras y series originales.\n✔ Contenido de Nickelodeon, MTV, Comedy Central y más.\n✔ Mira en TV, celular, tablet y computadora.\n✔ Descarga títulos y disfruta sin conexión.",
        "imagen": "images/paramount.jpg",
    },
    {
        "nombre": "CANVA PRO",
        "tipo": "perfil",
        "precio": 3.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Millones de plantillas premium.\n✔ Herramientas de IA para diseño.\n✔ Fondo transparente y redimensionado mágico.\n✔ Recursos gráficos e imágenes premium.",
        "imagen": "images/canva1.png",
    },
    {
        "nombre": "CAPCUT PRO",
        "tipo": "perfil",
        "precio": 12.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Plantillas, efectos y recursos Premium exclusivos.\n✔ Herramientas avanzadas de IA para edición de video.\n✔ Exportación en 4K y videos sin marca de agua.\n✔ Edición en móvil, PC y web con almacenamiento en la nube.",
        "imagen": "images/capcutpro.jpg",
    },
    {
        "nombre": "MICROSOFT 365",
        "tipo": "perfil",
        "precio": 25.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Word, Excel, PowerPoint y Outlook incluidos.\n✔ Almacenamiento seguro en la nube con OneDrive.\n✔ Acceso desde PC, Mac, celular y tablet.\n✔ Herramientas de IA con Microsoft Copilot.",
        "imagen": "images/microsoft365.jpg",
    },
    {
        "nombre": "CHATGPT PLUS",
        "tipo": "perfil",
        "precio": 13.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Se brinda correo y contraseña listo para usar.\n✔ Garantía por 30 días.\n✔ Acceso a modelos avanzados de razonamiento.\n✔ Creación de imágenes y análisis de archivos.",
        "imagen": "images/chatgpt.png",
    },
    {
        "nombre": "GEMINI PRO",
        "tipo": "perfil",
        "precio": 9.50,
        "entrega": "Entrega al instante",
        "desc": "✔ Se activa a tu correo.\n✔ Garantía por 30 días.\n✔ Acceso ampliado al modelo Gemini Pro.\n✔ IA integrada con Gmail, Docs y otras apps de Google.",
        "imagen": "images/geminipro1.jpg",
    },
    # ======================================================================
    # 7 NUEVOS SERVICIOS: CUENTAS COMPLETAS
    # ======================================================================
    {
        "nombre": "DISNEY PREMIUN (Cuenta Completa)",
        "tipo": "cuenta_completa",
        "precio": 15.20,
        "entrega": "Entrega al instante",
        "desc": "✔ Canales de ESPN y deportes en vivo.\n✔ Películas y series de Disney, Pixar, Marvel y Star Wars.\n✔ Calidad de video hasta 4K UHD y HDR.\n✔ Descarga contenido para verlo sin conexión.",
        "imagen": "images/disneypremiun.jpg",
    },
    {
        "nombre": "PRIME VIDEO (Cuenta Completa)",
        "tipo": "cuenta_completa",
        "precio": 8.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Películas, series y producciones Amazon Original.\n✔ Descarga contenido y disfruta sin conexión.\n✔ Calidad de video HD y Ultra HD en dispositivos compatibles.\n✔ Disponible en Smart TV, celular, tablet y computadora.",
        "imagen": "images/primevideo.jpg",
    },
    {
        "nombre": "HBO MAX (Cuenta Completa)",
        "tipo": "cuenta_completa",
        "precio": 10.40,
        "entrega": "Entrega en 24h",
        "desc": "✔ Series originales de HBO.\n✔ Películas taquilleras.\n✔ Universo DC y Warner Bros.\n✔ Estrenos exclusivos.",
        "imagen": "images/hbo.jpg",
    },
    {
        "nombre": "CRUNCHYROLL (Cuenta Completa)",
        "tipo": "cuenta_completa",
        "precio": 8.00,
        "entrega": "Entrega al instante",
        "desc": "✔ Miles de episodios de anime.\n✔ Estrenos en simulcast.\n✔ Subtítulos en español.\n✔ Amplio catálogo de anime.",
        "imagen": "images/CRUNCHYROLL1.png",
    },
    {
        "nombre": "VIX PREMIUN (Cuenta Completa)",
        "tipo": "cuenta_completa",
        "precio": 4.80,
        "entrega": "Entrega al instante",
        "desc": "✔ Series y películas en español.\n✔ Deportes en vivo (según disponibilidad).\n✔ Novelas y contenido exclusivo.\n✔ Sin anuncios en contenido Premium.",
        "imagen": "images/VIX PREMIUN.jpg",
    },
    {
        "nombre": "CAPCUT PRO (Cuenta Completa)",
        "tipo": "cuenta_completa",
        "precio": 19.20,
        "entrega": "Entrega al instante",
        "desc": "✔ Plantillas, efectos y recursos Premium exclusivos.\n✔ Herramientas avanzadas de IA para edición de video.\n✔ Exportación en 4K y videos sin marca de agua.\n✔ Edición en móvil, PC y web con almacenamiento en la nube.",
        "imagen": "images/capcutpro.jpg",
    },
    {
        "nombre": "CHATGPT PLUS (Cuenta Completa)",
        "tipo": "cuenta_completa",
        "precio": 21.60,
        "entrega": "Entrega al instante",
        "desc": "✔ Se brinda correo y contraseña listo para usar.\n✔ Garantía por 30 días.\n✔ Acceso a modelos avanzados de razonamiento.\n✔ Creación de imágenes y análisis de archivos.",
        "imagen": "images/chatgpt.png",
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
