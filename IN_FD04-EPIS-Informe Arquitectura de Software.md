![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.001.png)

**UNIVERSIDAD PRIVADA DE TACNA** 

**FACULTAD DE INGENIERÍA** 

**Escuela Profesional de Ingeniería de Sistemas** 

**“Análisis de Datos de Tesis Universitarias para Guiar a Estudiantes en la Elección de Temas y Tecnologías”** 

Curso: Inteligencia de negocios Docente: Ing. Patrick Cuadros 

Integrantes: 

***Ayma Choque, Erick Yoel (2021072616) \
Poma Machicado, Fabiola Estefani (2021070030) Tapia Vargas, Dylan Yariet (2021072630)*** 

**Tacna – Perú *2025*** 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.002.png)



|CONTROL DE VERSIONES ||||||
| - | :- | :- | :- | :- | :- |
|Versión |Hecha por |Revisada por |Aprobada por |Fecha |Motivo |
|1\.0 |MPV |ELV |ARV |10/10/2020 |Versión Original |
# **“Análisis de Datos de Tesis Universitarias para Guiar a Estudiantes en la Elección de Temas y Tecnologías” Documento de Arquitectura de Software** 
# **Versión *{1.0}*** 


|CONTROL DE VERSIONES ||||||
| - | :- | :- | :- | :- | :- |
|Versión |Hecha por |Revisada por |Aprobada por |Fecha |Motivo |
|1\.0 |MPV |ELV |ARV |10/10/2020 |Versión Original |

ÍNDICE GENERAL

