from django.shortcuts import render, HttpResponse
from healthrecords.forms import PatientForm, CSVForm
from healthrecords.gossis_models.imputation import impute_csv
from healthrecords.gossis_models.csv_upload_preprocess import summarize


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            imputed_db = impute_csv(r"C:\Users\Tyrone\PycharmProjects\healthdata\healthrecords\gossis_models\xgb_bin", file)
            upload_title, upload_summary = summarize(file, "upload")
            imputation_title, imputation_summary = summarize(imputed_db, "imputation")
            html_db = imputed_db.to_html()
            # Make the data passing more discrete
            return render(request, 'healthrecords/input_data_process.html', {'table_title': "Imputed Database", 'html_file': html_db, 'upload_summary': upload_summary, 'upload_title': upload_title, 'imputation_summary': imputation_summary, 'imputation_title': imputation_title})
            # return render(request, 'healthrecords/patients-data.html', {'inputted_data': form.cleaned_data})  # form.cleaned_data is a dictionary
    else:
        form = CSVForm()
    return render(request, 'healthrecords/index.html', {'form': form})

    # if request.method == 'POST':
    #     form = PatientForm(request.POST)
    #     csvform = CSVForm()
    #     if csvform.is_valid():
    #         return HttpResponse("Nice job!")
    #         # return render(request, 'healthrecords/patients-data.html', {'inputted_data': form.cleaned_data})
    #     else:
    #         return render(request, 'healthrecords/index.html', {'form': form, 'csvform': csvform})
    # else:
    #     form = PatientForm()
    #     csvform = CSVForm()
    #     return render(request, 'healthrecords/index.html', {'form': form, 'csvform': csvform})


def contact(request):
    return render(request, 'healthrecords/contact.html')

def patient(request):
    return HttpResponse("Form submitted correctly")

def about(request):
    return render(request, 'healthrecords/about.html')
