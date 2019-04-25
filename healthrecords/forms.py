from django import forms


class PatientForm(forms.Form):
    sodium = forms.FloatField(label='Sodium (mEq/L)', initial=140)
    temp = forms.FloatField(label='Temperature (C)', initial=37)
    creatinine = forms.FloatField(label='Creatinine (mg/dL)', initial=1)
    bilirubin = forms.FloatField(label='Bilirubin (mg/dL)', initial=1)
    albumin = forms.FloatField(label='Albumin (g/L)', initial=40)
    arterial_ph = forms.FloatField(label='Arterial pH', initial=7.4)
    arterial_po = forms.FloatField(label='Arterial pO2 (mmHg)', initial=90)
    heartrate = forms.FloatField(label='HeartRate (/min)', initial=80)
    wbc = forms.FloatField(label='WBC (x1000/mm3)', initial=10)
    paofio = forms.FloatField(label='PAO FiO2 (%)')
    resperate = forms.FloatField(label='Resperate')
    potassium = forms.FloatField(label='Potassium')
    platelets = forms.FloatField(label='Platelets')
    lactate = forms.FloatField(label='Lactate')
    hemoglobin = forms.FloatField(label='Hemoglobin')
    glucose = forms.FloatField(label='Glucose')
    calcium = forms.FloatField(label='Calcium')

    # sodium_a = forms.FloatField(label='Sodium (mEq/L)', initial=140)
    # sodium_h= forms.FloatField(label='Sodium (mEq/L)', initial=140)
    # sodium_d= forms.FloatField(label='Sodium (mEq/L)', initial=140)
    # temp_a = forms.FloatField(label='Temperature (C)', initial=37)
    # temp_h = forms.FloatField(label='Temperature (C)', initial=37)
    # temp_d = forms.FloatField(label='Temperature (C)', initial=37)
    # creatinine_a = forms.FloatField(label='Creatinine (mg/dL)', initial=1)
    # creatinine_h = forms.FloatField(label='Creatinine (mg/dL)', initial=1)
    # creatinine_d = forms.FloatField(label='Creatinine (mg/dL)', initial=1)
    # bilirubin_a = forms.FloatField(label='Bilirubin (mg/dL)', initial=1)
    # bilirubin_h = forms.FloatField(label='Bilirubin (mg/dL)', initial=1)
    # bilirubin_d = forms.FloatField(label='Bilirubin (mg/dL)', initial=1)
    # albumin_a = forms.FloatField(label='Albumin (g/L)', initial=40)
    # albumin_h = forms.FloatField(label='Albumin (g/L)', initial=40)
    # albumin_d = forms.FloatField(label='Albumin (g/L)', initial=40)
    # arterial_ph_a = forms.FloatField(label='Arterial pH', initial=7.4)
    # arterial_ph_h = forms.FloatField(label='Arterial pH', initial=7.4)
    # arterial_ph_d = forms.FloatField(label='Arterial pH', initial=7.4)
    # arterial_po_a = forms.FloatField(label='Arterial pO2 (mmHg)', initial=90)
    # arterial_po_h = forms.FloatField(label='Arterial pO2 (mmHg)', initial=90)
    # arterial_po_d = forms.FloatField(label='Arterial pO2 (mmHg)', initial=90)
    # heartrate_a = forms.FloatField(label='HeartRate (/min)', initial=80)
    # heartrate_h = forms.FloatField(label='HeartRate (/min)', initial=80)
    # heartrate_d = forms.FloatField(label='HeartRate (/min)', initial=80)
    # wbc_a = forms.FloatField(label='WBC (x1000/mm3)', initial=10)
    # wbc_h = forms.FloatField(label='WBC (x1000/mm3)', initial=10)
    # wbc_d = forms.FloatField(label='WBC (x1000/mm3)', initial=10)
    # paofio_a = forms.FloatField(label='PAO FiO2 (%)')
    # paofio_h = forms.FloatField(label='PAO FiO2 (%)')
    # paofio_d = forms.FloatField(label='PAO FiO2 (%)')
    # resperate_a = forms.FloatField(label='Resperate')
    # resperate_h = forms.FloatField(label='Resperate')
    # resperate_d = forms.FloatField(label='Resperate')
    # potassium_a = forms.FloatField(label='Potassium')
    # potassium_h = forms.FloatField(label='Potassium')
    # potassium_d = forms.FloatField(label='Potassium')
    # platelets_a = forms.FloatField(label='Platelets')
    # platelets_h = forms.FloatField(label='Platelets')
    # platelets_d = forms.FloatField(label='Platelets')
    # lactate_a = forms.FloatField(label='Lactate')
    # lactate_h = forms.FloatField(label='Lactate')
    # lactate_d = forms.FloatField(label='Lactate')
    # hemoglobin_a = forms.FloatField(label='Hemoglobin')
    # hemoglobin_h = forms.FloatField(label='Hemoglobin')
    # hemoglobin_d = forms.FloatField(label='Hemoglobin')
    # glucose_a = forms.FloatField(label='Glucose')
    # glucose_h = forms.FloatField(label='Glucose')
    # glucose_d = forms.FloatField(label='Glucose')
    # calcium_a = forms.FloatField(label='Calcium')
    # calcium_h = forms.FloatField(label='Calcium')
    # calcium_d = forms.FloatField(label='Calcium')
    #
    # def clean(self):
    #     pass
    
     # class SymptomWidget(forms.MultiWidget):
