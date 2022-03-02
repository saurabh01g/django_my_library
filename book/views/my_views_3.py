"""
--------------------------------------------------------------------------------------------------
Assignment No. 9            (from line 150)
--------------------------------------------------------------------------------------------------
Django Class Based 
           Generic Views
           Generic edit - CRUD operations using class based views (Create, Retrieve, Update, Delete)
--------------------------------------------------------------------------------------------------
S G.    dt. 09-02-2022
--------------------------------------------------------------------------------------------------
"""
# import logging
import traceback

from book.forms import (AddressForm, BookForm, BookModelForm, ContactForm,
                        FeedbackForm)
from book.models import Book, Employee
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

# logger = logging.getLogger("first")

# Create your views here.

"""all active book record i.e is_active=True."""
def show_all_active_books(request):
    # logger.info("Inside show_all_active_books view") #######
    all_active_books = Book.active_obj.all()                            # custom model manager obj.
    data = {'books': all_active_books}
    return render(request, 'show_active_books.html', context=data)

"""all inactive book record i.e is_active=False."""
def show_all_inactive_books(request):
    # logger.info("Inside show_all_inactive_books view") #######
    all_inactive_books = Book.objects.filter(is_active=False)
    data = {'books': all_inactive_books}
    return render(request, 'show_inactive_books.html', context=data)

"""update data for selected book id record at home page."""
def edit_data(request, id):
    # logger.debug(f"Edit button is clicked for Book ID - {id}") #######
    book = Book.active_obj.get(id=id)
    return render(request, template_name='home.html', context={'single_book': book})



"""soft delete for given book id. Single book record soft delete"""
def soft_delete_data(request, id):
    # logger.info(f"Inside soft_delete_data view. Soft Delete button is clicked for Book ID - {id}") #######
    print(request.method)
    if request.method == 'POST':
        try:
            book = Book.active_obj.get(id=id)
        except Book.DoesNotExist:
            # logger.warning(f"Insid soft_delete_data. Book ID - {id} is not present") #######
            traceback.print_exc()                                                        
            return HttpResponse(f"Book for id-{id} is not present.")
        else:
            book.is_active = False
            book.save()
            # logger.debug(f" Book ID - {id} record is set as inactive. Soft deleted.") #######
        return redirect('show_all_active_books')
    else:
        return HttpResponse(f"Request {request.method} method is not allowed. Only POST method.")

"""soft delete all book records"""
def soft_delete_all_data(request):
    # logger.info("Inside soft_delete_all_data view. Soft Delete all records button is clicked.") #######
    print(request.method)
    if request.method == 'POST':
            books = Book.objects.all()
            for book in books:                                                   
                book.is_active = False                         # is_active field is updated for book record.
                book.save()
            return redirect('show_all_active_books')
    else:
        # logger.error(f"{request.method} not allowed for soft delete all records button.") #######
        return HttpResponse(f"Request {request.method} method is not allowed. Only POST method.")

"""restore book record by updating is_active = True"""
def restore_data(request, id):
    # logger.info("Inside restore_data view. Restore button is clicked.") #######
    print(request.method)
    if request.method == 'POST':
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()  
            return HttpResponse(f"Book for id-{id} is not present.")
        else:
            book.is_active = True                               # is_active field is updated for book record.
            book.save()
            # logger.debug(f" Book ID - {id} record is  restored.") #######
        return redirect('show_all_inactive_books')
    else:
        return HttpResponse(f"Request {request.method} method is not allowed. Only POST method.")


def Feedback_Form(request):                                     # django form example
    context ={"form":FeedbackForm()}
    return render(request, "Feedback_Form.html", context)


def Book_Model_Form(request):                                   # django model example
    context ={"form":BookModelForm()}
    return render(request, "Book_Model_Form.html", context)


# def Address_Form(request):                                      # django crispy from example    
#     if request.method =="POST":
#         pass
#     else:
#         print("In GET request.")
#         context ={"form":AddressForm()}
#         return render(request, "Address_Form.html", context)

def Address_Form(request):                                      # here Address_Form is changed to practice django message    
    if request.method =="POST":
        print(request.POST)
        print("In POST request")
        form =BookForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            # print(form.cleaned_data[" name"])
            form.save()
            messages.success(request, "Data Saved successfully") 
            messages.info(request, "Redirecting to homepage")
        else:
             messages.error(request, "Invalide data")   
        return redirect("address_form") 
    elif request.method == "GET":
        print("In GET request.")
        context ={"form":BookForm()}
        return render(request, "Address_Form.html", context)
    else:
        return HttpResponse("Invalid HTTP method", statue=405)

def Contact_Form(request):                                      # django crispy from example    
    context ={"form":ContactForm()}
    return render(request, "Contact_Form.html", context)

#----------------------------------------------------------------------------------------------------------

"""class based views"""

class HomePage(View):
    def get(self, request):
        print("in get request")
        return HttpResponse("inside get")

    def post(self, request):
        print(request.POST)  # 
        return HttpResponse("Inside POST",status=201)

    def delete(self, request):
        print("in delete req.")
        return HttpResponse("inside delete",status=204)

    def put(self, request):
        print("in put req.")
        return HttpResponse("inside put")

    def patch(self, request):
        print("in patch req.")
        return HttpResponse("inside patch")


"""class based Generic views Edits"""
class EmployeeCreate(CreateView):  
    model = Employee  
    fields = '__all__'  
    success_url = reverse_lazy("book:EmployeeCreate")           # to redirect after Create


class EmployeeRetrieve(ListView):  
    model = Employee  
    success_url = reverse_lazy('book:EmployeeRetrieve')

class EmployeeDetail(DetailView):  
    model = Employee  
    success_url = reverse_lazy('book:EmployeeRetrieve')

class EmployeeUpdate(UpdateView):  
    model = Employee
    fields = '__all__'  
    success_url = reverse_lazy('book:EmployeeRetrieve')

class EmployeeDelete(DeleteView):  
    model = Employee
    success_url = reverse_lazy('book:EmployeeRetrieve')
    