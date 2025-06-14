![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.001.png)

**UNIVERSIDAD PRIVADA DE TACNA** 

**FACULTAD DE INGENIERÍA** 

**Escuela Profesional de Ingeniería de Sistemas** 

***“Análisis de Datos de Tesis Universitarias para Guiar a Estudiantes en la Elección de Temas y Tecnologías”*** 

Curso: Inteligencia de negocios Docente: Ing. Patrick Cuadros 

Integrantes: 

***Ayma Choque, Erick Yoel (2021072616) \
Poma Machicado, Fabiola Estefani (2021070030) Tapia Vargas, Dylan Yariet (2021072630)*** 

**Tacna – Perú *2025*** 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.002.png)



|CONTROL DE VERSIONES ||||||
| - | :- | :- | :- | :- | :- |
|Versión |Hecha por |Revisada por |Aprobada por |Fecha |Motivo |
|1\.0 |MPV |ELV |ARV |10/10/2020 |Versión Original |

**“Análisis de Datos de Tesis Universitarias para Guiar a Estudiantes en la Elección de Temas y Tecnologías” Documento de Especificación de Requerimientos de Software** 

**Versión *{1.0}*** 



|CONTROL DE VERSIONES ||||||
| - | :- | :- | :- | :- | :- |
|Versión |Hecha por |Revisada por |Aprobada por |Fecha |Motivo |
|1\.0 |MPV |ELV |ARV |10/10/2020 |Versión Original |

**ÍNDICE GENERAL** 

