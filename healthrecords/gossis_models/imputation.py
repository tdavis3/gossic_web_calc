import os
import pandas as pd
from healthrecords.gossis_models.gossis_module import Patient_DB, Patient


def load_imputation_models(models_dir: str) -> dict:
    models = {}
    for file_name in os.listdir(models_dir):
        if file_name not in models:
            models[file_name] = os.path.join(models_dir, file_name)
    return models


def impute_db(db, columns, models):
    imputed_db = Patient_DB(columns=columns)  # New db that will be populated with imputed rows.
    for row in db:
        patient = Patient(row, models)
        imputed_patient = patient.impute()
        imputed_db.add(imputed_patient)
    imputed_db.preprocess()
    return imputed_db


def impute_csv(models, csv):
    loaded_models = load_imputation_models(models)
    db_given = Patient_DB(csv)
    columns = pd.Index(['age', 'aids', 'cirrhosis', 'd1_albumin_max', 'd1_albumin_min',
     'd1_arterial_pco2_max', 'd1_arterial_pco2_min', 'd1_arterial_ph_max',
     'd1_arterial_ph_min', 'd1_arterial_po2_max', 'd1_arterial_po2_min',
     'd1_bilirubin_max', 'd1_bilirubin_min', 'd1_bun_max', 'd1_bun_min',
     'd1_calcium_max', 'd1_calcium_min', 'd1_creatinine_max',
     'd1_creatinine_range', 'd1_diasbp_max', 'd1_diasbp_min',
     'd1_glucose_max', 'd1_glucose_min', 'd1_hco3_max', 'd1_hco3_min',
     'd1_heartrate_max', 'd1_heartrate_min', 'd1_hemaglobin_max',
     'd1_hemaglobin_min', 'd1_hematocrit_max', 'd1_hematocrit_min',
     'd1_inr_max', 'd1_inr_min', 'd1_lactate_max', 'd1_lactate_min',
     'd1_mbp_max', 'd1_mbp_min', 'd1_pao2fio2ratio_max',
     'd1_pao2fio2ratio_min', 'd1_platelets_max', 'd1_platelets_min',
     'd1_potassium_max', 'd1_potassium_min', 'd1_resprate_max',
     'd1_resprate_min', 'd1_sodium_max', 'd1_sodium_min', 'd1_spo2_max',
     'd1_spo2_min', 'd1_sysbp_max', 'd1_sysbp_min', 'd1_temp_max',
     'd1_temp_min', 'd1_wbc_max', 'd1_wbc_min', 'dcs_group',
     'diabetes_mellitus', 'elective_surgery', 'hepatic_failure', 'lymphoma',
     'solid_tumor_with_metastasis', 'vent'])
    imputed_db = impute_db(db_given, columns, loaded_models)
    return imputed_db


if __name__ == "__main__":
    models = load_imputation_models(r"C:\Users\Tyrone\PycharmProjects\healthdata\healthrecords\gossis_models\xgb_bin")
    db_given = Patient_DB(
        r"C:\Users\Tyrone\PycharmProjects\healthdata\healthrecords\gossis_models\gossis_calc-master\out.csv")
    db_test = Patient_DB(
        r"C:\Users\Tyrone\PycharmProjects\healthdata\healthrecords\gossis_models\gossis_calc-master\out_test.csv")
    imputed_db = impute_db(db_given, db_test.columns, models)
    # imputed_db.download()

    """
    Questions:
    
        Implement the imputation the proper way. As of now I impute everything.
        What does the gossis mortality calculator expect as parameters?
        
    Next Steps:
    
        Unit Test the imputation part.
        Preprocess the data to avoid values that are not valid.  Like negative blood pressure, etc.  Look at git repo.
        Finish the django form allowing people to input one patient and csv file (multiple patients).
            - Impute data, if needed
            - Return mortality score
            
    """
