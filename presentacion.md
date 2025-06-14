---
marp: true
theme: uncover # O el tema base que prefieras, lo sobrescribiremos
paginate: true
header: "**Inteligencia de Negocios**"
footer: "© 2025 - Pág. <!--_footer: {page} / {totalPages}-->"
style: |
  /* Estilo base para todas las diapositivas */
  section {
    background-color: #FFFFFF; /* Fondo blanco */
    color: #34495E; /* Texto principal: Gris azulado oscuro (Wet Asphalt) */
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }

  /* Estilos para los encabezados */
  h1 {
    color: #2980B9; /* Azul primario (Peter River) */
    text-align: center;
    font-size: 2.2em;
    font-weight: 600;
  }

  h2 {
    color: #16A085; /* Turquesa/Verde Mar (Green Sea) */
    font-size: 1.8em;
    border-bottom: 2px solid #BDC3C7; /* Gris claro para el borde (Silver) */
    padding-bottom: 0.3em;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    font-weight: 500;
  }

  h3, h4, h5, h6 {
    color: #2C3E50; /* Azul medianoche (Midnight Blue) */
    font-size: 1.4em;
    font-weight: 500;
  }

  /* Estilos para el texto normal y listas */
  p, li {
    color: #34495E; /* Gris azulado oscuro (Wet Asphalt) */
    font-size: 0.95em; /* Ligeramente más grande para mejor lectura */
    line-height: 1.7; /* Mayor interlineado */
  }

  /* Estilos para tablas */
  table {
    color: #34495E;
    width: 100%;
    margin-top: 20px;
    border-collapse: collapse;
  }
  th {
    color: #FFFFFF; /* Texto blanco */
    background-color: #2C3E50; /* Fondo Azul medianoche */
    font-weight: bold;
  }
  td, th {
    border: 1px solid #BDC3C7; /* Borde Gris (Silver) */
    padding: 12px; /* Más padding */
    text-align: left;
  }
  tr:nth-child(even) {
    background-color: #ECF0F1; /* Filas pares con fondo gris muy claro (Clouds) */
  }

  /* Estilos para enlaces */
  a {
    color: #2980B9; /* Azul primario (Peter River) */
    text-decoration: none;
    font-weight: 500;
  }
  a:hover {
    color: #3498DB; /* Azul más claro al pasar el mouse (Belize Hole) */
    text-decoration: underline;
  }

  /* Estilos para bloques de código */
  pre, code {
    background-color: #ECF0F1; /* Fondo gris muy claro (Clouds) */
    color: #2C3E50; /* Texto Azul medianoche */
    border: 1px solid #BDC3C7; /* Borde Gris (Silver) */
    border-radius: 4px;
    padding: 0.6em;
  }
  code { /* Para código inline */
    padding: 0.2em 0.4em;
    font-size: 0.9em;
  }

  /* Elementos de énfasis */
  strong {
    color: #2980B9; /* Azul primario (Peter River) */
    font-weight: 600;
  }

  em {
    color: #16A085; /* Turquesa/Verde Mar (Green Sea) */
    font-style: italic;
  }

  /* Estilo para la portada (clase 'lead') */
  section.lead {
    text-align: center;
    padding-top: 8%;
  }
  section.lead h1 {
    color: #2980B9; /* Azul primario */
    font-size: 2.8em;
  }
  section.lead h2 {
    color: #16A085; /* Turquesa/Verde Mar */
    font-size: 1.5em;
    margin-top: 0.5em;
    border-bottom: none;
  }
  section.lead p {
    color: #34495E;
    font-size: 1em;
    margin-top: 1em;
  }
  .integrantes {
    font-size: 0.8em;
    color: #7F8C8D; /* Gris (Asbestos) */
    margin-top: 30px;
  }
  .integrantes p {
    margin: 5px 0;
    font-size: 0.9em;
    color: #7F8C8D;
  }
  .integrantes strong {
    color: #2C3E50; /* Azul medianoche */
  }

  /* Para la clase 'highlight' */
  .highlight {
    background-color: #ECF0F1; /* Fondo gris muy claro (Clouds) */
    border-left: 5px solid #F39C12; /* Borde Naranja (Orange) como acento */
    padding: 15px;
    border-radius: 4px;
    margin-top: 20px;
  }
  .highlight p, .highlight li {
    color: #2C3E50; /* Texto Azul medianoche dentro del highlight */
  }

  /* Imágenes */
  img {
    max-width: 85%; /* Ligeramente más pequeñas para más aire */
    max-height: 60vh;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 4px; /* Bordes redondeados sutiles */
    /* box-shadow: 0 4px 8px rgba(0,0,0,0.08); */ /* Sombra opcional */
  }

  /* Estilo para los iconos de pin y diana */
  .emoji-title {
    font-size: 1.2em;
    margin-right: 8px;
    color: #F39C12; /* Naranja (Orange) para los emojis */
  }
---

<!-- Portada -->
<!-- _class: lead -->
# **Análisis de Datos de Tesis Universitarias para Guiar a Estudiantes en la Elección de Temas y Tecnologías**

<p style="font-size:1.1em; color: #16A085;">Curso: Inteligencia de Negocios</p> <!-- Turquesa -->
<p style="font-size:1em; color: #34495E;">Docente: Ing. Patrick Cuadros</p>

--- 

<div class="integrantes">
  <p><strong>Integrantes:</strong></p>
  <p>Ayma Choque, Erick Yoel (2021072616)</p>
  <p>Poma Machicado, Fabiola Estefani (2021070030)</p>
  <p>Tapia Vargas, Dylan Yariet (2021072630)</p>
</div>

![bg right width:250](/documentos_md/img/logo.png)

---

## <span class="emoji-title">📌</span>Planteamiento del Problema

Muchos estudiantes universitarios enfrentan dificultades al momento de elegir un tema de tesis y las tecnologías adecuadas para su desarrollo. Esta situación se debe a la falta de acceso a información organizada y visual sobre los trabajos realizados en años anteriores.


### Consecuencias:
- Dificultad para elegir un tema de tesis alineado con las tendencias tecnológicas.
- Incertidumbre sobre qué tecnologías son más utilizadas en el entorno académico.
- Falta de referentes claros sobre cómo se aplican ciertas herramientas en proyectos reales.

---

## <span class="emoji-title">🎯</span>Alcance

Este proyecto abarca el análisis de tesis universitarias categorizadas por tema, año, universidad y tecnología utilizada. A través de gráficos interactivos en Power BI, se busca facilitar la toma de decisiones al momento de iniciar una tesis. La información se basa en una base de datos estructurada con campos como categoría, tecnología, título de tesis, universidad y año de publicación.

---

## <span class="emoji-title">🎯</span>Objetivo Principal

<p>-Permitir la visualización clara de la cantidad de tesis por categoría, titulos de tesis filtrados y las tecnologías utilizadas en cada una.</p>

---

## <span class="emoji-title">✅</span>Objetivos Secundarios

- Analizar la evolución temporal del uso de tecnologías en las tesis para identificar tendencias y cambios significativos a lo largo del tiempo.
- Identificar las universidades que destacan en cantidad de tesis por la categoria de tesis de interes.

---
## Conclusión

El dashboard desarrollado proporciona a los estudiantes universitarios una herramienta útil y visualmente intuitiva para identificar categorías de tesis con mayor frecuencia, tecnologías empleadas y tendencias según los años, facilitando así la toma de decisiones informadas.

---