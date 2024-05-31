from django.shortcuts import render
from .forms import Uploadfile
import pandas as pd
# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = Uploadfile(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)#read excel file
            data = df.to_html()# display data to html
            return render(request, 'display_table.html', {'data': data})
    else:
        form = Uploadfile()
    return render(request, 'home.html', {'form': form})