"""
-------------------------------------------------------------
Task given in video no 112
-------------------------------------------------------------
Task implemented :
            Split views : my_view_1, my_view_2, my_view_3 (All function based views previously writtin for assignment 8 are divided here)
            custom command : cmd_time, cmd_message
            forms : Django forms -        FeedbackForm 
                    Django model forms  - BookModelForm
                    Django Crispy Forms - AddressForm,
                                          ContactForm
                    (all form views written in my_view_3.py)
--------------------------------------------------------------
S G.    dt. 03-02-2022
--------------------------------------------------------------
"""
import datetime
#import logging

from book.models import Book
from django.http import HttpResponse
from django.shortcuts import redirect, render

#logger = logging.getLogger("first")


def view_a(request):
    return HttpResponse("In view_a")

def view_b(request):
    return HttpResponse("In view_b")

def welcome(request):                                                                               
    #logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')  # logs time stamp when Homepage was accessed
    return HttpResponse("<br><h1>Welcome to My_Library :) <a href='home'> Click here</a> to continue</h1>")

"""homepage() to create book object i.e. new entry in datatabase or to edit entry if id is given"""
def homepage(request):                                                                                  
    name = request.POST.get('bname')
    price = request.POST.get('bprice')
    qty = request.POST.get('bqty')

    if request.method == 'POST':                                                  # create new data entry
        if not request.POST.get('bid'):
            #logger.info("In homepage view for New Book Entry ")                   # INFO level to show that things are working as expected 
            book_name = name
            book_price = price
            book_qty = qty
            if not name or not price or not qty:                                  # if user enters empty data for any field then return HttpResponce
             #   logger.warning(f"Either one or more fields are entered empty:  BookName-{name} Price-{price} Quantity-{qty}")  #WRG.level to show unexpected happened                                                  # validation check if empty data is submitted
                return HttpResponse("All fields are mendatory. Please enter data. All fields should not be empty.") 
            Book.objects.create(name=book_name, price=book_price, qty=book_qty)                          # to create book record
            #logger.debug(f"New book record Entry:  BookName- {name}  Price- {price} Quantity- {qty}")    # DEBUG level to show detailed information
            #logger.debug(f"New book record Entry:{request.POST}")                 # DEBUG level to show detailed information . Here op. is QuerySet
            return redirect('homepage') 
        else:
            bid = request.POST.get('bid')
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as er_message:
                print(er_message)
             #   logger.error(er_message)                                          # ERROR level to show issue
            book_obj.name = name
            book_obj.price = price
            book_obj.qty =  qty
            book_obj.save()
            #logger.info(f"Record updated successfully for Book ID : {bid}") #######
            return redirect('show_all_active_books')
    
    elif request.method == 'GET':
        all_active_books = Book.active_obj.all()
        data = {'book': all_active_books}
        return render(request, 'home.html',context=data)
