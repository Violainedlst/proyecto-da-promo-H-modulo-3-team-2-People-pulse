🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
# People Pulse: Optimización y Retención de Talento
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪

![Logo de la Empresa](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/blob/main/images/logo.png)
_ _ _

## Módulo 3: Optimización de Talento

### 1. Resumen

En el entorno empresarial altamente competitivo de hoy en día, la toma de decisiones informadas es esencial para el éxito a largo plazo. La retención de empleados y la satisfacción en el trabajo son cuestiones críticas para cualquier organización, ya que afectan directamente a la productividad, la moral y la rentabilidad.

Con el objetivo de reducir la rotación de empleados y mejorar la satisfacción en el trabajo, ABC Corporation nos ha contratado, People Pulse, para desarrollar un proyecto de análisis de datos y experimentación A/B de gran alcance. Nuestra misión es identificar factores clave que influyen en la satisfacción en el trabajo y, en última instancia, en la retención de empleados.

En este proyecto, presentaremos los resultados de nuestro análisis exploratorio de datos, diseñaremos un experimento A/B para probar hipótesis críticas y analizaremos los resultados para proporcionar a ABC Corporation información valiosa que informe sus decisiones estratégicas.

![ABC Corporation](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/blob/main/images/logo_ABC.png)

_ _ _

### ¿Quiénes Somos?

Nosotras somos People Pulse, un equipo de analistas de datos dedicado a la optimización y retención de talento en las organizaciones. Nuestro equipo está compuesto exclusivamente por mujeres apasionadas y expertas en análisis de datos, psicología organizacional y tecnología. Creemos firmemente en la capacidad de los datos para transformar entornos laborales y mejorar la vida de las personas en el trabajo.

Nuestra misión es ayudar a las empresas a tomar decisiones informadas que promuevan la satisfacción y retención de sus empleados. Utilizamos herramientas de análisis avanzado, experimentación y tecnología de vanguardia para ofrecer soluciones personalizadas que aborden las necesidades específicas de cada organización.

_ _ _


### Fases del Proyecto 

**Fase 1:** Análisis Exploratorio de Datos (EDA)
[URL](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/tree/main/Fase01_Exploraci%C3%B3n_Datos)
Antes de llevar a cabo el experimento A/B y plantear hipótesis, es crucial comprender mejor el conjunto de datos y sus características. Realizaremos un análisis exploratorio detallado para familiarizarnos con ellos y entender qué información tenemos.

**Fase 2:** Transformación de los Datos
[URL](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/tree/main/Fase02_Limpieza_Datos)
Esta fase incluye la limpieza de datos, normalización, conversión de tipos de datos y la aplicación de reglas empresariales específicas. Las transformaciones se realizarán mediante funciones de Python aplicadas a los datos extraídos. Algunas de las transformaciones incluirán:


* Reemplazo de valores en la columna gender.
* Conversión de columnas a tipos de datos correctos.
* Eliminación o mantenimiento de valores duplicados.
* Corrección de valores inconsistentes y errores tipográficos.
* Identificación y manejo de columnas redundantes.


**Fase 3:** Diseño de BBDD e Inserción de los Datos
[URL](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/tree/main/Fase03_Arquitectura_BBDD)
Creación y estructuración de la base de datos, incluyendo la identificación de tablas necesarias y sus relaciones, así como la definición de claves primarias y foráneas. Incluye la inserción de datos iniciales.

**Fase 4:** Problema de A/B Testing
[URL](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/tree/main/Fase04_A.B-Testing)
Determinaremos si existe una relación entre el nivel de satisfacción en el trabajo y la rotación de empleados. Crearemos grupos A (Control) y B (Variante) según el nivel de satisfacción y analizaremos la tasa de rotación en cada grupo.

**Fase 5:** Creación de una ETL
[URL](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/tree/main/Fase05_Creaci%C3%B3n_de_una_ETL)
Desarrollaremos un archivo .py que llevará a cabo la extracción, transformación y carga (ETL) de datos, garantizando que la información se actualice de manera consistente y automatizada.