[**INTRODUCCIÓN  4](#_page3_x70.87_y80.83)** 

1. [**Generalidades de la Empresa  4](#_page3_x70.87_y104.64)** 
1. [Nombre de la Empresa  4](#_page3_x70.87_y120.44) 
1. [Visión  4](#_page3_x70.87_y160.06) 
1. [Misión  4](#_page3_x70.87_y199.68) 
1. [Organigrama  4](#_page3_x70.87_y286.72) 
2. [**Visionamiento de la Empresa  4](#_page3_x70.87_y302.52)** 
1. [Descripción del Problema  4](#_page3_x70.87_y436.99) 
1. [Objetivos de Negocios  4](#_page3_x70.87_y452.80) 
1. [Objetivos de Diseño  4](#_page3_x70.87_y626.88) 
1. [Alcance del Proyecto  4](#_page4_x70.87_y104.64) 
1. [Viabilidad del Sistema  4](#_page4_x70.87_y587.84) 
1. [Información obtenida del Levantamiento de Información  4](#_page5_x70.87_y318.33) 
3. [**Análisis de Procesos  4](#_page6_x70.87_y80.83)** 
1. [Diagrama del Proceso Actual – Diagrama de Actividades  4](#_page6_x70.87_y96.64) 
1. [Diagrama del Proceso Propuesto – Diagrama de Actividades Inicial  4](#_page7_x70.87_y80.83) 
4. [**Especificación de Requerimientos de Software  4](#_page8_x70.87_y80.83)** 
   1. [Cuadro de Requerimientos Funcionales Inicial  4](#_page8_x70.87_y96.64) 
   1. [Cuadro de Requerimientos No Funcionales  4](#_page9_x70.87_y80.83) 
   1. Cuadro de Requerimientos Funcionales Final  4 
   1. Reglas de Negocio  4 
5. [**Fase de Desarrollo  4](#_page11_x70.87_y407.26)** 
1. [Perfiles de Usuario  4](#_page11_x70.87_y423.07) 
1. [Modelo Conceptual  4](#_page11_x70.87_y551.33) 
   1. [Diagrama de Paquetes  4](#_page11_x70.87_y567.14) 
   1. [Diagrama de Casos de Uso  4](#_page12_x70.87_y80.83) 
   1. [Escenarios de Caso de Uso (Narrativa)  4](#_page12_x70.87_y438.79) 
1. [Modelo Lógico  4](#_page16_x70.87_y501.45) 
1. [Análisis de Objetos  4](#_page16_x70.87_y517.26) 
1. [Diagrama de Actividades con Objetos  4](#_page17_x70.87_y445.92) 
1. [Diagrama de Secuencia  4](#_page22_x70.87_y80.83) 
1. [Diagrama de Clases  4](#_page26_x70.87_y80.83) 

[**CONCLUSIONES  4](#_page27_x70.87_y80.83) **[RECOMENDACIONES  4](#_page27_x70.87_y270.72) [BIBLIOGRAFÍA 4](#_page27_x70.87_y563.65)** 

<a name="_page3_x70.87_y80.83"></a>INTRODUCCIÓN 

1. Generalidades<a name="_page3_x70.87_y104.64"></a> de la Empresa 
1. Nombre<a name="_page3_x70.87_y120.44"></a> de la Empresa Universidad Privada de Tacna - Escuela Profesional de Ingeniería de Sistemas 
1. Visión<a name="_page3_x70.87_y160.06"></a> Ser referentes en la formación de ingenieros de sistemas a nivel nacional.   
1. Misión<a name="_page3_x70.87_y199.68"></a> Formar Ingenieros de Sistemas competentes, emprendedores, con conocimientos científicos, formación humanística y responsabilidad social, para el desarrollo de soluciones de software y tecnologías de información que agreguen valor a las organizaciones.  
1. Organigrama<a name="_page3_x70.87_y286.72"></a> 
2. Visionamiento<a name="_page3_x70.87_y302.52"></a> de la Empresa 
1. Descripción del Problema Las universidades generan una gran cantidad de información sobre las tecnologías utilizadas en sus tesis. Sin embargo, la falta de un sistema estructurado para recopilar, analizar y visualizar estos datos dificulta la identificación de tendencias y la toma de decisiones informadas. Actualmente, el proceso de gestión de estos datos es manual y propenso a errores, lo que limita su utilidad. 
1. Objetivos<a name="_page3_x70.87_y452.80"></a><a name="_page3_x70.87_y436.99"></a> de Negocios 
   1. Facilitar la gestión y análisis de datos sobre tecnologías utilizadas en tesis universitarias. 
   1. Mejorar la toma de decisiones académicas mediante insights basados en datos. 
   1. Optimizar la carga y validación de archivos CSV con información de tesis. 
   1. Proveer una plataforma centralizada para el Coordinador Académico. 
   1. Ofrecer un dashboard interactivo en Power BI para análisis detallado. 
1. Objetivos<a name="_page3_x70.87_y626.88"></a> de Diseño 
- Crear un sistema web intuitivo para la carga y gestión de datasets. 
- Implementar validaciones que aseguren la integridad de los datos subidos. 
- Desarrollar un dashboard optimizado y rápido en Power BI. 
- Garantizar la interactividad y filtrado eficiente de los datos en el dashboard. 
- Permitir acceso fácil y seguro al dashboard desde la web. 
4. Alcance<a name="_page4_x70.87_y104.64"></a> del Proyecto Sistema 
- Carga de archivos CSV con datos de tesis. 
- Validación del formato de los archivos antes de la carga. 
- Historial de archivos subidos con opción de descarga. 
- Guía de actualización para Power BI. 
- Botón de acceso directo al dashboard en Power BI Web. 

Dashboard en Power BI  

- El dashboard está diseñado para ayudar a estudiantes universitarios en la elección de temas y tecnologías para sus tesis, y contempla los siguientes elementos visuales divididos en objetivos: 
- Gráfico de pastel: distribución de tesis por categoría. 
- Tabla interactiva: títulos de tesis filtrables por categoría. 
- Gráfico de barras: tecnologías más utilizadas en el desarrollo de tesis. 
- Gráfico de área: evolución anual del uso de tecnologías en tesis. 
- Filtro interactivo por tecnología: permite seleccionar una y ver su comportamiento en el tiempo. 
- Tabla: relación de títulos, categorías y tecnologías para apoyar la toma de decisiones del estudiante. Gráfico de barras apiladas: categorías de tesis con leyenda por universidad. 
- Permite identificar qué universidades destacan más por cada temática. 
- Proporciona una base para investigar referentes o egresados por tema específico. 
5. Viabilidad<a name="_page4_x70.87_y587.84"></a> del Sistema 
   ## El sistema propuesto es viable desde los puntos de vista técnico, económico y operativo: 
- Viabilidad Técnica 

  El proyecto se basa en tecnologías ampliamente accesibles y estables, como Power BI para la visualización de datos y archivos CSV como formato de entrada. La base de datos utilizada es sencilla y relacional, lo que facilita la integración y mantenimiento. Además, no se requieren recursos computacionales avanzados, ya que el procesamiento se realiza mayormente en Power BI. 

- Viabilidad Económica 

  La herramienta Power BI Desktop es gratuita y suficiente para el desarrollo del dashboard. Solo si se desea la publicación en línea y colaboración en tiempo real, se requiere una licencia Power BI Pro, cuyo costo es accesible. No hay necesidad de adquirir software adicional o infraestructura especializada, lo que reduce significativamente los costos. 

- Viabilidad Operativa 

  El sistema es fácil de usar para estudiantes universitarios, quienes podrán cargar archivos, consultar visualizaciones y tomar decisiones basadas en datos sin conocimientos técnicos avanzados. La interfaz es intuitiva y el proceso de análisis está automatizado, permitiendo un uso autónomo y eficiente. 

6. Información<a name="_page5_x70.87_y318.33"></a> obtenida del Levantamiento de Información 

   Durante el proceso de levantamiento de información, se recolectaron y analizaron datos estructurados sobre tesis universitarias con el objetivo de entender cómo los estudiantes seleccionan temas y tecnologías para sus trabajos de investigación. Los principales puntos obtenidos fueron: 

- Categorías de tesis comunes: Se identificaron categorías frecuentes como Inteligencia Artificial, Desarrollo Web, Seguridad Informática, entre otras. 
- Tecnologías más utilizadas: Herramientas como Firebase, Python, JavaScript, y frameworks como Angular y React fueron recurrentes. 
- Años de publicación: Se reconoció un incremento en el uso de ciertas tecnologías a lo largo del tiempo, especialmente en los últimos cinco años. 
- Universidades con mayor producción: Algunas universidades destacan en producción de tesis por categoría, lo que puede influir en la toma de decisiones de los estudiantes. 
3. Análisis<a name="_page6_x70.87_y80.83"></a> de Procesos 
1. Diagrama<a name="_page6_x70.87_y96.64"></a> del Proceso Actual – Diagrama de Actividades 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.003.jpeg)

2. Diagrama<a name="_page7_x70.87_y80.83"></a> del Proceso Propuesto – Diagrama de Actividades Inicial 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.004.jpeg)

4. Especificación<a name="_page8_x70.87_y80.83"></a> de Requerimientos de Software 
1. Cuadro<a name="_page8_x70.87_y96.64"></a> de Requerimientos Funcionales Inicial 



|RF |Requerimiento |Descripción |
| - | - | - |
|RF-01 |Visualizar categorías de tesis en gráfico circular |El sistema debe permitir al estudiante visualizar un gráfico circular que muestre la cantidad de tesis por categoría, para identificar áreas temáticas más frecuentes. |
|RF-02 |Explorar títulos de tesis por categoría |Al seleccionar una categoría en el gráfico circular, el sistema debe mostrar una tabla con los títulos de tesis relacionados. |
|RF-03 |Visualizar tecnologías usadas por tesis |Al seleccionar un título de tesis, el sistema debe mostrar un gráfico de barras con las tecnologías utilizadas en esa tesis. |
|RF-04 |Analizar la evolución de tecnologías |El sistema debe permitir seleccionar una tecnología y visualizar su evolución en el tiempo (por años) mediante un gráfico de áreas. |
|RF-05 |Explorar tesis por tecnología |El sistema debe mostrar una tabla con títulos de tesis, su categoría y tecnología seleccionada, filtrada por la tecnología elegida en el gráfico de evolución. |
|RF-06 |Comparar universidades por categoría de tesis |El sistema debe permitir al estudiante visualizar un gráfico de barras que compara las universidades que han producido más tesis por categoría (como Inteligencia Artificial, Desarrollo Web, etc.). |
|RF-07 |Aplicar filtros personalizados |El sistema debe permitir aplicar filtros dinámicos (como año, universidad o tecnología) para personalizar el análisis de las tesis. |
|RF-08 |Acceso directo al dashboard Power BI |El sistema debe ofrecer un acceso directo al dashboard publicado en Power BI Web para facilitar su consulta desde cualquier dispositivo. |

2. Cuadro<a name="_page9_x70.87_y80.83"></a> de Requerimientos No Funcionales 



|RNF |Requerimiento |Descripción |
| - | - | - |
|RNF-01 |Rendimiento |El sistema debe responder rápidamente durante todas las operaciones comunes (subir archivos, generar gráficos, aplicar filtros). Los tiempos de carga no deben ser mayores a 2 segundos en cualquier operación estándar. |
|RNF-02 |Usabilidad |La interfaz del sistema debe ser intuitiva y fácil de usar, permitiendo a los usuarios (coordinadores académicos) realizar tareas como cargar archivos, visualizar gráficos y aplicar filtros sin complicaciones. La navegación debe ser fluida en dispositivos de escritorio y móviles. |
|RNF-03 |Escalabilidad  |El sistema debe ser capaz de manejar un número creciente de tesis y datos sin afectar su rendimiento. Debe poder escalar de manera eficiente en cuanto a la base de datos y la generación de gráficos conforme crecen los datos y usuarios. |
|RNF-04 |Disponibilidad  |El sistema debe estar disponible el 99% del tiempo, garantizando que los usuarios puedan acceder al dashboard y realizar análisis sin interrupciones significativas. |

3. Cuadro de Requerimientos Funcionales Final 



|RF |Requerimiento |Descripción |
| - | - | - |
|RF-01 |Visualizar categorías de tesis en gráfico circular |El sistema debe permitir al estudiante visualizar un gráfico circular que muestre la cantidad de tesis por categoría, para identificar áreas temáticas más frecuentes. |
|RF-02 |Explorar títulos de tesis por categoría |Al seleccionar una categoría en el gráfico circular, el sistema debe mostrar una tabla con los títulos de tesis relacionados. |
|RF-03 |Visualizar tecnologías usadas por tesis |Al seleccionar un título de tesis, el sistema debe mostrar un gráfico de barras con las tecnologías |
|||utilizadas en esa tesis. |
| :- | :- | - |
|RF-04 |Analizar la evolución de tecnologías |El sistema debe permitir seleccionar una tecnología y visualizar su evolución en el tiempo (por años) mediante un gráfico de áreas. |
|RF-05 |Explorar tesis por tecnología |El sistema debe mostrar una tabla con títulos de tesis, su categoría y tecnología seleccionada, filtrada por la tecnología elegida en el gráfico de evolución. |
|RF-06 |Comparar universidades por categoría de tesis |El sistema debe permitir al estudiante visualizar un gráfico de barras que compare las universidades que han producido más tesis por categoría (como Inteligencia Artificial, Desarrollo Web, etc.). |
|RF-07 |Aplicar filtros personalizados |El sistema debe permitir aplicar filtros dinámicos (como año, universidad o tecnología) para personalizar el análisis de las tesis. |
|RF-08 |Acceso directo al dashboard Power BI |El sistema debe ofrecer un acceso directo al dashboard publicado en Power BI Web para facilitar su consulta desde cualquier dispositivo. |

4. Reglas de Negocio 



|Nº |Reglas de Negocio |Descripción |
| - | - | - |
|RN-01  |Acceso académico público |El acceso al dashboard es público y exclusivo para fines académicos. |
|RN-02 |Visualización basada en datos validados |Las visualizaciones se basan únicamente en los datos de tesis validados previamente. |
|RN-03 |Asociación obligatoria de tesis  |Cada tesis debe estar asociada a una categoría y al menos una tecnología. |
|RN-04 |Visualización temporal condicionada  |Solo se muestran visualizaciones temporales si existe un año de publicación válido. |
|RN-05 |Exclusión de datos incompletos  |Las tesis sin categoría o tecnología se excluyen de los gráficos correspondientes. |
|RN-06 |Actualización dinámica por selección |La selección de categorías en gráficos actualiza dinámicamente las visualizaciones relacionadas. |
|RN-07 |Requisito de selección en evolución |El gráfico de evolución de tecnologías requiere la selección de una tecnología específica. |
|RN-08 |Normalización de datos|Los datos deben estar normalizados para ser visualizados correctamente. |
|RN-09 |Fuentes oficiales |Las universidades no pueden modificar los datos; estos provienen de fuentes académicas oficiales. |
|RN-10 |Restricción de uso comercial |El sistema no permite uso comercial ni exportación masiva de los datos. |

5. Fase<a name="_page11_x70.87_y407.26"></a> de Desarrollo 
1. Perfil<a name="_page11_x70.87_y423.07"></a> de Usuario **Edad**: 20 a 28 años 

   **Nivel académico**: Últimos ciclos de una carrera profesional 

   **Necesidades**: Elegir tema y tecnología para su tesis con mayor claridad **Habilidades digitales**: Nivel medio, familiarizados con plataformas académicas **Objetivo principal**: Inspirarse y tomar decisiones acertadas para su tesis

2. Modelo<a name="_page11_x70.87_y551.33"></a> Conceptual 
1. Diagrama<a name="_page11_x70.87_y567.14"></a> de Paquetes 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.005.jpeg)

2. Diagrama<a name="_page12_x70.87_y80.83"></a> de Casos de Uso 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.006.jpeg)

3. Escenarios<a name="_page12_x70.87_y438.79"></a> de Caso de Uso (Narrativa) 



|**Caso de uso** |Visualizar categorías de tesis en gráfico circular |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Permitir al usuario identificar la distribución de tesis por categoría de investigación. |
|**Tipo** |Principal |
|**Descripción** |El sistema muestra un gráfico circular que representa el porcentaje de tesis por cada categoría (ej. Inteligencia Artificial, Big Data, IoT). Esto facilita el análisis visual de las áreas más abordadas por los trabajos de investigación. |
|**Precondición** |La base de datos debe estar actualizada con las tesis categorizadas. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Acceder al dashboard. |2\. Mostrar el gráfico circular con los datos actualizados. |
|3\. Seleccionar un período de tiempo (opcional). |4\. Aplicar filtro al gráfico circular. |
| - | - |
|5\. Pasar el cursor sobre una categoría. |6\. Mostrar porcentaje y número de tesis de esa categoría. |



|**Caso de uso** |Explorar títulos de tesis por categoría |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Permitir al usuario consultar los títulos de tesis agrupados por categorías específicas. |
|**Tipo** |Secundario |
|**Descripción** |Al hacer clic sobre una categoría en el gráfico, el sistema muestra una lista con los títulos de tesis que pertenecen a dicha categoría. |
|**Precondición** |Debe existir una relación entre cada tesis y su categoría. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Seleccionar una categoría. |2\. Mostrar los títulos de tesis de dicha categoría. |
|3\. Hacer clic sobre un título. |4\. (Opcional) Mostrar detalles adicionales de la tesis. |



|**Caso de uso** |Visualizar tecnologías usadas por tesis |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Mostrar qué tecnologías se han utilizado en las tesis registradas. |
|**Tipo** |Principal |
|**Descripción** |El sistema presenta un gráfico de barras o nube de palabras con las tecnologías más empleadas, facilitando el análisis del ecosistema tecnológico académico. |
|**Precondición** |La información sobre tecnologías usadas debe estar cargada y normalizada en el sistema. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Acceder al gráfico de tecnologías. |2\. Mostrar visualización con frecuencia de uso por tecnología. |
|3\. Aplicar filtros (por año, universidad, etc.). |4\. Actualizar el gráfico con base en los filtros |
||aplicados. |
| :- | - |



|**Caso de uso** |Analizar la evolución de tecnologías |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Permitir al usuario visualizar cómo ha variado el uso de diferentes tecnologías en las tesis a lo largo del tiempo. |
|**Tipo** |Principal |
|**Descripción** |El sistema muestra una línea de tiempo con gráficos que representan la frecuencia con que cada tecnología ha sido utilizada por año. |
|**Precondición** |Los datos deben incluir año y tecnologías asociadas a cada tesis. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Acceder al gráfico de evolución tecnológica. |2\. Mostrar una línea temporal con el uso de tecnologías por año. |
|3\. Filtrar por categoría o universidad (opcional). |4\. Ajustar la visualización según los filtros seleccionados. |
|5\. Comparar dos tecnologías. |6\. Resaltar las líneas correspondientes para facilitar el análisis. |



|**Caso de uso** |Explorar tesis por tecnología |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Permitir al usuario acceder a las tesis que han utilizado una tecnología específica. |
|**Tipo** |Secundario |
|**Descripción** |El usuario selecciona una tecnología y el sistema muestra todas las tesis que han empleado dicha tecnología. |
|**Precondición** |Cada tesis debe tener registrada al menos una tecnología asociada. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Seleccionar una tecnología del listado o gráfico. |2\. Mostrar una lista de tesis que utilizan la tecnología seleccionada. |
|3\. Hacer clic sobre un título de tesis. |4\. Mostrar los detalles de la tesis (autor, universidad, año, etc.). |
| - | :- |



|**Caso de uso** |Comparar universidades por categoría de tesis |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Analizar y comparar la producción de tesis en distintas categorías por universidad. |
|**Tipo** |Principal |
|**Descripción** |El sistema presenta una visualización (gráfico de barras comparativo o mapa de calor) con la cantidad de tesis por categoría y por universidad. |
|**Precondición** |Los datos deben incluir la universidad asociada a cada tesis y su categoría. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Acceder al gráfico comparativo de universidades. |2\. Mostrar visualización con datos cruzados por categoría y universidad. |
|3\. Seleccionar una o varias universidades. |4\. Actualizar el gráfico para reflejar solo las universidades seleccionadas. |



|**Caso de uso** |Aplicar filtros personalizados |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Ofrecer una vista dinámica del dashboard permitiendo filtrar por distintos campos: año, universidad, categoría, tecnología, etc. |
|**Tipo** |Secundario |
|**Descripción** |El sistema proporciona controles para que el usuario pueda aplicar múltiples filtros y así realizar un análisis más específico. |
|**Precondición** |El sistema debe tener integradas opciones de filtro en cada visualización. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Acceder al panel de filtros. |2\. Mostrar campos disponibles para filtrar. |
|3\. Aplicar filtros por año, universidad, |4\. Actualizar automáticamente los gráficos en |
|tecnología, etc. |función de los filtros. |
| - | - |
|5\. Limpiar filtros. |6\. Restaurar visualización a su estado original. |



|**Caso de uso** |Acceso directo al dashboard Power BI |
| - | - |
|**Actores** |Coordinador Académico, Público en general |
|**Propósito** |Brindar acceso rápido y centralizado al dashboard interactivo de Power BI. |
|**Tipo** |Principal |
|**Descripción** |Desde la plataforma, los usuarios pueden ingresar directamente al entorno de Power BI para explorar visualizaciones, aplicar filtros y exportar datos. |
|**Precondición** |El usuario debe contar con permisos de visualización en Power BI y el enlace al dashboard debe estar activo. |
|**Curso normal de eventos** ||
|**Acciones de actores** |**Acciones del sistema** |
|1\. Iniciar sesión en la plataforma. |2\. Validar acceso del usuario. |
|3\. Hacer clic en el botón o enlace del dashboard. |4\.   Redirigir al usuario al dashboard Power BI. |
|5\. Navegar entre reportes. |6\. Mostrar contenido interactivo actualizado. |

3. Modelo<a name="_page16_x70.87_y501.45"></a> Lógico 
1. Análisis<a name="_page16_x70.87_y517.26"></a> de Objetos 

   UC01: Visualizar categorías de tesis en gráfico circular 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.007.png)

UC02: Explorar títulos de tesis por categoría 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.008.png)

UC03: Visualizar tecnologías usadas por tesis 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.009.png)

UC04: Analizar la evolución de tecnologías 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.010.png)

UC05: Explorar tesis por tecnología 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.011.png)

UC06: Comparar universidades por categoría de tesis 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.012.png)

UC07: Aplicar filtros personalizados 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.013.png)

UC08: Acceso directo al dashboard Power BI 

![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.014.png)

2. Diagrama<a name="_page17_x70.87_y445.92"></a> de Actividades 

   UC01: Visualizar categorías de tesis en gráfico circular 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.015.png)

   UC02: Explorar títulos de tesis por categoría 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.016.png)

   UC03: Visualizar tecnologías usadas por tesis 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.017.png)

   UC04: Analizar la evolución de tecnologías 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.018.png)

   UC05: Explorar tesis por tecnología 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.019.png)

   UC06: Comparar universidades por categoría de tesis 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.020.png)

   UC07: Aplicar filtros personalizados 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.021.png)

   UC08: Acceso directo al dashboard Power BI 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.022.png)

3. Diagrama<a name="_page22_x70.87_y80.83"></a> de Secuencia 

   UC01: Visualizar categorías de tesis en gráfico circular 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.023.png)

   UC02: Explorar títulos de tesis por categoría 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.024.png)

   UC03: Visualizar tecnologías usadas por tesis 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.025.png)

   UC04: Analizar la evolución de tecnologías 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.026.png)

   UC05: Explorar tesis por tecnología 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.027.png)

   UC06: Comparar universidades por categoría de tesis 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.028.png)

   UC07: Aplicar filtros personalizados 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.029.png)

   UC08: Acceso directo al dashboard Power BI 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.030.png)

4. Diagrama<a name="_page26_x70.87_y80.83"></a> de Clases 

   ![](/IMG/Aspose.Words.7f950f38-0c48-4023-9072-2ebbe0093805.031.jpeg)

<a name="_page27_x70.87_y80.83"></a>CONCLUSIÓN 

El desarrollo del presente proyecto permitió analizar de forma clara y visual la producción de tesis universitarias, clasificadas por categorías, tecnologías utilizadas y procedencia institucional. Gracias a las visualizaciones implementadas, fue posible identificar tendencias en el uso de tecnologías a lo largo del tiempo, así como reconocer qué universidades destacan en determinadas áreas temáticas. Estos resultados no solo brindan un panorama general del estado actual de la investigación académica, sino que también ofrecen insumos valiosos para la toma de decisiones en ámbitos educativos, tecnológicos y científicos. En conclusión, el proyecto contribuye significativamente al entendimiento de la evolución tecnológica en el ámbito académico, facilitando futuras investigaciones y promoviendo una toma de decisiones informada. 

<a name="_page27_x70.87_y270.72"></a>RECOMENDACIONES 

**Actualizar constantemente la base de datos de tesis** para asegurar que las visualizaciones reflejen información actual y relevante, permitiendo un análisis más preciso de las tendencias tecnológicas emergentes. 

**Ampliar el análisis incluyendo nuevas variables**, como el impacto de cada tesis (por ejemplo, número de citas o publicaciones relacionadas), para enriquecer la comprensión del aporte académico de cada trabajo. 

**Implementar filtros más específicos en las visualizaciones**, como año, universidad, carrera o palabras clave, con el fin de facilitar la búsqueda personalizada por parte de investigadores, docentes y estudiantes. 

**Promover el uso de esta herramienta en entornos educativos** para que sirva como guía en la<a name="_page27_x70.87_y563.65"></a> elección de temas y tecnologías para futuras investigaciones. 
28 
