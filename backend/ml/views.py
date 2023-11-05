from django.shortcuts import render
from joblib import load

model = load('./savedmodels/maintenance_duration_model.pkl')


def index(request):
    return render(request, 'index.html')


def result(request):
    year = request.GET['year']
    km_driven = request.GET['km_driven']
    selling_price = request.GET['selling_price']

    y_pred = model.predict([[year, km_driven, selling_price]])

    return render(request, 'result.html', {'year': year, 'km_driven': km_driven, 'selling_price': selling_price, 'result': y_pred})
