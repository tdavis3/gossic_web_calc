import numpy as np
import pandas as pd
import xgboost as xgb


class Patient_DB:

    def __init__(self, df_csv=None, columns=None):
        # if columns is None:
        #     self.columns = columns
        if df_csv is None:
            self.db = pd.DataFrame(columns=columns)
            self.columns = columns
            self.length = len(self.db)  # Number of rows
        else:
            self.db = pd.read_csv(df_csv)
            self.columns = self.db.columns

    def __len__(self):
        return len(self.db.index)

    def __iter__(self):
        for row in self.db.itertuples():
            yield row

    def __eq__(self, other):  # Does not work because of float precision.
        return self.db.equals(other.db)

    def add(self, row: np.ndarray):
        self.db.loc[self.length] = row
        self.length += 1

    def drop_row(self, index):
        self.db = self.db.drop(self.db.index[index])
        self.length -= 1

    def drop_col(self, index):
        self.db = self.db.drop(self.db.columns[[index]], axis=1)

    def download(self):
        self.db.to_csv(r"C:\Users\Tyrone\Downloads\db_to_test_on.csv", index=False)

    def to_html(self):
        return self.db.to_html()

    def preprocess(self):
        # bounds = {"heartrate": (0, 400), "temperature": (25, 46), "": (), "": ()}
        # if var >= val and var <= val1:
        #     pass
        # else:
        #     raise ValueError
        pass



