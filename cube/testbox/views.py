from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse

from .forms import Userform
from .models import chat_log
import nltk

# Create your views here
'''def index(request):
    if request.method == 'POST':
        # if the form has been filled#
        form = Userform(request.POST)
        if form.is_valid():  # All the data is valid
            chat = request.POST.get('chat', '')
            # creating an user object containing all the data
            chat = nltk.word_tokenize(chat)
        user_obj = User(chat=chat)
        # saving all the data in the current object into the database
        user_obj.save()
        # return HttpResponse(" " + chat[0])
        return render(request,'testbox/home.html',{"user_obj":user_obj,'is_submit': True})
        #  Redirect after POST {'is_submit': True}
    else:
       form = Userform()  # unbound form
       return render(request, 'testbox/home.html', {'form': form})
'''




# the function executes with the showdata url to display the list of chat
def showchat(request):

    if request.method == 'POST':
        # if the form has been filled#
        form = Userform(request.POST)
        if form.is_valid():  # All the data is valid
            chat = request.POST.get('CHAT', '')
            # creating an user object containing all the data
            #chat = nltk.word_tokenize(chat)
        user_obj = chat_log(chat=chat,source="User")
        # saving all the data in the current object into the database
        user_obj.save()

    form = Userform()
        # return HttpResponse(" " + chat[0])
        #return render(request,'testbox/home.html',{"user_obj":user_obj,'is_submit': True})
    all_chat = chat_log.objects.all()
    return render(request, 'testbox/showchat.html', {'all_chat': all_chat,'form': form })

#def getreply(request):
   # return HttpResponse("Got it!")


