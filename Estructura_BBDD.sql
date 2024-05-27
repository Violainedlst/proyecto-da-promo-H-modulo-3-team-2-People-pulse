/* Las columnas que os encontraréis en el DataFrame son:

Age: La edad del empleado. 

Attrition: Indica si el empleado ha dejado la empresa ("No" significa que no ha dejado la empresa y "Yes" significa que ha dejado la empresa).

BusinessTravel: Describe la frecuencia de los viajes relacionados con el trabajo del empleado (por ejemplo, "Travel_Rarely" para raramente).

DailyRate: La tarifa diaria del empleado.

Department: El departamento en el que trabaja el empleado (por ejemplo, "Research & Development", "Sales", etc.).

DistanceFromHome: La distancia desde el hogar del empleado hasta su lugar de trabajo.

Education: Nivel de educación del empleado (generalmente en una escala del 1 al 5).

EducationField: El campo de educación del empleado.

EmployeeCount: Un contador que generalmente es 1 y se usa para contar empleados.

EmployeeNumber: Un número de identificación único para el empleado.

EnvironmentSatisfaction: Nivel de satisfacción del empleado en relación con su entorno de trabajo. Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción.

Gender: El género del empleado. Donde 0 corresponde con "hombre" y 1 con "mujer".

HourlyRate: La tarifa por hora del empleado.

JobInvolvement: Nivel de implicación del empleado en su trabajo.

JobLevel: Nivel jerárquico del empleado en la empresa.

JobRole: El rol o puesto de trabajo del empleado.

JobSatisfaction: Nivel de satisfacción del empleado con su trabajo.

MaritalStatus: El estado civil del empleado (por ejemplo, "Single", "Married", etc.).

MonthlyIncome: Ingresos mensuales del empleado.

MonthlyRate: Tasa mensual del empleado.

NumCompaniesWorked: Número de compañías en las que el empleado ha trabajado.

Over18: Indica si el empleado es mayor de 18 años.

OverTime: Indica si el empleado trabaja horas extras ("Yes" para sí o "No" para no).

PercentSalaryHike: El porcentaje de aumento salarial del empleado.

PerformanceRating: Calificación de rendimiento del empleado.

RelationshipSatisfaction: Nivel de satisfacción en las relaciones interpersonales del empleado.

StandardHours: Las horas estándar de trabajo.

StockOptionLevel: Nivel de opciones de compra de acciones del empleado.

TotalWorkingYears: Total de años de experiencia laboral del empleado.

TrainingTimesLastYear: Número de veces que el empleado recibió capacitación el año pasado.

WorkLifeBalance: Equilibrio entre trabajo y vida personal del empleado.

YearsAtCompany: Años que el empleado ha trabajado en la empresa actual.

YearsInCurrentRole: Años que el empleado ha estado en su puesto actual.

YearsSinceLastPromotion: Años desde la última promoción del empleado.

YearsWithCurrManager: Años que el empleado ha estado bajo la supervisión del actual gerente.

SameAsMonthlyIncome: Ingresos mensuales del empleado.

DateBirth: Año de nacimiento del empleado (teniendo en cuenta que los datos fueron recogidos en el 2023)

Salary: Salario de los empleados.

RoleDepartament: El departamento y el rol del empleado.

NumberChildren: Número de hijos de los empleados.

RemoteWork: Si el empleado puede teletrabajar o no. */

CREATE SCHEMA Abc_Corporation;

-- Datos empleado

/*CREATE TABLE employees (
EmployeeNumber INT NOT NULL PRIMARY KEY, --> Se puede utilizar como id de empleado.
age  --> La edad del empleado
gender --> El género del empleado. Donde 0 corresponde con "hombre" y 1 con "mujer".
DateBirth --> Año de nacimiento del empleado (teniendo en cuenta que los datos fueron recogidos en el 2023)
NumberChildren --> Número de hijos de los empleados.
marital_status -- > El estado civil del empleado (por ejemplo, "Single", "Married", etc.).
over_18 --> Indica si el empleado es mayor de 18 años. Creo que se puede eliminar porque no aporta nada
attrition --> Indica si el empleado ha dejado la empresa ("No" significa que no ha dejado la empresa y "Yes" 
			  significa que ha dejado la empresa).
 );

CREATE TABLE employees_details (
employee_number FK
id_department FK
JobRole --> El rol o puesto de trabajo del empleado.
remote_work --> Si el empleado puede teletrabajar o no.
distance_from_home --> La distancia desde el hogar del empleado hasta su lugar de trabajo.
standard_hours --> Las horas estándar de trabajo.
overtime --> Indica si el empleado trabaja horas extras ("Yes" para sí o "No" para no).
business_travel --> Describe la frecuencia de los viajes relacionados con el trabajo del empleado 
					(por ejemplo, "Travel_Rarely" para raramente).
stock_option_level --> Nivel de opciones de compra de acciones del empleado.
); 

CREATE TABLE departments (
id_department PK
department -->  El departamento en el que trabaja el empleado (por ejemplo, "Research & Development", "Sales", etc.).
);

CREATE TABLE Education (
id_education --> PK
education --> Nivel de educación del empleado (generalmente en una escala del 1 al 5).
education_field --> El campo de educación del empleado.
EmployeeNumber FK
);

CREATE TABLE salaries (
EmployeeNumber FK
daily_rate --> La tarifa diaria del empleado.
hourly_rate --> La tarifa por hora del empleado.
monthly_income --> Ingresos mensuales del empleado.
monthly_rate --> Tasa mensual del empleado.
percent_salary_hike --> El porcentaje de aumento salarial del empleado.
salary --> Salario de los empleados.
same_as_monthly_income -->
);

CREATE TABLE satisfaction(
EmployeeNumber FK -->
environment_satisfaction --> Nivel de satisfacción del empleado en relación con su entorno de trabajo. 
							Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de 
							máxima satisfacción.
job_involvement --> Nivel de implicación del empleado en su trabajo.
job_satisfaction --> Nivel de satisfacción del empleado con su trabajo.
performance_rating --> Calificación de rendimiento del empleado.
relationship_satisfaction --> Nivel de satisfacción en las relaciones interpersonales del empleado.
work_life_balance -->  Equilibrio entre trabajo y vida personal del empleado.
);

CREATE TABLE cv_details(
EmployeeNumber FK -->
num_companies_worked --> Número de compañías en las que el empleado ha trabajado.
training_times_last_year --> Número de veces que el empleado recibió capacitación el año pasado.
total_working_years --> Total de años de experiencia laboral del empleado.
years_at_company --> Años que el empleado ha trabajado en la empresa 
years_in_current_role -->  Años que el empleado ha estado en su puesto actual.
years_since_last_promotion --> Años desde la última promoción del empleado.
years_with_curr_manager --> Años que el empleado ha estado bajo la supervisión del actual gerente.

);
*/


