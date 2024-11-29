Gas Utility Customer Service
<!-- you can Access the Django admin at http://127.0.0.1:8000/admin/ and 
 API at http://127.0.0.1:8000/api/requests/. -->


<!-- python manage.py createsuperuser
username: deba
password: deba@2002@123 -->
Gas Utility Customer Service
A simple Django web application for managing customer service requests for a gas utility company. This project provides an API for customers to submit service requests, track their status, and view their account information. Support representatives can manage, resolve, and track the requests using the Django admin interface.

Features

Customer Service Requests: Customers can submit requests such as repairs, installations, and maintenance.
Tracking Request Status: Customers can track the status of their service requests (Pending, In Progress, Resolved, Closed).
Admin Interface: Support representatives can view, manage, and resolve service requests directly from the Django admin interface.
API for Service Requests: Customers can interact with the application via a REST API to submit and track requests.

Installation

git clone <repository-url>
cd gas_utility

<!-- create python -m venv venv ( create virtual enviroment)
.\venv\scripts\activate  (activate it ) 
pip install django
pip install django djangorestframework
and then run python manage.py makemigrations and then 
run python manage.py migrate after this is done go for 
python manage.py createsuperuser
username: deba
password: deba@2002@123 
python manage.py runserver
you will get a link (http://127.0.0.1:8000/)

and to access the Django admin at http://127.0.0.1:8000/admin/ and 
 API at http://127.0.0.1:8000/api/requests/.  use this-->


Models
ServiceRequest Model
customer_name: Name of the customer submitting the request.
email: Email address of the customer.
request_type: Type of service request (repair, installation, maintenance, etc.).
details: Description of the issue or service request.
file_attachment: Optional file attachment related to the request.
status: Current status of the request (Pending, In Progress, Resolved, Closed).
created_at: Timestamp of when the request was created.
resolved_at: Timestamp of when the request was resolved.
Django Admin Customization
In the Django admin interface, the following features are enabled:

View all service requests with filters for status and request type.
Track request status and display the current status in the admin list view.
Mark requests as resolved using a custom action.
Search and filter service requests by customer name, email, and status.

