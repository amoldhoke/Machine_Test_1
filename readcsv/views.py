from django.shortcuts import render
from .models import *
import pandas as pd
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect


# HOME
def home(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        obj = File.objects.create(file=file)
        create_db(obj.file)
        messages.success(request, 'File uploaded successfully.')

    all_candidate_list = Customer.objects.order_by('customer_id').all()

    # Pagination
    paginator = Paginator(all_candidate_list, 10)
    page = request.GET.get('page')
    all_candidate = paginator.get_page(page)

    # Context
    context = {
        'customers':all_candidate,
        }
    return render(request, "index.html", context)

# Creates Database from csv
def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]

    for i in list_of_csv:
        Customer.objects.create(
            first_name=i[1],
            last_name=i[2],
            email=i[3],
            mobile=i[4],
            address=i[5]
        )

# Function to delete the message
def delete_message(request, customer_id):
    customer = Customer.objects.get(customer_id = customer_id)
    customer.delete()
    messages.success(request, "Message successfully delete !")
    return HttpResponseRedirect('/')