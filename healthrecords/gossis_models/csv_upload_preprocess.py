import os
import pandas as pd
from healthrecords.gossis_models.gossis_module import Patient_DB, Patient


def summarize(obj, purpose):
    if isinstance(obj, Patient_DB):
        db = obj
        print(purpose)
    else:
        db = Patient_DB(obj)  # What if this errors?  How could it error?
        print(purpose)
    if purpose == "upload":
        title = "Upload Summary"
        place = "Uploaded"
    elif purpose == "imputation":
        title = "Imputation Summary"
        place = "Imputed"
    db_summary = {
        "Number of Patients " + place + "Successfully": len(db),
        "Number of Variables": len(db.columns),
        "Errors": 0
    }
    return title, db_summary
