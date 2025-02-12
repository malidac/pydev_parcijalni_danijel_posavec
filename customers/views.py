from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer
# Create your views here.

def customer_list(request):
    """
    View to display a list of all customers.
    Supports HTML and JSON responses.
    """
    customers = Customer.objects.all()
    if request.headers.get('Content-Type') == 'application/json':
        customers_data = [
            {"name": customers.name,
             "vatid": customers.vatid,
             "street": customers.street,
             "city": customers.city,
             "county": customers.country,
             }
            for customer in customers
        ]
    return render(request,
                  'customers/customers_list.html',
                  {'customers': customers})

def customer_create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        vatid = request.POST.get('vatid')
        street = request.POST.get('street')
        city = request.POST.get('city')
        country = request.POST.get('country')

        if name and vatid and street and city and country:
            customer = Customer.objects.create(name=name, vatid=vatid, street=street, city=city, country=country)
            return redirect('customer_list')
        return render(request, 'customers/customer_create_form.html', {'error': 'All fields are required.'})

    return render(request, 'customers/customer_create_form.html')

def customer_edit(request, pk):
    """
    View to update an existing customer.
    """
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.name = request.POST.get('name', customer.name)
        customer.vatid = request.POST.get('vatid', customer.vatid)
        customer.street = request.POST.get('street', customer.street)
        customer.city = request.POST.get('city', customer.city)
        customer.country = request.POST.get('country', customer.country)
        customer.save()
        return redirect('customer_list')

    return render(request, 'customers/customer_edit_form.html', {'customer': customer})
