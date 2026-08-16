# Sección Hero Premium - Documentación Técnica

## 📋 Visión General
Sección hero profesional y moderna diseñada para un sitio de venta de licencias digitales. Incluye estructura visual jerárquica clara con componentes interactivos.

---

## 🎨 Componentes Principales

### 1. **Badge Superior**
```html
<div class="hero-badge">
  <span class="badge-icon">◆</span>
  <span class="badge-text">Tu entretenimiento sin límites</span>
</div>
```
- Ícono diamante (◆) a la izquierda
- Fondo semitransparente con blur
- Borde redondeado (border-radius: 999px)
- Estilos: `badge-icon`, `badge-text`

---

### 2. **Título Principal (H1)**
```html
<h1 class="hero-title">
  Licencias Digitales al
  <span class="hero-accent">Mejor Precio</span>
</h1>
```
- Font: 'Space Grotesk', weight: 700
- Tamaño responsive: clamp(2.4rem, 6vw, 3.8rem)
- Línea base: 1.15
- Palabra clave en `<span class="hero-accent">` con subrayado dinámico

---

### 3. **Subtítulo**
```html
<p class="hero-subtitle">
  Acceso inmediato a tus plataformas favoritas. Precios competitivos, entrega al instante y soporte 24/7.
</p>
```
- Font: 'Work Sans'
- Color: var(--hero-muted) - #9FC8E1
- Máximo ancho: 580px
- Line-height: 1.6

---

### 4. **Botones CTA**
```html
<div class="hero-cta-row">
  <button class="hero-btn hero-btn-primary">
    <span class="btn-icon">🛒</span>
    Ver catálogo
  </button>
  <button class="hero-btn hero-btn-secondary">
    <span class="btn-icon">▷</span>
    ¿Cómo funciona?
  </button>
</div>
```

#### Botón Primario
- Background: Gradiente de #49E2B6 a #3dce9f
- Color texto: #050D24 (oscuro)
- Sombra: 0 12px 32px rgba(73, 226, 182, 0.4)
- Hover: Traslación Y -3px con sombra aumentada

#### Botón Secundario
- Background: rgba(243, 236, 216, 0.08) (transparente)
- Borde: 1.5px solid rgba(73, 226, 182, 0.35)
- Color texto: #F3ECD8 (crema)
- Hover: Fondo más opaco + borde más visible

---

### 5. **Fila de Estadísticas**
```html
<div class="hero-stats">
  <div class="stat-item">
    <div class="stat-number">18+</div>
    <div class="stat-label">Productos</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">24/7</div>
    <div class="stat-label">Entrega de Licencias</div>
  </div>
  <div class="stat-item">
    <div class="stat-number">2,521+</div>
    <div class="stat-label">Ventas</div>
  </div>
</div>
```

- Layout: 3 columnas responsive (grid: repeat(auto-fit, minmax(140px, 1fr)))
- Números: Font 'Space Mono', size: clamp(1.8rem, 4vw, 2.6rem), color: #49E2B6
- Etiquetas: Mayúsculas, pequeñas, color: #9FC8E1

---

## 🎭 Fondos y Efectos

### Grid de Fondo
```css
.hero-bg-grid {
  background-image:
    linear-gradient(90deg, rgba(73, 226, 182, 0.04) 1px, transparent 1px),
    linear-gradient(0deg, rgba(73, 226, 182, 0.04) 1px, transparent 1px);
  background-size: 80px 80px;
}
```
- Grid sutil en verde menta con opacidad muy baja (0.04)
- Tamaño: 80px × 80px
- Crea efecto de profundidad sin saturar

### Gradientes Radiales
```css
.hero-bg-gradient {
  background: 
    radial-gradient(circle at 15% 20%, rgba(73, 226, 182, 0.15) 0%, transparent 25%),
    radial-gradient(circle at 85% 15%, rgba(79, 255, 209, 0.12) 0%, transparent 20%),
    linear-gradient(180deg, rgba(5, 13, 36, 0.8) 0%, rgba(4, 14, 37, 0.95) 100%);
}
```
- 2 focos radiales (arriba-izquierda y arriba-derecha)
- Gradiente lineal vertical
- Crea efecto de iluminación ambiental

---

## 📐 Espaciado y Layout

