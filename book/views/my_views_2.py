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
# import logging
import traceback

from book.models import Book
from django.http import HttpResponse
from django.shortcuts import redirect, render

# logger = logging.getLogger("first")

def view_c(request):
    return HttpResponse("In view_c")

def view_d(request):
    return HttpResponse("In view_d")


"""hard delete for given book id. Single book record hard delete"""
def delete_data(request, id):
    # logger.debug(f"Delete button is clicked for Book ID - {id}") #######
    print(request.method)
    if request.method == 'POST':
        try:
            book = Book.active_obj.get(id=id)
        except Book.DoesNotExist:
            traceback.print_exc()                                                              # to print detail exception message at terminal
            return HttpResponse(f"Book for id-{id} is not present.")
        else:
            book.delete()
            # logger.debug(f"Data deleted successfully for Book ID - {id}") #######
        return redirect('show_all_active_books')
    else:
        return HttpResponse(f"Request {request.method} method is not allowed. Only POST method.")

"""hard delete all book records"""
def delete_all_data(request):
    # logger.info("Delete all records button is clicked.(Hard Delete)") #######
    print(request.method)
    if request.method == 'POST':
        book = Book.objects.all()                                                               #since objects mgr is used it will fetch all data also is_active = True
        book.delete()
        # logger.info(f"All book data deleted successfully. Hard delete") #######
        return redirect('show_all_active_books')
    else:
        # logger.error(f"{request.method} not allowed for Delete all records button.") #######
        return HttpResponse(f"Request {request.method} method is not allowed. Only POST method.")
