# HERO SECTION - RESUMEN DE ESPECIFICACIONES

## 🎯 COMPONENTES IMPLEMENTADOS

### 1️⃣ BADGE SUPERIOR
```
┌─────────────────────────────────────────┐
│  ◆  TU ENTRETENIMIENTO SIN LÍMITES      │  ← Píldora redondeada
└─────────────────────────────────────────┘
```
- **Ícono**: Diamante (◆)
- **Posición**: Izquierda
- **Fondo**: rgba(73, 226, 182, 0.1) - Semitransparente
- **Borde**: 1px solid rgba(73, 226, 182, 0.3)
- **Border-radius**: 999px
- **Tipografía**: Space Grotesk, 700, 0.85rem, mayúsculas
- **Efecto blur**: backdrop-filter blur(10px)

---

### 2️⃣ TÍTULO PRINCIPAL (H1)
```
Licencias Digitales al
[Mejor Precio]  ← Color acento, con subrayado
```
- **Font**: Space Grotesk
- **Weight**: 700
- **Tamaño**: clamp(2.4rem, 6vw, 3.8rem)
- **Line-height**: 1.15
- **Color base**: #F3ECD8 (crema)
- **Color acento**: #49E2B6 (verde menta)
- **Decoración**: Subrayado degradado en palabra clave
- **Sombra**: 0 8px 24px rgba(0, 0, 0, 0.3)

---

### 3️⃣ SUBTÍTULO
```
Acceso inmediato a tus plataformas favoritas. 
Precios competitivos, entrega al instante y soporte 24/7.
```
- **Font**: Work Sans
- **Tamaño**: 1.08rem
- **Color**: #9FC8E1 (celeste apagado)
- **Line-height**: 1.6
- **Max-width**: 580px
- **Propuesta de valor**: Clara y concisa (1-2 líneas)

---

### 4️⃣ BOTONES CTA (2 EN FILA)

#### PRIMARIO - Ver catálogo
```
┌──────────────────────────┐
│  🛒  Ver catálogo        │  ← Fondo sólido acento
└──────────────────────────┘
```
- **Background**: Gradiente #49E2B6 → #3dce9f
- **Color texto**: #050D24 (oscuro)
- **Padding**: 14px 28px
- **Border-radius**: 12px
- **Ícono**: 🛒 (carrito)
- **Sombra**: 0 12px 32px -8px rgba(73, 226, 182, 0.4)
- **Hover**: translateY(-3px) + sombra aumentada

#### SECUNDARIO - ¿Cómo funciona?
```
┌──────────────────────────┐
│  ▷  ¿Cómo funciona?      │  ← Borde sutil, fondo transparente
└──────────────────────────┘
```
- **Background**: rgba(243, 236, 216, 0.08) (transparente)
- **Borde**: 1.5px solid rgba(73, 226, 182, 0.35)
- **Color texto**: #F3ECD8 (crema)
- **Padding**: 14px 28px
- **Border-radius**: 12px
- **Ícono**: ▷ (play)
- **Hover**: Fondo más opaco + borde más visible + translateY(-3px)

---

### 5️⃣ ESTADÍSTICAS (3 COLUMNAS)
```
18+              24/7             2,521+
PRODUCTOS        ENTREGA DE       VENTAS
                 LICENCIAS

↑ Números: Color acento, font Space Mono, grande
↓ Etiquetas: Gris muted, pequeñas, mayúsculas
```

**Columna 1**: 18+ / PRODUCTOS
**Columna 2**: 24/7 / ENTREGA DE LICENCIAS
**Columna 3**: 2,521+ / VENTAS

- **Números**:
  - Font: Space Mono, 700
  - Tamaño: clamp(1.8rem, 4vw, 2.6rem)
  - Color: #49E2B6 (verde menta)
  
- **Etiquetas**:
  - Font: Space Grotesk, 600
  - Tamaño: 0.75rem
  - Color: #9FC8E1 (celeste apagado)
  - Letter-spacing: 0.08em
  - Text-transform: uppercase
  
- **Layout**: Grid responsive, auto-fit, minmax 140px
- **Gap**: 32px (desktop), 24px (tablet), 16px (mobile)

---

## 🎨 PALETA DE COLORES