| Elemento | Padding/Margin | Notas |
|----------|----------------|-------|
| `.hero-premium` | 120px 24px 80px | Vertical: 120px arriba, 80px abajo |
| `.hero-badge` | 10px 20px | Padding interno |
| `.hero-badge` (bottom) | 32px | Margin-bottom |
| `.hero-title` (bottom) | 20px | Margin-bottom |
| `.hero-subtitle` (bottom) | 40px | Margin-bottom |
| `.hero-cta-row` (bottom) | 60px | Margin-bottom |
| `.hero-stats` | gap: 32px | Entre items |

---

## 🎬 Animaciones

### Fade-In-Up en Cascada
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

Timings:
- Badge: 0.8s ease-out, delay: 0s
- Title: 0.8s ease-out, delay: 0.1s
- Subtitle: 0.8s ease-out, delay: 0.2s
- Botones: 0.8s ease-out, delay: 0.3s
- Stats: 0.8s ease-out, delay: 0.4s

### Transiciones en Hover
```css
.hero-btn {
  transition: all 0.3s ease;
}
.hero-btn:hover {
  transform: translateY(-3px);
}
```

---

## 📱 Responsive Design

### Desktop (>768px)
- Badge: inline-flex horizontal
- Title: 2.4rem - 3.8rem
- Stats: 3 columnas con gap 32px
- Botones: Fila horizontal con gap 16px

### Tablet (768px)
- Reducción proporcional de tamaños
- Badge: 32px margin-bottom
- Title: clamp reduce a max 2.8rem
- Stats: gap reducido a 24px
- Botones: Padding reducido

### Mobile (≤480px)
- Badge: flex-direction: column, alineado a izquierda
- Title: 1.6rem
- Botones: `flex-direction: column`, width 100%
- Stats: 3 columnas compactas, gap 16px
- Padding general: 60px 16px 48px

---

## 🎨 Paleta de Colores (CSS Variables)

```css
:root {
  --hero-bg: #050D24;           /* Azul marino oscuro */
  --hero-accent: #49E2B6;       /* Verde menta */
  --hero-text: #F3ECD8;         /* Crema */
  --hero-muted: #9FC8E1;        /* Celeste apagado */
  --hero-border: rgba(243, 236, 216, 0.14); /* Borde sutil */
}
```

---

## 🔗 Fuentes de Google Fonts

Asegúrate de que estas líneas estén en el `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Work+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

---

## 📦 Cómo Integrar en tu Proyecto

### Paso 1: Copiar CSS
Copia el bloque `<style>` completo de `templates/hero-section.html` y pégalo en tu `<head>` de `index.html`.

### Paso 2: Copiar HTML
Coloca el HTML de la sección hero justo después del `<header>`:
```html
<header>
  <!-- tu navegación -->
</header>

<!-- AQUÍ VA LA SECCIÓN HERO -->
<section class="hero-premium">
  <!-- contenido del hero -->
</section>

<!-- resto de tu contenido -->
```

### Paso 3: Personalizar
Modifica el contenido del badge, título, subtítulo, botones y estadísticas según tus necesidades:
```html
<span class="badge-text">Tu texto aquí</span>
<h1 class="hero-title">Tu título <span class="hero-accent">destacado</span></h1>
<p class="hero-subtitle">Tu descripción</p>
```

---

## 🎯 Casos de Uso

- **E-commerce**: Hero para landing page de productos digitales
- **SaaS**: Sección introductoria de servicios
- **Marketplace**: Vitrina de plataforma de licencias
- **Portafolio**: Header impactante para showcases profesionales

---

## ✨ Características Avanzadas

- ✅ Completamente responsive
- ✅ Animaciones suaves
- ✅ Efectos hover interactivos
- ✅ Fondos dinámicos (grid + gradientes)
- ✅ Accesibilidad (semántica HTML, contrast ratios válidos)
- ✅ Performance optimizado (sin JS requerido)
- ✅ Dark mode ready
- ✅ CSS variables para fácil customización

---

## 🐛 Troubleshooting

**Las fuentes no cargan:**
→ Verifica que el link de Google Fonts esté en el `<head>` antes que otros CSS

**El hero se ve muy pequeño en mobile:**
→ Revisa que los clamp() estén correctos: `clamp(min, preff, max)`

**Las animaciones se ven entrecortadas:**
→ Asegúrate de que `animation-fill-mode: both` esté aplicado

**El fondo grid no se ve:**
→ Verifica que la opacidad sea > 0.02 para que sea visible

---

## 📄 Archivos de Referencia

- `templates/hero-section.html` - Componente completo con estilos
- `static/hero-demo.html` - Demo standalone HTML
- Este documento - Documentación técnica

---

**Última actualización:** 2026-08-15  
**Versión:** 1.0 Premium