1. [***INTRODUCCIÓN  5***](#_page3_x85.05_y93.34)
1. [**Propósito (Diagrama 4+1)  5**](#_page3_x85.05_y406.32) 
1. [**Alcance  5**](#_page3_x85.05_y562.16) 
1. [**Definición, siglas y abreviaturas  5**](#_page3_x85.05_y681.60) 
1. **Organización del documento  5** 
2. [***OBJETIVOS Y RESTRICCIONES ARQUITECTONICAS  5***](#_page4_x85.05_y181.79)
   1. [Requerimientos Funcionales  5](#_page4_x85.05_y214.78)
   1. [Requerimientos No Funcionales – Atributos de Calidad  5](#_page5_x85.05_y157.93)
3. [***REPRESENTACIÓN DE LA ARQUITECTURA DEL SISTEMA  6***](#_page6_x85.05_y149.30)
1. [**Vista de Caso de uso  6**](#_page6_x85.05_y175.79) 
   1. [Diagramas de Casos de uso  6](#_page6_x85.05_y196.29)
2. [**Vista Lógica  6**](#_page6_x85.05_y577.43) 
1. [Diagrama de Subsistemas (paquetes)  7](#_page6_x85.05_y608.41)
1. [Diagrama de Secuencia (vista de diseño)  7](#_page7_x85.05_y106.77)
1. [Diagrama de Colaboración (vista de diseño)  7](#_page11_x85.05_y70.85)
1. [Diagrama de Objetos  7](#_page11_x85.05_y107.83)
1. [Diagrama de Clases  7](#_page12_x85.05_y70.85)
1. [Diagrama de Base de datos (relacional o no relacional)  7](#_page12_x85.05_y415.51)
3. [**Vista de Implementación (vista de desarrollo)  7**](#_page13_x85.05_y70.85) 
1. [Diagrama de arquitectura software (paquetes)  7](#_page13_x85.05_y85.34)
1. [Diagrama de arquitectura del sistema (Diagrama de componentes)  7](#_page13_x85.05_y412.88)
4. [**Vista de procesos  7**](#_page14_x85.05_y70.85) 

[3.4.1. Diagrama de Procesos del sistema (diagrama de actividad)  8](#_page14_x85.05_y85.34)

5. [**Vista de Despliegue (vista física)  8**](#_page15_x85.05_y70.85) 

[3.5.1. Diagrama de despliegue  8](#_page15_x85.05_y85.34)

4. [***ATRIBUTOS DE CALIDAD DEL SOFTWARE  8*** ](#_page16_x85.05_y70.85)[Escenario de Funcionalidad  8**](#_page16_x85.05_y85.34) [**Escenario de Usabilidad  8**](#_page16_x85.05_y184.29) [**Escenario de confiabilidad  9**](#_page16_x85.05_y268.74) **Escenario de rendimiento  9** [**Escenario de mantenibilidad  9**](#_page16_x85.05_y452.14) **Otros Escenarios  9** 
1. INTRODUCCIÓN<a name="_page3_x85.05_y93.34"></a> 

El proceso de elaboración de una tesis universitaria representa uno de los mayores retos para los estudiantes, especialmente al momento de elegir un tema adecuado y definir las tecnologías a utilizar. Esta etapa, fundamental en la formación académica, suele generar incertidumbre debido a la falta de orientación o de referencias concretas sobre las tendencias actuales y pasadas en los trabajos de investigación. 

Ante esta problemática, el presente proyecto tiene como objetivo principal brindar apoyo a los estudiantes mediante el análisis de datos históricos de tesis universitarias. A través del uso de herramientas de inteligencia de negocios como Power BI, se ha diseñado un dashboard interactivo que permite visualizar de manera clara y estructurada información clave sobre las categorías de tesis más desarrolladas, las tecnologías más utilizadas por año, y las universidades que destacan en determinados campos temáticos. 

Este análisis no solo proporciona una guía útil para la toma de decisiones informadas, sino que también fomenta una planificación más estratégica del trabajo de investigación. Al ofrecer una visualización comprensible y accesible de datos relevantes, se busca reducir la incertidumbre del estudiante y facilitar su camino hacia una tesis bien fundamentada y acorde con las tendencias académicas y tecnológicas. 

1. Propósito<a name="_page3_x85.05_y406.32"></a> (Diagrama 4+1) 

   El propósito de este documento es describir la arquitectura del sistema de visualización y análisis de tesis universitarias, usando el modelo arquitectónico 4+1 propuesto por Philippe Kruchten. Este enfoque permite representar el sistema desde diferentes perspectivas (vista lógica, vista de desarrollo, vista de procesos, vista física y casos de uso), facilitando la comprensión integral por parte de todos los stakeholders: desarrolladores, usuarios finales, mantenedores y responsables técnicos. 

   El sistema permite visualizar la evolución de tecnologías utilizadas en tesis, categorizar trabajos académicos y resaltar la producción de universidades en áreas específicas. 

2. Alcance<a name="_page3_x85.05_y562.16"></a> 

   Este proyecto abarca el análisis de tesis universitarias categorizadas por tema, año, universidad y tecnología utilizada. A través de gráficos interactivos en Power BI, se busca facilitar la toma de decisiones al momento de iniciar una tesis. La información se basa en una base de datos estructurada con campos como categoría, tecnología, título de tesis, universidad y año de publicación. 

3. Definición,<a name="_page3_x85.05_y681.60"></a> siglas y abreviaturas 

Tesis: Trabajo de investigación final elaborado por estudiantes para obtener un grado académico. 

Power BI: Herramienta de Microsoft para visualización de datos y creación de dashboards interactivos. 

Dashboard: Panel visual interactivo que muestra gráficos y tablas con datos relevantes. 

Categoría de Tesis: Área temática en la que se clasifica una tesis, como IA, Desarrollo Web, etc. 

Tecnología: Herramientas, lenguajes o plataformas utilizadas en el desarrollo de una tesis (por ejemplo, Firebase, Python, etc.). 

2. **OBJETIVOS<a name="_page4_x85.05_y181.79"></a> Y RESTRICCIONES ARQUITECTÓNICAS** 
1. Priorización de requerimientos* 
1. Requerimientos<a name="_page4_x85.05_y214.78"></a> Funcionales 



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

2. Requerimientos<a name="_page5_x85.05_y157.93"></a> No Funcionales – Atributos de Calidad 



|RNF |Requerimiento |Descripción |
| - | - | - |
|RNF-01 |Rendimiento |El sistema debe responder rápidamente durante todas las operaciones comunes (subir archivos, generar gráficos, aplicar filtros). Los tiempos de carga no deben ser mayores a 2 segundos en cualquier operación estándar. |
|RNF-02 |Usabilidad |La interfaz del sistema debe ser intuitiva y fácil de usar, permitiendo a los usuarios (coordinadores académicos) realizar tareas como cargar archivos, visualizar gráficos y aplicar filtros sin complicaciones. La navegación debe ser fluida en dispositivos de escritorio y móviles. |
|RNF-03 |Escalabilidad  |El sistema debe ser capaz de manejar un número creciente de tesis y datos sin afectar su rendimiento. Debe poder escalar de manera eficiente en cuanto a la base de datos y la generación de gráficos conforme crecen los datos y usuarios. |
|RNF-04 |Disponibilidad  |El sistema debe estar disponible el 99% del tiempo, garantizando que los usuarios puedan acceder al dashboard y realizar análisis sin interrupciones significativas. |

2. Restricciones 

   Durante el desarrollo del presente proyecto se identificaron diversas restricciones que condicionaron el diseño, implementación y alcance del sistema. Estas son las principales: 

- Disponibilidad de datos:La calidad y precisión del análisis dependen directamente de los datos disponibles en los archivos fuente (como archivos CSV o bases de datos). Si la información está incompleta, desactualizada o mal estructurada, puede afectar los resultados mostrados por el sistema. 
- Formato de entrada: El sistema está diseñado para trabajar con un formato de datos específico (campos como título, categoría, universidad, tecnología y año). Cualquier cambio en la estructura de entrada requiere ajustes técnicos en la carga y procesamiento de los datos. 
3. **REPRESENTACIÓN<a name="_page6_x85.05_y149.30"></a> DE LA ARQUITECTURA DEL SISTEMA**
1. Vista<a name="_page6_x85.05_y175.79"></a> de Caso de uso* 
3. Diagramas<a name="_page6_x85.05_y196.29"></a> de Casos de uso 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.003.jpeg)

2. Vista<a name="_page6_x85.05_y577.43"></a> Lógica* 
1. Diagrama<a name="_page6_x85.05_y608.41"></a> de Subsistemas (paquetes) 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.004.jpeg)

2. Diagrama<a name="_page7_x85.05_y106.77"></a> de Secuencia (vista de diseño) 

UC01: Visualizar categorías de tesis en gráfico circular 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.005.png)

UC02: Explorar títulos de tesis por categoría 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.006.png)

UC03: Visualizar tecnologías usadas por tesis 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.007.png)

UC04: Analizar la evolución de tecnologías 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.008.png)

UC05: Explorar tesis por tecnología 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.009.png)

UC06: Comparar universidades por categoría de tesis 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.010.png)

UC07: Aplicar filtros personalizados 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.011.png)

UC08: Acceso directo al dashboard Power BI 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.012.png)

3. Diagrama<a name="_page11_x85.05_y70.85"></a> de Colaboración (vista de diseño) 
3. Diagrama<a name="_page11_x85.05_y107.83"></a> de Objetos 

UC01: Visualizar categorías de tesis en gráfico circular 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.013.png)

UC02: Explorar títulos de tesis por categoría 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.014.png)

UC03: Visualizar tecnologías usadas por tesis 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.015.png)

UC04: Analizar la evolución de tecnologías 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.016.png)

UC05: Explorar tesis por tecnología 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.017.png)

UC06: Comparar universidades por categoría de tesis 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.018.png)

UC07: Aplicar filtros personalizados 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.019.png)

UC08: Acceso directo al dashboard Power BI 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.020.png)

5. Diagrama<a name="_page12_x85.05_y70.85"></a> de Clases 

   ![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.021.jpeg)

6. Diagrama<a name="_page12_x85.05_y415.51"></a> de Base de datos 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.022.jpeg)

3. Vista<a name="_page13_x85.05_y70.85"></a> de Implementación (vista de desarrollo) 
1. Diagrama<a name="_page13_x85.05_y85.34"></a> de arquitectura software (paquetes) 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.023.jpeg)

2. Diagrama<a name="_page13_x85.05_y412.88"></a> de arquitectura del sistema (Diagrama de componentes) 

   ![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.024.png)

4. Vista<a name="_page14_x85.05_y70.85"></a> de procesos* 

   <a name="_page14_x85.05_y85.34"></a>3.4.1. Diagrama de Procesos del sistema (diagrama de actividad) 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.025.jpeg)

5. Vista<a name="_page15_x85.05_y70.85"></a> de Despliegue (vista física) 

   <a name="_page15_x85.05_y85.34"></a>3.5.1. Diagrama de despliegue 

![](/IMG/Aspose.Words.5fc1f2e5-687d-4689-bc4d-5d0e8ebd01fc.026.jpeg)

4. **ATRIBUTOS<a name="_page16_x85.05_y70.85"></a> DE CALIDAD DEL SOFTWARE** <a name="_page16_x85.05_y85.34"></a>**Escenario de Funcionalidad** 

   El sistema cumple con su propósito principal: permitir la visualización clara y filtrada de tesis académicas por categoría, tecnologías utilizadas y universidad. Además, brinda funcionalidades como filtros temporales y categóricos que responden a las necesidades informativas de los usuarios. La seguridad está garantizada mediante el control del acceso a la fuente de datos y la integridad de la información visualizada. 

   <a name="_page16_x85.05_y184.29"></a>**Escenario de Usabilidad** 

   La interfaz fue diseñada para que cualquier usuario (docente, estudiante o investigador) pueda interactuar fácilmente con el sistema, interpretar los gráficos y comprender los resultados sin necesidad de conocimientos técnicos avanzados. Se prioriza la facilidad de aprendizaje, la navegación intuitiva y una presentación visual atractiva y clara de los datos. 

   <a name="_page16_x85.05_y268.74"></a>**Escenario de confiabilidad** 

   El sistema garantiza la integridad y disponibilidad de los datos mostrados. Las visualizaciones están respaldadas por información precisa y verificada, lo que permite a los usuarios confiar en los resultados para la toma de decisiones o futuras investigaciones. Asimismo, se han considerado medidas básicas de seguridad para proteger los datos contra alteraciones o accesos no autorizados. 

   **Escenario de rendimiento** 

   El sistema fue optimizado para ofrecer tiempos de carga rápidos y respuestas inmediatas ante las consultas o filtros aplicados. El procesamiento de datos y la generación de visualizaciones se realiza de forma eficiente, sin sobrecargar el navegador ni requerir recursos excesivos del dispositivo del usuario. 

   <a name="_page16_x85.05_y452.14"></a>**Escenario de mantenibilidad** 

   La estructura modular del sistema facilita futuras actualizaciones, como la incorporación de nuevos filtros, categorías o tecnologías emergentes. También permite la adaptación a nuevos conjuntos de datos o a otros contextos académicos. La documentación del código y la organización interna del proyecto fueron consideradas para garantizar su escalabilidad. 
17 
