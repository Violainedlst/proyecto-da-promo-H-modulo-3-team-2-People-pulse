CREATE SCHEMA Abc_Corporation;

-- Datos empleado

CREATE TABLE employees (
EmployeeNumber INT NOT NULL PRIMARY KEY, --> Se puede utilizar como id de empleado.
age INT,  --> La edad del empleado
gender INT, --> El género del empleado. Donde 0 corresponde con "hombre" y 1 con "mujer".
DateBirth DATE, --> Año de nacimiento del empleado (teniendo en cuenta que los datos fueron recogidos en el 2023)
NumberChildren INT,  --> Número de hijos de los empleados.
marital_status VARCHAR(20), -- > El estado civil del empleado (por ejemplo, "Single", "Married", etc.).
--over_18 --> Indica si el empleado es mayor de 18 años. Creo que se puede eliminar porque no aporta nada
attrition VARCHAR(2) --> Indica si el empleado ha dejado la empresa ("No" significa que no ha dejado la empresa y "Yes" significa que ha dejado la empresa).
 );

CREATE TABLE employees_details (
employee_number INT NOT NULL,
id_department INT NOT NULL,
JobRole VARCHAR(255), --> El rol o puesto de trabajo del empleado.
remote_work VARCHAR(2),--> Si el empleado puede teletrabajar o no.
distance_from_home INT, --> La distancia desde el hogar del empleado hasta su lugar de trabajo.
standard_hours INT, --> Las horas estándar de trabajo.
overtime VARCHAR(5), --> Indica si el empleado trabaja horas extras ("Yes" para sí o "No" para no).
business_travel VARCHAR(100), --> Describe la frecuencia de los viajes relacionados con el trabajo del empleado (por ejemplo, "Travel_Rarely" para raramente).
stock_option_level INT, --> Nivel de opciones de compra de acciones del empleado.
employee_number INT NOT NULL
); 

CREATE TABLE departments (
id_department NOT NULL AUTO_INCREMENT PRIMARY KEY,
department VARCHAR(100) -->  El departamento en el que trabaja el empleado (por ejemplo, "Research & Development", "Sales", etc.).
);

CREATE TABLE Education (
id_education NOT NULL AUTO_INCREMENT PRIMARY KEY ,
education VARCHAR(100), --> Nivel de educación del empleado (generalmente en una escala del 1 al 5).
education_field VARCHAR(100), --> El campo de educación del empleado.
EmployeeNumber FK
);

CREATE TABLE salaries (
EmployeeNumber INT NOT NULL,
monthly_income DECIMAL(10, 2), --> Ingresos mensuales del empleado.
monthly_rate DECIMAL(10, 2), --> Tasa mensual del empleado.
daily_rate DECIMAL(10, 2), --> La tarifa diaria del empleado.
hourly_rate DECIMAL(10, 2),--> La tarifa por hora del empleado.
percent_salary_hike DECIMAL(5, 2),--> El porcentaje de aumento salarial del empleado.
salary DECIMAL(10, 2), --> Salario de los empleados.
FOREIGN KEY EmployeeNumber references employees (EmployeeNumber)
);

CREATE TABLE satisfaction(
EmployeeNumber INT NOT NULL,
environment_satisfaction INT, --> Nivel de satisfacción del empleado en relación con su entorno de trabajo.Con valores 
                              -- que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción.
job_involvement INT, --> Nivel de implicación del empleado en su trabajo.
job_satisfaction INT, --> Nivel de satisfacción del empleado con su trabajo.
performance_rating INT, --> Calificación de rendimiento del empleado.
relationship_satisfaction INT,  --> Nivel de satisfacción en las relaciones interpersonales del empleado.
work_life_balance INT,-->  Equilibrio entre trabajo y vida personal del empleado.
FOREIGN KEY EmployeeNumber references employees (EmployeeNumber)
);

CREATE TABLE cv_details(
EmployeeNumber INT NOT NULL,
num_companies_worked INT, --> Número de compañías en las que el empleado ha trabajado.
training_times_last_year INT, --> Número de veces que el empleado recibió capacitación el año pasado.
total_working_years INT,--> Total de años de experiencia laboral del empleado.
years_at_company INT,--> Años que el empleado ha trabajado en la empresa 
years_in_current_role INT, -->  Años que el empleado ha estado en su puesto actual.
years_since_last_promotion INT,--> Años desde la última promoción del empleado.
years_with_curr_manager INT --> Años que el empleado ha estado bajo la supervisión del actual gerente.
FOREIGN KEY EmployeeNumber references employees (EmployeeNumber)

);