CREATE SCHEMA abc_Corporation;
USE abc_Corporation;

-- Datos empleado

CREATE TABLE employees (
employee_number INT NOT NULL PRIMARY KEY, 
age INT,                    -- > La edad del empleado
gender VARCHAR(6),          -- > El género del empleado. Male o Female.
year_birth INT,             -- > Año de nacimiento del empleado (teniendo en cuenta que los datos fueron recogidos en el 2023)
marital_status VARCHAR(20), -- > El estado civil del empleado (por ejemplo, "Single", "Married", etc.).
attrition VARCHAR(3)        -- > Indica si el empleado ha dejado la empresa ("No" significa que no ha dejado la empresa y "Yes" significa que ha dejado la empresa).
);


CREATE TABLE employees_details (
employee_number INT NOT NULL,
department VARCHAR(50),
job_role VARCHAR(100),         -- > El rol o puesto de trabajo del empleado.
remote_work VARCHAR(3),        -- > Si el empleado puede teletrabajar o no.(Yes o No)
distance_from_home INT,        -- > La distancia desde el hogar del empleado hasta su lugar de trabajo.
overtime VARCHAR(3),           -- > Indica si el empleado trabaja horas extras ("Yes" para sí o "No" para no).
business_travel VARCHAR(50),   -- > Describe la frecuencia de los viajes relacionados con el trabajo del empleado (por ejemplo, "Travel_Rarely" para raramente).
stock_option_level INT,        -- > Nivel de opciones de compra de acciones del empleado.
FOREIGN KEY (employee_number) REFERENCES employees (employee_number)

); 

CREATE TABLE Education (
employee_number INT NOT NULL,
education INT,       -- > Nivel de educación del empleado (generalmente en una escala del 1 al 5).
education_field VARCHAR(50), -- > El campo de educación del empleado.
FOREIGN KEY (employee_number) REFERENCES employees (employee_number)
);

CREATE TABLE salaries (
employee_number INT NOT NULL,
monthly_income DECIMAL(8, 2),      -- > Ingresos mensuales del empleado.
monthly_rate INT,                  -- > Tasa mensual del empleado.
hourly_rate INT,                   -- > La tarifa por hora del empleado.
percent_salary_hike INT, -- > El porcentaje de aumento salarial del empleado.
FOREIGN KEY (employee_number) REFERENCES employees (employee_number)
);

CREATE TABLE satisfaction(
employee_number INT NOT NULL,
environment_satisfaction INT,    -- > Nivel de satisfacción del empleado en relación con su entorno de trabajo. Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción.
job_involvement INT,             -- > Nivel de implicación del empleado en su trabajo.
job_satisfaction INT,            -- > Nivel de satisfacción del empleado con su trabajo.
relationship_satisfaction INT,   -- > Nivel de satisfacción en las relaciones interpersonales del empleado.
work_life_balance INT,           -- > Equilibrio entre trabajo y vida personal del empleado.
FOREIGN KEY (employee_number) REFERENCES employees (employee_number)
);

CREATE TABLE cv_details(
employee_number INT NOT NULL,
num_companies_worked INT,        -- > Número de compañías en las que el empleado ha trabajado.
training_times_last_year INT,    -- > Número de veces que el empleado recibió capacitación el año pasado.
total_working_years INT,         -- > Total de años de experiencia laboral del empleado.
years_at_company INT,            -- > Años que el empleado ha trabajado en la empresa 
years_since_last_promotion INT,  -- > Años desde la última promoción del empleado.
years_with_curr_manager INT,     -- > Años que el empleado ha estado bajo la supervisión del actual gerente.
FOREIGN KEY (employee_number) REFERENCES employees (employee_number)
);
