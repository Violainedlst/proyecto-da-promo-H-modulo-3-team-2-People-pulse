import pandas as pd

# Leer el fichero csv desde GitHub
url = "https://raw.githubusercontent.com/Violainedlst/proyecto-da-promo-H-modulo-3-team-2-People-pulse/main/CSVs/HR_RAW_DATA.csv"
data_bruto = pd.read_csv(url)

# Para ver el fichero entero
pd.set_option('display.max_columns', None)

# Listas a utilizar posteriormente
columns_to_drop = ["id", "same_as_monthly_income", "employee_count", "salary", "standard_hours", "over_18", 
                   "performance_rating", "number_children", "years_in_current_role"]
columns_with_commas = ['daily_rate', 'monthly_income', 'employee_number', 'total_working_years', 
                       'work_life_balance']
replacements = {'forty-seven': '47', 'fifty-eight': '58', 'thirty-six': '36', 'fifty-five': '55', 'fifty-two': '52', 
                'thirty-one': '31', 'thirty': '30',
                    'twenty-six': '26', 'thirty-seven': '37', 'thirty-two': '32', 'twenty-four': '24'}
columns_to_int = [
        'age', 'year_birth', 'employee_number', 'distance_from_home', 'stock_option_level', 'education',
        'monthly_rate', 'hourly_rate', 'percent_salary_hike', 'environment_satisfaction', 'job_involvement',
        'job_satisfaction', 'relationship_satisfaction', 'work_life_balance', 'num_companies_worked',
        'training_times_last_year', 'total_working_years', 'years_at_company', 'years_since_last_promotion',
        'years_with_curr_manager', 'daily_rate', 'monthly_income'
    ]

# Crea una copia del DataFrame para no actuar directamente sobre el original
data = data_bruto.copy()

data.head(10)


# Convertir los nombres de las columnas en minúsculas
def lowercase_columns(df):
    # Convertir los nombres de las columnas a minúsculas

    df.columns = [column.lower().strip() for column in df.columns]
    return df

# Modificar los nombres de las columnas para mejor comprensión lectora
def rename_columns(df):
    # Renombrar columnas para mayor claridad
    data.rename(columns={
        'unnamed: 0': 'id',
        'businesstravel': 'business_travel',
        'dailyrate': 'daily_rate',
        'distancefromhome': 'distance_from_home',
        'educationfield': 'education_field',
        'employeecount': 'employee_count',
        'employeenumber': 'employee_number',
        'environmentsatisfaction': 'environment_satisfaction',
        'hourlyrate': 'hourly_rate',
        'jobinvolvement': 'job_involvement',
        'joblevel': 'job_level',
        'jobrole': 'job_role',
        'jobsatisfaction': 'job_satisfaction',
        'maritalstatus': 'marital_status',
        'monthlyincome': 'monthly_income',
        'monthlyrate': 'monthly_rate',
        'numcompaniesworked': 'num_companies_worked',
        'over18': 'over_18',
        'overtime': 'overtime',
        'percentsalaryhike': 'percent_salary_hike',
        'performancerating': 'performance_rating',
        'relationshipsatisfaction': 'relationship_satisfaction',
        'standardhours': 'standard_hours',
        'stockoptionlevel': 'stock_option_level',
        'totalworkingyears': 'total_working_years',
        'trainingtimeslastyear': 'training_times_last_year',
        'worklifebalance': 'work_life_balance',
        'yearsatcompany': 'years_at_company',
        'yearsincurrentrole': 'years_in_current_role',
        'yearssincelastpromotion': 'years_since_last_promotion',
        'yearswithcurrmanager': 'years_with_curr_manager',
        'sameasmonthlyincome': 'same_as_monthly_income',
        'datebirth': 'year_birth',
        'roledepartament': 'role_department',
        'numberchildren': 'number_children',
        'remotework': 'remote_work'
    }, inplace=True)
    return df

# Eliminar columnas innecesarias
def drop_unnecessary_columns(df):
    # Definir columnas a eliminar    
    existing_columns_to_drop = [col for col in columns_to_drop if col in df.columns]
    # Eliminar las columnas especificadas
    df = df.drop(columns=existing_columns_to_drop)
    return df

