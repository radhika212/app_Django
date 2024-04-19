from django.shortcuts import render, redirect
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        # Process form submission
        # Create a new service request object and save it
        ServiceRequest.objects.create(
            customer=request.user.customer,
            request_type=request.POST['request_type'],
            description=request.POST['description'],
            attachment=request.FILES.get('attachment')
        )
        return redirect('request_tracking')
    return render(request, 'submit_request.html')

def request_tracking(request):
    # Fetch all service requests for the current customer
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'request_tracking.html', {'requests': requests})