| Elemento | Color | Código | Uso |
|----------|-------|--------|-----|
| **Fondo Principal** | Azul Marino Oscuro | #050D24 | Background section |
| **Acento/Highlight** | Verde Menta | #49E2B6 | Palabra clave, números, botón primario |
| **Texto Principal** | Crema | #F3ECD8 | Títulos, botones |
| **Texto Muted** | Celeste Apagado | #9FC8E1 | Subtítulos, etiquetas |
| **Bordes** | Blanco/Crema Transparente | rgba(243,236,216,0.14) | Líneas sutiles |
| **Gradiente Button** | Verde → Verde oscuro | #49E2B6 → #3dce9f | Botón primario |

---

## 🔤 TIPOGRAFÍA

### Fuentes Importadas
```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Work+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

| Elemento | Font | Weight | Tamaño | Letter-spacing |
|----------|------|--------|--------|-----------------|
| **Títulos/Badge/Etiquetas** | Space Grotesk | 700 | Variable | -0.02em / 0.08em |
| **Cuerpo/Subtítulo** | Work Sans | 400-600 | Variable | Normal |
| **Números/Monospace** | Space Mono | 700 | Variable | Normal |

---

## 🎬 ANIMACIONES

### Entrada en Cascada (Fade-In-Up)
```
Badge      ←  0s   ┐
Title      ←  0.1s │
Subtitle   ←  0.2s ├─ Cada 0.1s de delay
Botones    ←  0.3s │
Stats      ←  0.4s ┘

Duración: 0.8s ease-out
Desde: opacity 0 + translateY(20px)
Hacia: opacity 1 + translateY(0)
```

### Hover en Botones
```
Tiempo: 0.3s ease
Efecto: transform translateY(-3px)
        box-shadow aumenta
```

---

## 📐 DIMENSIONES Y ESPACIADO

### Sección General
```
Padding Vertical:   120px (top) × 80px (bottom)
Padding Horizontal: 24px (responsive)
Min-height:         100vh
```

### Espaciado Vertical Interno
```
Badge ↓ (32px)
Title ↓ (20px)
Subtitle ↓ (40px)
Botones ↓ (60px)
Estadísticas
```

### Bordes y Radios
```
Badge border-radius:     999px (píldora)
Button border-radius:    12px (redondeado suave)
Grid background-size:    80px × 80px
```

---

## 🌐 RESPONSIVE BREAKPOINTS

### Desktop (>768px)
- Min-height: 100vh
- Badge: Horizontal
- Title: 2.4rem - 3.8rem
- Stats: 3 columnas, gap 32px
- Buttons: Fila horizontal, gap 16px

### Tablet (768px)
- Min-height: Auto
- Reducciones proporcionales
- Padding: 80px 20px 60px
- Title: Max 2.8rem
- Stats gap: 24px

### Mobile (≤480px)
- Padding: 60px 16px 48px
- Badge: Columnar
- Title: 1.6rem
- Buttons: Stack vertical (100% width)
- Stats: 3 columnas compactas
- Stats gap: 16px

---

## 🖼️ EFECTOS DE FONDO

### Grid Sutil
```css
Linear gradients:
- Eje X: 1px de color, 79px transparente (repetido)
- Eje Y: 1px de color, 79px transparente (repetido)
Opacidad: 0.04 (muy sutil)
Color: #49E2B6 (verde menta)
```

### Gradientes Radiales
```
1. Círculo 15% izq, 20% arriba: 
   rgba(73, 226, 182, 0.15) → transparent a 25%
   
2. Círculo 85% der, 15% arriba:
   rgba(79, 255, 209, 0.12) → transparent a 20%
   
3. Lineal 180deg:
   rgba(5, 13, 36, 0.8) arriba
   → rgba(4, 14, 37, 0.95) abajo
```

---

## ✅ CHECKLIST DE IMPLEMENTACIÓN

- [x] Badge con ícono y texto
- [x] Título H1 con palabra acento destacada
- [x] Subtítulo descriptivo
- [x] Botón primario con gradiente
- [x] Botón secundario con borde
- [x] 3 estadísticas en fila
- [x] Fondo con grid y gradientes
- [x] Animaciones en cascada
- [x] Efectos hover en botones
- [x] Responsive en 3 breakpoints
- [x] Tipografía correcta (Space Grotesk, Work Sans)
- [x] Paleta de colores completa
- [x] Accessible (semántica HTML correcta)

---

## 📋 ARCHIVOS GENERADOS

1. **templates/hero-section.html** - Componente reutilizable
2. **static/hero-demo.html** - Demo standalone
3. **HERO_DOCUMENTATION.md** - Documentación completa
4. **HERO_SPECS.md** - Este archivo (especificaciones)

---

**Diseño completado: 2026-08-15** ✨