#     def __init__(self, *args, **kwargs):
#         super(SymptomWidget, self).__init__(*args, **kwargs,
#         widgets = [
#             forms.IntegerField(),
#             forms.IntegerField(),
#             forms.IntegerField()
#         ])
#
#     def decompress(self, value):
#         if value:
#             return value.split(' ')
#         return [None, None]
#
#
# class SymptomField(forms.MultiValueField):
#     widget = SymptomWidget
#
#     def __init__(self, label=None, initial=None):
#         super(SymptomField, self).__init__(label=label, initial=initial,
#         fields = (
#             forms.IntegerField(initial=initial, label='Apache'),
#             forms.IntegerField(initial=initial, label='Hour 1'),
#             forms.IntegerField(initial=initial, label='Day 1')
#         ))
#
#     def compress(self, data_list):
#         return ' '.join(data_list)
#
#
# class PatientForm(forms.ModelForm):
#     sodium = SymptomField(label='Sodium (mEq/L)', initial=140)
#     temp = SymptomField(label='Temperature (C)', initial=37)
#     creatinine = SymptomField(label='Creatinine (mg/dL)', initial=1)
#     bilirubin = SymptomField(label='Bilirubin (mg/dL)', initial=1)
#     albumin = SymptomField(label='Albumin (g/L)', initial=40)
#     arterial_ph = SymptomField(label='Arterial pH', initial=7.4)
#     arterial_po = SymptomField(label='Arterial pO2 (mmHg)', initial=90)
#     heartrate = SymptomField(label='HeartRate (/min)', initial=80)
#     wbc = SymptomField(label='WBC (x1000/mm3)', initial=10)
#     paofio = SymptomField(label='PAO FiO2 (%)')
#     resperate = SymptomField(label='Resperate')
#     potassium = SymptomField(label='Potassium')
#     platelets = SymptomField(label='Platelets')
#     lactate = SymptomField(label='Lactate')
#     hemoglobin = SymptomField(label='Hemoglobin')
#     glucose = SymptomField(label='Glucose')
#     calcium = SymptomField(label='Calcium')

def validate_file_extension(f):
    if not f.name.endswith('.csv'):
        raise forms.ValidationError("Must be a CSV file.")

class CSVForm(forms.Form):
    file = forms.FileField(validators=[validate_file_extension])


