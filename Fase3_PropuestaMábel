# 📊 Propuesta Mábel: Estructura MySQL en Python

### Esquema de Base de Datos

```python
import mysql.connector

def create_database():
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS people_pulse")
    cursor.execute("USE employees_db")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INT PRIMARY KEY,
            age INT,
            attrition VARCHAR(3),
            business_travel VARCHAR(20),
            daily_rate INT,
            department VARCHAR(50),
            distance_from_home INT,
            education INT,
            education_field VARCHAR(50),
            employee_count INT,
            employee_number INT,
            environment_satisfaction INT,
            gender VARCHAR(10),
            hourly_rate INT,
            job_involvement INT,
            job_level INT,
            job_role VARCHAR(50),
            job_satisfaction INT,
            marital_status VARCHAR(20),
            monthly_income INT,
            monthly_rate INT,
            num_companies_worked INT,
            over_18 VARCHAR(3),
            overtime VARCHAR(5),
            percent_salary_hike INT,
            performance_rating INT,
            relationship_satisfaction INT,
            standard_hours INT,
            stock_option_level INT,
            total_working_years INT,
            training_times_last_year INT,
            work_life_balance INT,
            years_at_company INT,
            years_in_current_role INT,
            years_since_last_promotion INT,
            years_with_curr_manager INT,
            date_birth DATE,
            salary VARCHAR(20),
            role_department VARCHAR(100),
            number_children INT,
            remote_work VARCHAR(5)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS satisfaction_levels (
            employee_id INT PRIMARY KEY,
            environment_satisfaction INT,
            job_satisfaction INT,
            relationship_satisfaction INT,
            work_life_balance INT,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

# Ejecutar la función para crear la base de datos y tablas
create_database()
```

---

