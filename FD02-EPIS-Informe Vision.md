![ref1]

**UNIVERSIDAD PRIVADA DE TACNA** 

**FACULTAD DE INGENIERÍA** 

**Escuela Profesional de Ingeniería de Sistemas** 

***“Análisis de Datos de Tesis Universitarias para Guiar a Estudiantes en la Elección de Temas y Tecnologías”*** 

Curso: *Inteligencia de Negocios* Docente: *Ing. Patrick Cuadros* 

Integrantes: 

***Ayma Choque, Erick Yoel (2021072616) \
Poma Machicado, Fabiola Estefani (2021070030) Tapia Vargas, Dylan Yariet (2021072630)*** 

**Tacna – Perú *2025*** 

![](/IMG/Aspose.Words.2e7ccb51-cc74-4fe5-ae33-c6070a1db31b.002.png) ![ref2]
|CONTROL DE VERSIONES ||||||
| - | :- | :- | :- | :- | :- |
|Versión |Hecha por |Revisada por |Aprobada por |Fecha |Motivo |
|1\.0 |MPV |PC |PC |10/06/2025 |Versión Original |
# **Análisis de Datos de Tesis Universitarias para Guiar a Estudiantes en la Elección de Temas y Tecnologías Documento de Visión** 
# **Versión *{1.0}*** 


|CONTROL DE VERSIONES ||||||
| - | :- | :- | :- | :- | :- |
|Versión |Hecha por |Revisada por |Aprobada por |Fecha |Motivo |
|1\.0 |MPV |ELV |ARV |10/10/2025 |Versión Original |

**ÍNDICE GENERAL** 