Fase 6: Reporte de los Resultados
[URL](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/tree/main/Fase06_Reporte_Resultados)
Proporcionaremos a ABC Corporation un informe detallado con visualizaciones en Python, resaltando tendencias, áreas de mejora y fortalezas dentro de la empresav

_ _ _


### Los Datos

Las columnas que encontraremos en el DataFrame incluyen:


* Age: Edad del empleado.
* Attrition: Indicador de si el empleado ha dejado la empresa.
* BusinessTravel: Frecuencia de viajes relacionados con el trabajo.
* DailyRate: Tarifa diaria del empleado.
* Department: Departamento del empleado.
* DistanceFromHome: Distancia desde el hogar al trabajo.
* Education: Nivel de educación.
* EducationField: Campo de educación.
* EmployeeCount: Contador de empleados.
* EmployeeNumber: Número de identificación único.
* EnvironmentSatisfaction: Nivel de satisfacción con el entorno de trabajo.
* Gender: Género del empleado.
* HourlyRate: Tarifa por hora.
* JobInvolvement: Nivel de implicación en el trabajo.
* JobLevel: Nivel jerárquico.
* JobRole: Rol o puesto de trabajo.
* JobSatisfaction: Nivel de satisfacción con el trabajo.
* MaritalStatus: Estado civil.
* MonthlyIncome: Ingresos mensuales.
* MonthlyRate: Tasa mensual.
* NumCompaniesWorked: Número de compañías previas.
* Over18: Indica si es mayor de 18 años.
* OverTime: Indicador de horas extras.
* PercentSalaryHike: Porcentaje de aumento salarial.
* PerformanceRating: Calificación de rendimiento.
* RelationshipSatisfaction: Satisfacción en relaciones interpersonales.
* StandardHours: Horas estándar de trabajo.
* StockOptionLevel: Nivel de opciones de compra de acciones.
* TotalWorkingYears: Total de años de experiencia laboral.
* TrainingTimesLastYear: Número de veces que recibió capacitación el año pasado.
* WorkLifeBalance: Equilibrio entre trabajo y vida personal.
* YearsAtCompany: Años en la empresa actual.
* YearsInCurrentRole: Años en el puesto actual.
* YearsSinceLastPromotion: Años desde la última promoción.
* YearsWithCurrManager: Años bajo la supervisión del actual gerente.


![Icono para ABC Corporation](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/blob/main/images/icono.png)

[CSV Sin Limpiar](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/blob/main/CSVs/HR_RAW_DATA.csv)
[CSV Limpio](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/blob/main/CSVs/HR_RAW_DATA_LIMPIO.csv)

_ _ _

### 🥇Objetivos del Proyecto

- **Identificar Factores Clave:** Determinar los factores que más influyen en la satisfacción y retención de los empleados.
- **Reducir la Rotación:** Desarrollar estrategias basadas en datos para reducir la rotación de empleados.
- **Mejorar la Satisfacción Laboral:** Proponer medidas para mejorar la satisfacción de los empleados en el trabajo.
- **Implementar A/B Testing:** Diseñar y ejecutar experimentos A/B para validar hipótesis clave.
- **Automatizar Procesos:** Crear un sistema de ETL automatizado para la gestión continua de datos.
- **Generar Informes Visuales:** Proporcionar informes detallados y visualizaciones que ayuden a la toma de decisiones estratégicas en ABC Corporation.


[Informe Resultante](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/blob/main/Fase06_Reporte_Resultados/InformeAnalisisAbcCorporation.pdf)

[Manual de Uso para Interfaz Gráfica](https://github.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/blob/main/Fase06_Reporte_Resultados/Manual_de_usuario_ABC_Corporation.pdf)

_ _ _

### Personas del Equipo



* Gloria González Muñoz (https://www.linkedin.com/in/gloria-gonzalez-105500107/)
* Violaine Deloustal (https://www.linkedin.com/in/violaine-deloustal-b35498105/)
* Diana García Martín (https://www.linkedin.com/in/diana-garc)
* Silvia Piñel Fañanás (https://www.linkedin.com/in/silviapi)
* Mábel Martínez Rodríguez (https://www.linkedin.com/in/mabelmr)


🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
¡Gracias por interesarte en nuestro proyecto! :muscle::sparkles:   
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
