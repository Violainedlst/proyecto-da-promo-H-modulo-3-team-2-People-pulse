# 📊 Propuesta Mábel: Estructura MySQL en Python

### Esquema de Base de Datos

```python
import mysql.connector  # Importa el conector MySQL para Python

def create_database():
    # Conecta a MySQL usando las credenciales proporcionadas
    conn = mysql.connector.connect(
        host="your_host",  # Reemplaza con el nombre del host de tu servidor MySQL
        user="your_username",  # Reemplaza con tu nombre de usuario de MySQL
        password="your_password"  # Reemplaza con tu contraseña de MySQL
    )
    cursor = conn.cursor()  # Crea un cursor para ejecutar comandos SQL

    # Crea una base de datos llamada 'people_pulse' si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS people_pulse")
    cursor.execute("USE people_pulse")  # Usa la base de datos 'people_pulse'

    # Crea la tabla 'employees' si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INT PRIMARY KEY AUTO_INCREMENT,  # ID único para cada empleado
            age INT,  # Edad del empleado
            attrition VARCHAR(3),  # Si el empleado sigue en la empresa ('Yes' o 'No')
            business_travel VARCHAR(20),  # Frecuencia de viajes de negocios
            daily_rate INT,  # Tarifa diaria del empleado
            department VARCHAR(50),  # Departamento del empleado
            distance_from_home INT,  # Distancia desde casa al trabajo
            education INT,  # Nivel educativo
            education_field VARCHAR(50),  # Campo de estudio
            employee_count INT,  # Contador de empleados (valor constante)
            employee_number INT,  # Número único de empleado
            environment_satisfaction INT,  # Satisfacción con el entorno
            gender VARCHAR(10),  # Género del empleado
            hourly_rate INT,  # Tarifa por hora del empleado
            job_involvement INT,  # Grado de involucramiento en el trabajo
            job_level INT,  # Nivel del trabajo
            job_role VARCHAR(50),  # Rol del trabajo
            job_satisfaction INT,  # Satisfacción con el trabajo
            marital_status VARCHAR(20),  # Estado civil
            monthly_income INT,  # Ingreso mensual
            monthly_rate INT,  # Tarifa mensual
            num_companies_worked INT,  # Número de empresas en las que ha trabajado
            over_18 VARCHAR(3),  # Si el empleado es mayor de 18 años
            overtime VARCHAR(5),  # Si el empleado trabaja horas extras
            percent_salary_hike INT,  # Incremento porcentual de salario
            performance_rating INT,  # Calificación de rendimiento
            relationship_satisfaction INT,  # Satisfacción con las relaciones
            standard_hours INT,  # Horas estándar de trabajo
            stock_option_level INT,  # Nivel de opciones sobre acciones
            total_working_years INT,  # Total de años trabajando
            training_times_last_year INT,  # Veces que se ha entrenado el año pasado
            work_life_balance INT,  # Equilibrio entre trabajo y vida personal
            years_at_company INT,  # Años en la empresa
            years_in_current_role INT,  # Años en el rol actual
            years_since_last_promotion INT,  # Años desde la última promoción
            years_with_curr_manager INT,  # Años con el manager actual
            date_birth DATE,  # Fecha de nacimiento
            salary VARCHAR(20),  # Salario del empleado
            role_department VARCHAR(100),  # Rol y departamento del empleado
            number_children INT,  # Número de hijos
            remote_work VARCHAR(5)  # Si trabaja de forma remota
        )
    ''')

    # Crea la tabla 'satisfaction_levels' si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS satisfaction_levels (
            employee_id INT PRIMARY KEY,  # ID único para cada registro (coincide con 'employee_id')
            environment_satisfaction INT,  # Satisfacción con el entorno
            job_satisfaction INT,  # Satisfacción con el trabajo
            relationship_satisfaction INT,  # Satisfacción con las relaciones
            work_life_balance INT,  # Equilibrio entre trabajo y vida personal
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)  # Relación con la tabla 'employees'
        )
    ''')

    conn.commit()  # Confirma los cambios en la base de datos
    cursor.close()  # Cierra el cursor
    conn.close()  # Cierra la conexión con la base de datos

# Ejecutar la función para crear la base de datos y tablas
create_database()  # Llama a la función para crear la base de datos y tablas
```
