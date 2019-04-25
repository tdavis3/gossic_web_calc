import os
import unittest
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
    return imputed_db


class Imputation_Test(unittest.TestCase):
    def test_imputation(self):
        # Edge cases like what if a db is all nans
        # If probabilities are negative
        models = load_imputation_models(
            r"C:\Users\Tyrone\PycharmProjects\healthdata\healthrecords\gossis_models\xgb_bin")
        db_given = Patient_DB(
            r"C:\Users\Tyrone\PycharmProjects\healthdata\healthrecords\gossis_models\gossis_calc-master\out.csv")
        db_test = Patient_DB(
            r"C:\Users\Tyrone\PycharmProjects\healthdata\healthrecords\gossis_models\gossis_calc-master\out_test.csv")
        db_to_test_on = Patient_DB(r"C:\Users\Tyrone\Downloads\db_to_test_on.csv")
        imputed_db = impute_db(db_given, db_test.columns, models)
        self.assertEqual(imputed_db, db_to_test_on)