class Patient:
    impute_variables = sorted(["d1_diasbp_max", "d1_diasbp_min", "d1_heartrate_max", "d1_heartrate_min", "d1_mbp_max",
                               "d1_mbp_min", "d1_resprate_max", "d1_resprate_min", "d1_spo2_max", "d1_spo2_min",
                               "d1_sysbp_max", "d1_sysbp_min", "d1_temp_max", "d1_temp_min",
                               "d1_albumin_max", "d1_albumin_min", "d1_bilirubin_max", "d1_bilirubin_min", "d1_bun_max",
                               "d1_bun_min", "d1_calcium_max", "d1_calcium_min", "d1_creatinine_max", "d1_glucose_max",
                               "d1_glucose_min", "d1_hco3_max", "d1_hco3_min", "d1_hemaglobin_max", "d1_hemaglobin_min",
                               "d1_hematocrit_max", "d1_hematocrit_min", "d1_inr_max", "d1_inr_min", "d1_lactate_max",
                               "d1_lactate_min", "d1_platelets_max", "d1_platelets_min", "d1_potassium_max",
                               "d1_potassium_min", "d1_sodium_max", "d1_sodium_min", "d1_wbc_max", "d1_wbc_min",
                               "d1_arterial_pco2_max", "d1_arterial_pco2_min", "d1_arterial_ph_max",
                               "d1_arterial_ph_min",
                               "d1_arterial_po2_max", "d1_arterial_po2_min", "d1_pao2fio2ratio_max",
                               "d1_pao2fio2ratio_min",
                               "d1_creatinine_range", "dcs_group", "elective_surgery", "hepatic_failure", "age", "vent",
                               "aids", "cirrhosis", "diabetes_mellitus", "lymphoma",
                               "solid_tumor_with_metastasis"])
    len_impute_vars = len(impute_variables)
    ordered_input_variables = ["d1_diasbp_max", "d1_diasbp_min", "d1_heartrate_max", "d1_heartrate_min",
                               "d1_mbp_max", "d1_mbp_min", "d1_resprate_max", "d1_resprate_min",
                               "d1_spo2_max", "d1_spo2_min", "d1_sysbp_max", "d1_sysbp_min",
                               "d1_temp_max", "d1_temp_min", "d1_albumin_max", "d1_albumin_min",
                               "d1_bilirubin_max", "d1_bilirubin_min", "d1_bun_max", "d1_bun_min",
                               "d1_calcium_max", "d1_calcium_min", "d1_creatinine_max", "d1_glucose_max",
                               "d1_glucose_min", "d1_hco3_max", "d1_hco3_min", "d1_hemaglobin_max",
                               "d1_hemaglobin_min", "d1_hematocrit_max", "d1_hematocrit_min",
                               "d1_inr_max", "d1_inr_min", "d1_lactate_max", "d1_lactate_min",
                               "d1_platelets_max", "d1_platelets_min", "d1_potassium_max", "d1_potassium_min",
                               "d1_sodium_max", "d1_sodium_min", "d1_wbc_max", "d1_wbc_min", "d1_arterial_pco2_max",
                               "d1_arterial_pco2_min", "d1_arterial_ph_max", "d1_arterial_ph_min",
                               "d1_arterial_po2_max", "d1_arterial_po2_min", "d1_pao2fio2ratio_max",
                               "d1_pao2fio2ratio_min", "d1_creatinine_range", "albumin_apache",
                               "arf_apache", "bilirubin_apache", "bun_apache", "creatinine_apache",
                               "fio2_apache", "glucose_apache", "heart_rate_apache", "hematocrit_apache",
                               "intubated_apache", "map_apache", "paco2_apache", "paco2_for_ph_apache",
                               "pao2_apache", "ph_apache", "resprate_apache", "sodium_apache",
                               "temp_apache", "ventilated_apache", "wbc_apache", "dcs_groupALL_LOW",
                               "dcs_groupINTERM_DCS", "dcs_groupSOME_HIGH", "groupGastrointestinal",
                               "groupGenitourinary", "groupGynecological", "groupHematological",
                               "groupMetabolic", "groupMusculoskeletal/Skin", "groupNeurological",
                               "groupOther medical disorders", "groupRespiratory", "groupSepsis",
                               "groupTrauma", "icu_admit_sourceAccident & Emergency", "icu_admit_sourceFloor",
                               "icu_admit_sourceOperating Room / Recovery", "icu_admit_sourceOther Hospital",
                               "icu_admit_sourceOther ICU", "icu_typeCardiac ICU", "icu_typeCCU",
                               "icu_typeCCU-CTICU", "icu_typeCSICU", "icu_typeCSRU", "icu_typeCTICU",
                               "icu_typeMed-Surg ICU", "icu_typeMICU", "icu_typeNeuro ICU",
                               "icu_typeSICU", "icu_typeTSICU", "elective_surgery", "age", "dx_class101",
                               "dx_class102", "dx_class103", "dx_class104", "dx_class105", "dx_class106",
                               "dx_class107", "dx_class108", "dx_class109", "dx_class110", "dx_class1101",
                               "dx_class1102", "dx_class111", "dx_class1202", "dx_class1203",
                               "dx_class1204", "dx_class1205", "dx_class1206", "dx_class1207",
                               "dx_class1208", "dx_class1209", "dx_class1210", "dx_class1211",
                               "dx_class1212", "dx_class1213", "dx_class1301", "dx_class1302",
                               "dx_class1303", "dx_class1304", "dx_class1401", "dx_class1403",
                               "dx_class1404", "dx_class1405", "dx_class1406", "dx_class1407",
                               "dx_class1408", "dx_class1409", "dx_class1410", "dx_class1411",
                               "dx_class1412", "dx_class1413", "dx_class1501", "dx_class1502",
                               "dx_class1503", "dx_class1504", "dx_class1505", "dx_class1506",
                               "dx_class1601", "dx_class1602", "dx_class1603", "dx_class1604",
                               "dx_class1605", "dx_class1701", "dx_class1703", "dx_class1704",
                               "dx_class1705", "dx_class1801", "dx_class1802", "dx_class1803",
                               "dx_class1902", "dx_class1903", "dx_class1904", "dx_class201",
                               "dx_class202", "dx_class203", "dx_class204", "dx_class206", "dx_class207",
                               "dx_class208", "dx_class209", "dx_class210", "dx_class2101",
                               "dx_class211", "dx_class212", "dx_class213", "dx_class2201",
                               "dx_class301", "dx_class303", "dx_class305", "dx_class306", "dx_class307",
                               "dx_class308", "dx_class309", "dx_class310", "dx_class311", "dx_class312",
                               "dx_class313", "dx_class401", "dx_class402", "dx_class403", "dx_class404",
                               "dx_class405", "dx_class406", "dx_class407", "dx_class408", "dx_class409",
                               "dx_class410", "dx_class501", "dx_class502", "dx_class503", "dx_class504",
                               "dx_class601", "dx_class602", "dx_class603", "dx_class604", "dx_class605",
                               "dx_class701", "dx_class702", "dx_class703", "dx_class704", "dx_class801",
                               "dx_class802", "dx_class901", "dx_class902", "dx_class903", "dx_class99",
                               "vent", "aids", "cirrhosis", "diabetes_mellitus", "lymphoma",
                               "solid_tumor_with_metastasis",
                               "hepatic_failure"]  # Variables that imputation model expects in order.
    categorical_vars = {
        "dcs_group": ["ALL_HIGH", "ALL_LOW", "INTERM_DCS", "SOME_HIGH"],
        "group": ["Cardiovascular", "Gastrointestinal", "Genitourinary", "Gynecological",
                  "Hematological", "Metabolic", "Musculoskeletal/Skin", "Neurological",
                  "Other medical disorders", "Respiratory", "Sepsis", "Trauma"],
        "icu_admit_source": ["", "Accident & Emergency", "Floor", "Operating Room / Recovery",
                             "Other Hospital", "Other ICU"],
        "icu_type": ["", "Cardiac ICU", "CCU",
                     "CCU-CTICU", "CSICU", "CSRU",
                     "CTICU", "Med-Surg ICU",
                     "MICU",
                     "Neuro ICU", "SICU", "TSICU"],
        "dx_class": ["1002", "101", "102", "103",
                     "104", "105", "106", "107", "108", "109", "110", "1101",
                     "1102", "111", "1202", "1203", "1204", "1205", "1206", "1207",
                     "1208", "1209", "1210", "1211", "1212", "1213", "1301", "1302",
                     "1303", "1304", "1401", "1403", "1404", "1405", "1406", "1407",
                     "1408", "1409", "1410", "1411", "1412", "1413", "1501", "1502",
                     "1503", "1504", "1505", "1506", "1601", "1602", "1603", "1604",
                     "1605", "1701", "1703", "1704", "1705", "1801", "1802", "1803",
                     "1902", "1903", "1904", "201", "202", "203", "204", "206",
                     "207", "208", "209", "210", "2101", "211", "212", "213",
                     "2201", "301", "303", "305", "306", "307", "308", "309",
                     "310", "311", "312", "313", "401", "402", "403", "404", "405",
                     "406", "407", "408", "409", "410", "501", "502", "503", "504",
                     "601", "602", "603", "604", "605", "701", "702", "703", "704",
                     "801", "802", "901", "902", "903",
                     "99"],
        "aids": ["0", "1"], "cirrhosis": ["0", "1"], "diabetes_mellitus": ["0", "1"], "elective_surgery": ["0", "1"],
        "hepatic_failure": ["0", "1"], "lymphoma": ["0", "1"], "solid_tumor_with_metastasis": ["0", "1"],
        "vent": ["0", "1"]}  # Variables that are categorical and their values.

    def __init__(self, row: tuple, models: dict):
        self.row = row
        self.models = models

    def get_var_value(self, var: str):
        """ Returns the value of the variable/column name or None if var doesn't exist. """
        try:
            val = self.row.__getattribute__(var)
        except:
            val = np.nan
        return val

    @staticmethod
    def categorical(var) -> tuple:
        if var == "ventilated_apache":
            return False, None
        if var in Patient.categorical_vars:  # Might not need this.
            return True, var
        for cvar in Patient.categorical_vars:
            if var.startswith(cvar):
                return True, cvar
        return False, None

    @staticmethod
    def get_category_list(var, val) -> np.ndarray:
        category_list = np.asarray([])
        if pd.isna(val):
            return np.full(len(Patient.categorical_vars[var]) - 1, np.nan)
        elif Patient.categorical_vars[var][0] == str(val):
            return np.full(len(Patient.categorical_vars[var]) - 1, 0)
        for value in Patient.categorical_vars[var][1:]:
            if value != str(val):
                category_list = np.append(category_list, 0)
            else:
                category_list = np.append(category_list, 1)
        return category_list

    def impute_var(self, var_being_imputed):
        columns = []
        result = [tuple()]
        pointer = 0
        while pointer < len(Patient.ordered_input_variables):
            var = Patient.ordered_input_variables[pointer]  # Can be vars with numbers appended to the front.
            categorical, actual_var = Patient.categorical(var)
            if categorical:
                val = self.get_var_value(actual_var)
                category_list = Patient.get_category_list(actual_var, val)
                if var_being_imputed == actual_var:
                    pointer += len(category_list)
                    continue
                result[0] += tuple(category_list)
                if len(category_list) == 1:
                    columns.append(actual_var)
                    pointer += 1
                else:
                    dum = []
                    for title in Patient.categorical_vars[actual_var][1:]:
                        dum.append(actual_var + title)
                    columns += dum
                    pointer += len(category_list)
            if not categorical:
                if var_being_imputed == var:
                    pointer += 1
                    continue
                val = self.get_var_value(var)
                result[0] += (val,)
                columns.append(var)
                pointer += 1
        impute_model_input = pd.DataFrame.from_records(data=result, columns=columns)
        bst = xgb.Booster({'nthread': 2})
        bst.load_model(self.models[var_being_imputed])  # Get the associated model.
        pred = bst.predict(xgb.DMatrix(data=impute_model_input.iloc[[0]]))
        # Preprocess the prediction.
        categorical, actual_var = Patient.categorical(var_being_imputed)
        if categorical:
            print(pred, actual_var)
            if not isinstance(pred[0], np.ndarray):
                if pred[0] > 1 - pred[0]:
                    return 0
                elif 1 - pred[0] > pred[0]:
                    return 1
                # What if they are equal
            else:
                index_of_max = np.argmax(pred)
                cat_pred = Patient.categorical_vars[actual_var][index_of_max]
                return cat_pred
        return pred[0]

    def impute(self):
        columns = np.asarray([])
        result = np.asarray([])
        for var in Patient.impute_variables:
            val = self.get_var_value(var)
            if pd.isna(val):
                prediction = self.impute_var(var)
                result = np.append(result, prediction)
            else:
                result = np.append(result, val)
            # prediction = self.impute_var(var)  # Impute all vars that have models
            # result = np.append(result, prediction)
            columns = np.append(columns, var)
        return result