# Rellenamos, de forma consecutiva, nulos en 'employee_number'
def update_employee_numbers(df, column_name):
    # Convertir la columna 'employee_number' a numérico, forzando errores a NaN, y luego a entero
    df['employee_number'] = pd.to_numeric(df['employee_number'].str.replace(',', ''), errors='coerce').fillna(0).astype(int)
    
    # Identificar duplicados en la columna
    duplicados = df.duplicated(subset=column_name, keep=False)
    
    # Obtener los valores únicos actuales
    valores_unicos = set(df[column_name])
    
    # Inicializar un nuevo número que no esté en valores_unicos
    max_valor_actual = max(valores_unicos)
    nuevos_numeros = iter(range(max_valor_actual + 1, max_valor_actual + 1 + duplicados.sum()))
    
    # Asignar nuevos números a las filas duplicadas
    df.loc[duplicados, column_name] = [next(nuevos_numeros) for _ in range(duplicados.sum())]
    
    return df

# Limpiar espacios en blanco en el DataFrame
def strip_whitespace(df):
    # Eliminar espacios en blanco en todo el DataFrame
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df

# Convertir todas las cadenas en el DataFrame a minúsculas
def lowercase_all_strings(df):
    # Convertir todas las cadenas a minúsculas
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.lower()
    return df

# Convertir el DataFrame a tipo string
def convert_to_string(df):
    # Convertir todo el DataFrame a tipo string
    df = df.astype(str)
    return df

# Limpiar valores específicos en columnas
def clean_column_values(df):
    # Limpiar y reemplazar valores específicos en varias columnas
    df['daily_rate'] = df['daily_rate'].str.replace('$', '', regex=False)
    df['business_travel'] = df['business_travel'].str.replace('-', '_', regex=False)
    df['distance_from_home'] = df['distance_from_home'].str.replace('-', '', regex=False)
    df['hourly_rate'] = df['hourly_rate'].str.replace('not available', '0', regex=False)
    df['remote_work'] = df['remote_work'].apply(lambda x: 'yes' if x in ['1', 'true', 'yes'] else 'no')
    df["gender"] = df["gender"].replace({'0': 'male', '1': 'female'})
    data["marital_status"] = data["marital_status"].str.replace('marreid', 'married', regex=False)
    return df

# Reemplazar comas por puntos en ciertas columnas
def replace_commas(df):
    # Reemplazar comas por puntos en ciertas columnas  
    for col in columns_with_commas:
        df[col] = df[col].str.replace(',', '.', regex=False)
    return df

# Rellenar valores nulos y reemplazar 'nan'
def fill_na_values(df):
    # Rellenar valores nulos y reemplazar 'nan'
    df = data.fillna('n/a')
    df = data.replace('nan', 'n/a')
    return df

# Reemplazar ciertos valores de texto en la columna 'age'
def replace_age_values(df):
    # Reemplazar ciertos valores de texto en la columna 'age'    
    df['age'] = df['age'].replace(replacements)
    return df

# Imprimir valores únicos de cada columna
def print_unique_values(df):
    # Imprimir valores únicos de cada columna
    for column in data.columns:
        print(f"Columna: {column}")
        print(df[column].unique())
        print("\n--------------------\n")

# Convertir columnas específicas a tipo int
def convert_columns_to_int(df):
    # Convertir cada columna a int, manejando valores 'n/a'
    for column in columns_to_int:
        df[column] = pd.to_numeric(df[column], errors='coerce')
        mean_value = df[column].mean()
        df[column] = df[column].fillna(mean_value)
        df[column] = df[column].apply(int)
    return df

# Ejecutar funciones en orden
data = lowercase_columns(data)
data = rename_columns(data)
data = drop_unnecessary_columns(data)
data = update_employee_numbers(data)
data = strip_whitespace(data)
data = lowercase_all_strings(data)
data = convert_to_string(data)
data = clean_column_values(data)
data = replace_commas(data)
data = fill_na_values(data)
data = replace_age_values(data)
data = convert_columns_to_int(data)
print_unique_values(data)

# Convertimos el resultado en un csv
data.to_csv('HR_RAW_DATA_LIMPIO.csv')