1. [**Introducción  4](#_page3_x85.05_y84.96)** 
1. [Propósito  4](#_page3_x85.05_y401.61) 
1. [Alcance  4](#_page3_x85.05_y476.89) 
1. [Definiciones, Siglas y Abreviaturas  4](#_page3_x85.05_y581.15) 
1. [Referencias  5](#_page4_x85.05_y144.44) 
1. [Visión General  5](#_page4_x85.05_y599.50) 
2. [**Posicionamiento  6](#_page5_x85.05_y158.93)** 
   1. [Oportunidad de negocio  6](#_page5_x85.05_y174.74) 
   1. [Definición del problema  6](#_page5_x85.05_y351.45) 
3. [**Descripción de los interesados y usuarios  6](#_page5_x85.05_y536.17)** 
1. [Resumen de los interesados  6](#_page5_x85.05_y551.98) 
1. [Resumen de los usuarios  6](#_page5_x85.05_y641.75) 
1. [Entorno de usuario  7](#_page6_x85.05_y84.96) 
1. [Perfiles de los Usuarios  7](#_page6_x85.05_y189.23) 
1. [Necesidades de los interesados y usuarios  7](#_page6_x85.05_y347.98) 
4. [**Vista General del Producto  7](#_page6_x85.05_y498.73)** 
   1. [Perspectiva del producto  7](#_page6_x85.05_y514.54) 
   1. [Resumen de capacidades  7](#_page6_x85.05_y641.29) 
   1. [Suposiciones y dependencias  8](#_page7_x85.05_y200.89) 
   1. [Licenciamiento e instalación  8](#_page7_x85.05_y424.10) 
5. [**Características del producto  8](#_page7_x85.05_y610.32)** 
5. [**Restricciones  9](#_page8_x85.05_y107.46)** 
5. [**Rangos de calidad  9](#_page8_x85.05_y264.70)** 
5. [**Precedencia y Prioridad  9](#_page8_x85.05_y400.96)** 
5. [**Otros requerimientos del producto  9](#_page8_x85.05_y566.20)** 
1. [Estándares legales  9](#_page8_x85.05_y582.01) 
1. [Estándares de comunicación  10](#_page9_x85.05_y84.96) 
1. [Estándares de cumplimiento de la plataforma  10](#_page9_x85.05_y256.70) 
1. [Estándares de calidad y seguridad  10](#_page9_x85.05_y391.45) 
10. [**Conclusiones  10](#_page9_x85.05_y613.15)** 
10. [**Recomendaciones  11](#_page10_x85.05_y202.40)** 
10. [**Bibliografía  11](#_page10_x85.05_y491.57)** 
1. Introducción<a name="_page3_x85.05_y84.96"></a> 

   El proceso de elaboración de una tesis universitaria representa uno de los mayores retos para los estudiantes, especialmente al momento de elegir un tema adecuado y definir las tecnologías a utilizar. Esta etapa, fundamental en la formación académica, suele generar incertidumbre debido a la falta de orientación o de referencias concretas sobre las tendencias actuales y pasadas en los trabajos de investigación. 

   Ante esta problemática, el presente proyecto tiene como objetivo principal brindar apoyo a los estudiantes mediante el análisis de datos históricos de tesis universitarias. A través del uso de herramientas de inteligencia de negocios como Power BI, se ha diseñado un dashboard interactivo que permite visualizar de manera clara y estructurada información clave sobre las categorías de tesis más desarrolladas, las tecnologías más utilizadas por año, y las universidades que destacan en determinados campos temáticos. 

   Este análisis no solo proporciona una guía útil para la toma de decisiones informadas, sino que también fomenta una planificación más estratégica del trabajo de investigación. Al ofrecer una visualización comprensible y accesible de datos relevantes, se busca reducir la incertidumbre del estudiante y facilitar su camino hacia una tesis bien fundamentada y acorde con las tendencias académicas y tecnológicas. 

1. Propósito<a name="_page3_x85.05_y401.61"></a> 

   Brindar orientación a los estudiantes universitarios mediante el análisis de datos de tesis previas, ayudándoles a elegir temas y tecnologías con base en tendencias reales, visualizadas mediante dashboards interactivos. 

2. Alcance<a name="_page3_x85.05_y476.89"></a> 

Este proyecto abarca el análisis de tesis universitarias categorizadas por tema, año, universidad y tecnología utilizada. A través de gráficos interactivos en Power BI, se busca facilitar la toma de decisiones al momento de iniciar una tesis. La información se basa en una base de datos estructurada con campos como categoría, tecnología, título de tesis, universidad y año de publicación. 

3. Definiciones,<a name="_page3_x85.05_y581.15"></a> Siglas y Abreviaturas 

   Tesis: Trabajo de investigación final elaborado por estudiantes para obtener un grado académico. 

   Power BI: Herramienta de Microsoft para visualización de datos y creación de dashboards interactivos. 

   Dashboard: Panel visual interactivo que muestra gráficos y tablas con datos relevantes. 

   Categoría de Tesis: Área temática en la que se clasifica una tesis, como IA, Desarrollo Web, etc. 

   Tecnología: Herramientas, lenguajes o plataformas utilizadas en el desarrollo de una tesis (por ejemplo, Firebase, Python, etc.). 

4. Referencias<a name="_page4_x85.05_y144.44"></a> 

   En los últimos años, las universidades han generado una gran cantidad de trabajos de investigación a nivel de pregrado y posgrado. Sin embargo, muchos de estos documentos quedan almacenados sin un tratamiento adecuado que permita aprovechar su contenido para orientar a futuros estudiantes. Esta situación ha motivado el desarrollo de sistemas de análisis de datos que permitan extraer información útil de repositorios académicos, como base para la toma de decisiones informadas. 

   Diversos estudios han propuesto el uso de herramientas de Business Intelligence (BI) y análisis de datos para facilitar la exploración de patrones en tesis universitarias. Por ejemplo, investigaciones recientes destacan el uso de Power BI para construir dashboards que muestran la evolución de tecnologías, la frecuencia de ciertas temáticas y la distribución por universidades, como recurso clave para investigadores novatos (Sharda et al., 2020). 

   Asimismo, Provost y Fawcett (2013) enfatizan que el pensamiento analítico basado en datos puede ser un factor decisivo al momento de seleccionar un tema de tesis, ya que permite visualizar qué áreas están siendo más desarrolladas y qué tecnologías están en tendencia. Esta perspectiva ha sido especialmente útil en carreras como Ingeniería de Sistemas, donde la elección de tecnologías actualizadas es crucial. 

   De igual forma, el enfoque de análisis de tesis en base a su categoría, año de publicación, universidad y tecnologías utilizadas no solo permite identificar tendencias, sino también visualizar oportunidades de innovación en áreas poco exploradas. Esto ha impulsado el desarrollo de soluciones enfocadas exclusivamente en estudiantes, como tu proyecto, que organiza dicha información en gráficos dinámicos e interactivos para facilitar la comprensión y exploración de los datos. 

5. Visión<a name="_page4_x85.05_y599.50"></a> General 

   Este proyecto consiste en el desarrollo de un sistema de visualización interactiva basado en Power BI, que analiza datos históricos de tesis universitarias con el objetivo de orientar a los estudiantes en la elección de temas y tecnologías relevantes para sus investigaciones. A través de dashboards organizados por objetivos específicos, se presenta información sobre las categorías más comunes, la evolución de tecnologías utilizadas a lo largo del tiempo y las universidades que destacan en ciertas áreas temáticas. 

   La solución permite filtrar y explorar los datos de manera intuitiva, lo que facilita la identificación de tendencias, tecnologías emergentes y enfoques investigativos aplicados por otros estudiantes. De esta forma, se convierte en una herramienta útil para inspirar, comparar y tomar decisiones fundamentadas en el desarrollo de una tesis. 

2. Posicionamiento<a name="_page5_x85.05_y158.93"></a> 
1. Oportunidad<a name="_page5_x85.05_y174.74"></a> de negocio 

   Actualmente, muchos estudiantes enfrentan dificultades al momento de definir el tema y las tecnologías para desarrollar su tesis universitaria, lo que genera retrasos, inseguridad académica y decisiones poco fundamentadas. Esta situación representa una oportunidad para aprovechar el análisis de datos como herramienta de apoyo, permitiendo a los estudiantes explorar tendencias pasadas y actuales en trabajos de investigación. Mediante un dashboard interactivo, se puede ofrecer una guía visual basada en datos reales, que aporte valor en la toma de decisiones y oriente a los estudiantes hacia enfoques exitosos y actualizados, mejorando así la calidad y eficiencia del proceso de elaboración de tesis. 

2. Definición<a name="_page5_x85.05_y351.45"></a> del problema 

   Los estudiantes universitarios suelen enfrentar incertidumbre al momento de seleccionar el tema y las tecnologías para su tesis, debido a la falta de referencias claras y actualizadas sobre las tendencias en investigaciones previas. Esto se traduce en una toma de decisiones limitada, basada muchas veces en recomendaciones informales o búsquedas desorganizadas. La ausencia de una herramienta que sintetice de forma visual y comprensible los datos históricos de tesis dificulta identificar qué temas son más comunes, qué tecnologías están en auge y qué universidades destacan en determinadas categorías. 

3. Descripción<a name="_page5_x85.05_y536.17"></a> de los interesados y usuarios 
1. Resumen<a name="_page5_x85.05_y551.98"></a> de los interesados 

   El único interesado clave en este proyecto es el estudiante universitario, específicamente aquel que se encuentra en proceso de definir, desarrollar o investigar ideas para su tesis. El dashboard está diseñado para ayudarlo a tomar decisiones informadas basadas en datos reales de tesis anteriores. 

2. Resumen<a name="_page5_x85.05_y641.75"></a> de los usuarios 

   El usuario principal del sistema es el estudiante universitario de últimos ciclos, que necesita apoyo para elegir un tema y tecnología adecuada para su tesis. Este estudiante busca referencias previas, conocer qué se ha hecho en su área y qué herramientas están en tendencia. 

3. Entorno<a name="_page6_x85.05_y84.96"></a> de usuario 

   El entorno de usuario es un dashboard interactivo desarrollado en Power BI, con gráficos dinámicos, filtros y tablas que permiten explorar temas, tecnologías y tendencias de tesis. Su diseño es simple e intuitivo, accesible desde un navegador web, sin necesidad de conocimientos avanzados en análisis de datos. 

4. Perfiles<a name="_page6_x85.05_y189.23"></a> de los Usuarios 

   **Edad**: 20 a 28 años 

   **Nivel académico**: Últimos ciclos de una carrera profesional 

   **Necesidades**: Elegir tema y tecnología para su tesis con mayor claridad **Habilidades digitales**: Nivel medio, familiarizados con plataformas académicas **Objetivo principal**: Inspirarse y tomar decisiones acertadas para su tesis 

5. Necesidades<a name="_page6_x85.05_y347.98"></a> de los interesados y usuarios 

   Conocer las **categorías de tesis más comunes** para guiar la elección de su tema Saber qué **tecnologías han sido más utilizadas** para evaluar su aplicabilidad Ver la **evolución de ciertas tecnologías a lo largo del tiempo** 

   Identificar en qué **universidades se han desarrollado ciertos tipos de tesis** Tener acceso a **títulos reales de tesis anteriores** como punto de referencia 

4. Vista<a name="_page6_x85.05_y498.73"></a> General del Producto 
1. Perspectiva<a name="_page6_x85.05_y514.54"></a> del producto 

   El producto se concibe como una herramienta de consulta académica dirigida a estudiantes universitarios. Se posiciona como una solución que complementa la orientación académica brindada por docentes o asesores, aportando un enfoque basado en datos para tomar decisiones más informadas sobre el tema de tesis. Puede funcionar como un módulo dentro de una plataforma universitaria o de acceso independiente. 

2. Resumen<a name="_page6_x85.05_y641.29"></a> de capacidades 

   El dashboard incluye las siguientes capacidades: 

- Visualización de categorías de tesis mediante gráfico circular interactivo. 
- Listado de títulos de tesis por categoría seleccionada. 
- Gráfico de barras de tecnologías utilizadas por categoría o tesis. 
- Gráfico de áreas para ver la evolución del uso de tecnologías a lo largo de los años. 
- Filtro dinámico por tecnología, que actualiza visualizaciones en tiempo real. 
- Tabla combinada de tesis, categoría y tecnología para análisis contextual. 
- Gráfico de barras por universidad y categoría de tesis, para identificar instituciones destacadas en cada área temática. 
3. Suposiciones<a name="_page7_x85.05_y200.89"></a> y dependencias 

   Se asume que la base de datos se encuentra estructurada y actualizada correctamente, sin errores en los registros (por ejemplo, sin tecnologías duplicadas o tesis sin año de publicación). 

   El funcionamiento del dashboard depende de Power BI Desktop o Power BI Service para su visualización e interacción. 

   La utilidad del análisis está condicionada a la cantidad y variedad de datos disponibles. A mayor volumen histórico y diversidad temática, mejores serán las recomendaciones y tendencias que se puedan identificar. 

   Se asume que los usuarios finales tienen un conocimiento básico del uso de dashboards interactivos (clics, filtros, navegación entre páginas). 

4. Licenciamiento<a name="_page7_x85.05_y424.10"></a> e instalación 

   Licencia de Power BI: Power BI Desktop es de uso gratuito. Para publicar en la nube y compartir, se requiere Power BI Pro. 

   Instalación: Solo se requiere la instalación de Power BI Desktop en un equipo Windows. No se necesita instalación de servidores ni dependencias adicionales. 

   Base de datos: Se asume que el archivo fuente (.csv, Excel o base de datos SQL) se encuentra accesible localmente o a través de conexión directa en el entorno Power BI. 

5. Características<a name="_page7_x85.05_y610.32"></a> del producto 

   Visualización de datos interactiva y dinámica. 

   Navegación entre páginas por objetivos. 

   Filtros por categoría, tecnología y año de publicación. Análisis de tecnologías por tendencias y recurrencia. Comparación entre universidades por áreas temáticas. Consulta directa de títulos de tesis según filtros aplicados. 

   Diseño enfocado en estudiantes como usuarios finales. 

6. Restricciones<a name="_page8_x85.05_y107.46"></a> 

   El análisis se limita a los campos disponibles en la base de datos (categoría, tecnología, título, año, universidad). 

   No se incluyen resúmenes ni contenido completo de las tesis, solo los metadatos disponibles. 

   El producto no incluye recomendaciones automáticas con IA, solo visualización basada en filtros y tendencias. 

   Se requiere conexión a internet si se usa la versión online (Power BI Service). 

7. Rangos<a name="_page8_x85.05_y264.70"></a> de calidad 

   Interfaz limpia y amigable con visuales consistentes. 

   Tiempo de respuesta inmediato para filtros y selecciones. 

   Datos depurados sin registros vacíos ni duplicados. 

   Actualización sencilla de datos mediante sustitución del archivo fuente. Legibilidad y contraste adecuados para facilitar la interpretación de gráficos. 

8. Precedencia<a name="_page8_x85.05_y400.96"></a> y Prioridad 

   Primero, se debe asegurar la calidad y limpieza de los datos. 

   Segundo, se prioriza la utilidad para el estudiante: las visualizaciones deben responder preguntas clave (qué categoría elegir, qué tecnología usar, qué universidad investigar). 

   Tercero, la integración del dashboard con otras plataformas es opcional y secundaria. 

   Cuarto, se prioriza el mantenimiento sencillo del informe, facilitando actualizaciones futuras con nuevos datos. 

9. Otros<a name="_page8_x85.05_y566.20"></a> requerimientos del producto 
1. Estándares<a name="_page8_x85.05_y582.01"></a> legales 

   Protección de datos personales: El proyecto no incluye información confidencial ni nombres de estudiantes, cumpliendo así con la Ley N.° 29733 – Ley de Protección de Datos Personales (Perú). 

   Uso académico y educativo: El análisis se realiza con fines educativos y de orientación estudiantil, sin fines de lucro. 

   Fuentes de datos: Los datos utilizados provienen de una base propia o recopilada con fines académicos. Si se incluye información de universidades reales, se debe evitar violar derechos de autor o propiedad intelectual de las tesis. 

2. Estándares<a name="_page9_x85.05_y84.96"></a> de comunicación 

   **Visualizaciones claras y comprensibles**: Uso de gráficos estándar (circular, de barras, de áreas) con etiquetas legibles. 

   **Interactividad guiada**: Cada gráfico está acompañado de filtros o leyendas que ayudan al usuario a comprender mejor la información. 

   **Lenguaje simple y directo**: Todo el contenido está orientado a estudiantes universitarios, evitando tecnicismos innecesarios. 

   **Colores y diseño**: Se siguen buenas prácticas de visualización de datos (colores diferenciables, uso de leyendas, jerarquía visual). 

3. Estándares<a name="_page9_x85.05_y256.70"></a> de cumplimiento de la plataforma 

   Compatibilidad: El dashboard fue desarrollado en Power BI Desktop y es compatible con Power BI Service para su publicación en línea. 

   Formato de datos: Se cumple con las estructuras esperadas por Power BI (relaciones normalizadas, claves únicas, tipos de datos consistentes). 

   Rendimiento: El informe ha sido optimizado para un rendimiento fluido, evitando cálculos complejos innecesarios. 

4. Estándares<a name="_page9_x85.05_y391.45"></a> de calidad y seguridad Calidad: 
- Validación previa de los datos: sin registros duplicados o vacíos. 
- Actualización de datos mediante conexiones configuradas. 
- Pruebas de visualizaciones con distintos filtros para garantizar integridad. 

Seguridad: 

- El archivo .pbix no contiene contraseñas, credenciales ni conexiones en vivo a bases de datos sensibles. 
- Si se publica en línea, se debe restringir el acceso a usuarios autorizados (recomendado uso privado o compartido solo con estudiantes). 
- Se evita mostrar información personal o sensible. 
10. Conclusiones<a name="_page9_x85.05_y613.15"></a> 

    **Facilitación en la elección de temas de tesis**: El dashboard desarrollado proporciona a los estudiantes universitarios una herramienta útil y visualmente intuitiva para identificar categorías de tesis con mayor frecuencia, tecnologías empleadas y tendencias según los años, facilitando así la toma de decisiones informadas. 

    **Identificación de tecnologías emergentes**: Gracias al gráfico de áreas y filtros aplicables, los estudiantes pueden analizar qué tecnologías han sido más utilizadas en los últimos años, lo que permite orientar sus proyectos hacia herramientas actuales y con mayor relevancia académica o profesional. 

    **Referencia por universidades destacadas**: El gráfico de barras por universidad y categoría de tesis permite conocer qué instituciones han trabajado más ciertas temáticas, sirviendo como guía para conocer enfoques existentes, buscar referentes o posibles asesores. 

    **Organización efectiva de la información**: La estructura del dashboard permite una navegación simple y enfocada en los intereses del usuario, integrando visualizaciones claras, tablas detalladas y filtros dinámicos para mejorar la experiencia. 

11. Recomendaciones<a name="_page10_x85.05_y202.40"></a> 

    **Ampliar el conjunto de datos**: Incluir más tesis de diferentes universidades o facultades permitirá que los resultados sean más representativos y útiles para una mayor cantidad de estudiantes. 

    **Agregar buscador por palabras clave**: Incluir un filtro por palabras clave en los títulos o resúmenes de tesis facilitará aún más la exploración por parte del usuario. 

    **Implementar una vista de tecnologías relacionadas**: Mostrar sugerencias de tecnologías complementarias que suelen aparecer juntas en tesis ayudaría a los estudiantes a estructurar mejor sus marcos tecnológicos. 

    **Actualizar datos periódicamente**: Se recomienda establecer una rutina de actualización anual o semestral del dataset para mantener el dashboard alineado con las tendencias actuales. 

    **Publicar en una plataforma accesible**: Subir el proyecto a Power BI Service o incrustarlo en una página web académica garantizaría su uso continuo y alcance entre los estudiantes de diversas carreras. 

12. Bibliografía<a name="_page10_x85.05_y491.57"></a> 

    Provost, F., & Fawcett, T. (2013). *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking*. O’Reilly Media. 

    Sharda, R., Delen, D., & Turban, E. (2020). *Analytics, Data Science, & Artificial Intelligence: Systems for Decision Support* (11th ed.). Pearson Education. 
11 

[ref1]: /IMGAsposeAspose.Words.2e7ccb51-cc74-4fe5-ae33-c6070a1db31b.001.png
[ref2]: /IMG/Aspose.Words.2e7ccb51-cc74-4fe5-ae33-c6070a1db31b.003.png
