query_creacion_bbdd= """CREATE SCHEMA IF NOT EXISTS `abc_corporation` DEFAULT CHARACTER SET utf8 ;"""

query_creacion_tabla_employees = """
                                CREATE TABLE IF NOT EXISTS abc_corporation.employees (
                                employee_number BIGINT NOT NULL PRIMARY KEY, 
                                age BIGINT,                 -- > La edad del empleado
                                gender VARCHAR(6),          -- > El género del empleado. Male o Female.
                                year_birth BIGINT,          -- > Año de nacimiento del empleado (teniendo en cuenta que los datos fueron recogidos en el 2023)
                                marital_status VARCHAR(20), -- > El estado civil del empleado (por ejemplo, "Single", "Married", etc.).
                                attrition VARCHAR(3)        -- > Indica si el empleado ha dejado la empresa ("No" significa que no ha dejado la empresa y "Yes" significa que ha dejado la empresa).
                                );
                                
                                """

query_creacion_tabla_employees_details = """    
                                        CREATE TABLE abc_corporation.employees_details (
                                        employee_number BIGINT NOT NULL PRIMARY KEY,
                                        department VARCHAR(50),
                                        job_role VARCHAR(100),         -- > El rol o puesto de trabajo del empleado.
                                        remote_work VARCHAR(3),        -- > Si el empleado puede teletrabajar o no.(Yes o No)
                                        distance_from_home BIGINT,        -- > La distancia desde el hogar del empleado hasta su lugar de trabajo.
                                        overtime VARCHAR(3),           -- > Indica si el empleado trabaja horas extras ("Yes" para sí o "No" para no).
                                        business_travel VARCHAR(50),   -- > Describe la frecuencia de los viajes relacionados con el trabajo del empleado (por ejemplo, "Travel_Rarely" para raramente).
                                        stock_option_level BIGINT,       -- > Nivel de opciones de compra de acciones del empleado.
                                        FOREIGN KEY (employee_number) REFERENCES abc_corporation.employees(employee_number)
                                        ); 
                                        
                                        """

query_creacion_tabla_education = """
                                    CREATE TABLE abc_corporation.Education (
                                    employee_number BIGINT,
                                    education BIGINT,       -- > Nivel de educación del empleado (generalmente en una escala del 1 al 5).
                                    education_field VARCHAR(50), -- > El campo de educación del empleado.
                                    FOREIGN KEY (employee_number) REFERENCES abc_corporation.employees(employee_number)
                                    );
                                """

query_creacion_tabla_salaries = """

                                    CREATE TABLE abc_corporation.salaries (
                                    employee_number BIGINT NOT NULL PRIMARY KEY,
                                    monthly_income DECIMAL(8, 2),      -- > Ingresos mensuales del empleado.
                                    monthly_rate BIGINT,                  -- > Tasa mensual del empleado.
                                    hourly_rate BIGINT,                   -- > La tarifa por hora del empleado.
                                    percent_salary_hike BIGINT, -- > El porcentaje de aumento salarial del empleado.
                                    FOREIGN KEY (employee_number) REFERENCES abc_corporation.employees(employee_number)
                                    );
                                
                                """

query_creacion_tabla_satisfaction = """
                                    CREATE TABLE abc_corporation.satisfaction(
                                    employee_number BIGINT NOT NULL PRIMARY KEY,
                                    environment_satisfaction BIGINT,    -- > Nivel de satisfacción del empleado en relación con su entorno de trabajo. Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción.
                                    job_involvement BIGINT,             -- > Nivel de implicación del empleado en su trabajo.
                                    job_satisfaction BIGINT,            -- > Nivel de satisfacción del empleado con su trabajo.
                                    relationship_satisfaction BIGINT,   -- > Nivel de satisfacción en las relaciones interpersonales del empleado.
                                    work_life_balance BIGINT ,          -- > Equilibrio entre trabajo y vida personal del empleado.
                                    FOREIGN KEY (employee_number) REFERENCES abc_corporation.employees(employee_number)
                                    );
                                """

query_creacion_tabla_cv_details = """
                                    CREATE TABLE abc_corporation.cv_details(
                                    employee_number BIGINT NOT NULL PRIMARY KEY,
                                    num_companies_worked BIGINT,        -- > Número de compañías en las que el empleado ha trabajado.
                                    training_times_last_year BIGINT,    -- > Número de veces que el empleado recibió capacitación el año pasado.
                                    total_working_years BIGINT,         -- > Total de años de experiencia laboral del empleado.
                                    years_at_company BIGINT,            -- > Años que el empleado ha trabajado en la empresa 
                                    years_since_last_promotion BIGINT,  -- > Años desde la última promoción del empleado.
                                    years_with_curr_manager BIGINT,     -- > Años que el empleado ha estado bajo la supervisión del actual gerente.
                                    FOREIGN KEY (employee_number) REFERENCES abc_corporation.employees(employee_number)
                                    );
                                """
                                
query_insertar_employees = "INSERT INTO abc_corporation.employees (employee_number,age,gender,year_birth,marital_status,attrition) VALUES (%s,%s,%s,%s,%s,%s)"

query_insertar_employees_details = "INSERT INTO abc_corporation.employees_details (employee_number,department,job_role,remote_work,distance_from_home,overtime,business_travel,stock_option_level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

query_insertar_education = "INSERT INTO abc_corporation.education (employee_number,education,education_field) VALUES (%s,%s,%s)"

query_insertar_salaries = "INSERT INTO abc_corporation.salaries (employee_number,monthly_income,monthly_rate,hourly_rate,percent_salary_hike) VALUES (%s,%s,%s,%s,%s)"

query_insertar_satisfaction = "INSERT INTO abc_corporation.satisfaction (employee_number,environment_satisfaction,job_involvement,job_satisfaction,relationship_satisfaction,work_life_balance) VALUES (%s,%s,%s,%s,%s,%s)"

query_insertar_cv_details = "INSERT INTO abc_corporation.cv_details (employee_number,num_companies_worked,training_times_last_year,total_working_years,years_at_company,years_since_last_promotion,years_with_curr_manager) VALUES (%s,%s,%s,%s,%s,%s,%s)"
