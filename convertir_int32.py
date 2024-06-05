import pandas as pd

def convertir_df(data):
    # Verificar la información inicial del DataFrame
    print("Información inicial del DataFrame:")
    print(data.info())
    # Lista de columnas a convertir
    columnas_convertidas = ["hourly_rate","work_life_balance","age","daily_rate","distance_from_home","education", "employee_number", "environment_satisfaction", "job_involvement", "job_level", "job_satisfaction", "monthly_rate", "num_companies_worked", "percent_salary_hike", "relationship_satisfaction", "stock_option_level", "training_times_last_year", "total_working_years","years_at_company", "years_since_last_promotion", "years_with_curr_manager", "year_birth"]
    #Verificar que las columnas existen en el DataFrame
    for col in columnas_convertidas:
        if col in data.columns:
            print(f"Columna {col} existe y es de tipo: {data[col].dtype}")
        else:
            print(f"Columna {col} no existe en el DataFrame")
    #Convertir a int32 solo las columnas que existen
    for col in columnas_convertidas:
        if col in data.columns:
            try:
                data[col] = data[col].apply(lambda x: int(x) if not pd.isna(x) else x)
                data[col] = data[col].astype(int)
                data[col].dtype
                print(f"Columna {col} convertida a int nativo de Python")
            except Exception as e:
                print(f"Error al convertir la columna {col}: {e}")
    # Verificar la información del DataFrame después de la conversión
    print("Información del DataFrame después de la conversión:")
    print(data.info())  
    return data
