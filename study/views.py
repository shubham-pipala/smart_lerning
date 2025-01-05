from django.shortcuts import render,redirect
from . models import *
from .form import * # for form mate
from django.views import generic
# from youtubesearchpython import *
import requests




# Create your views here.
def home(request):
    return render(request,'study/home.html')



def note(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = noteform(request.POST)
            if form.is_valid():
                # Save the note and associate it with the logged-in user
                new_note = form.save(commit=False)
                new_note.user = request.user
                new_note.save()
                return redirect('notes')  # Redirect to the same page after saving
        else:
            form = noteform()
        
        # Fetch notes for the authenticated user
            user_notes = notes.objects.filter(user=request.user)
            context = {'noted': user_notes, 'form': form}
            return render(request, 'study/notes.html', context)
    else:
        # Redirect unauthenticated users to the login page
        return render(request,'study/notes.html')  # Adjust the URL name for your login page

def delete(request,pk):
    notes.objects.get(id=pk).delete()
    return render(request,'study/notes.html') 

# def delete(request,pk):
#     notes.objects.get(id=pk).delete()
#     return render(request,'homework.html') 



# def note(request):
    
    
#     if request.user.is_authenticated:
#         form = noteform()
#         note= notes.objects.filter(user=request.user)
#         context={'noted':note,'form':form}
#         return render(request,'notes.html',context)
#     else:
#         return render(request,'notes.html')

    
class notedetailview(generic.DetailView):### for note upar click karta note detail page khule tene mate
    model=notes
# def notedetailview(request):
#     return render(request,'notes_detail.html')
    
    

def dictionary(request):
    return render(request,'dictionary.html')

def login_(request):
    return render(request,'login.html')

def homework(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = workpage(request.POST)
            if form.is_valid():  # if form is valid
                # Save the note and associate it with the logged-in user
                new_WORK = form.save(commit=False) ## save the form
                new_WORK.user = request.user
                new_WORK.save()
                return redirect('homework') 
        else:
            form = workpage(request.POST)
            works=work.objects.filter(user=request.user)
            if len(works)== 0 :
                homework_done = True
            else:
                homework_done = False
            return render(request,'study/homework.html',{'workes': works,'homework_done':homework_done,'form':form})
    else:
        return render(request,'study/homework.html')


def update_work(request,pk=None):
    works=work.objects.get(id=pk)
    if works.is_finished == True:
        works.is_finished = False
        works.save()
    else:
        works.is_finished =True
    
    return redirect('homework')



def delete_work(request,pk):
    work.objects.get(id=pk).delete()
    return render(request,'study/homework.html') 

# def youtube(request):   ## first install youtube using this =pip install youtube-search-python
#     if request.method == "POST":
#         form = dashbord(request.POST)
#         text = request.POST['text']
#         video = VideosSearch(text,limit=20)
#         result=[]
#         for i in video.result()['result']:
#             result_disc = {
#                 'input':text,
#                 'title':i['title'],
#                 'duration':i['duration'],
#                 'thumbnail':i['thumbnail'][0]['url'],
#                 'channel':i['channel']['name'],
#                 'link':i['link'],
#                 'views':i['viewCount']['short'],
#                 'published':i['publishedTime'],
#                 'descriptions':i['descriptions']
#             }
#             result_dist = {}
#             desc=''
#             if i['descriptions']:
#                 for j in i['descriptions']:
#                     desc += j['text']
#                 result_dist = {'descriptions': desc}

#                 result.append(result_dist)
#                 return render(request,'study/youtube.html',{'form':form,'result':result_dist})
#     else:       
#         form = dashbord()
#         return render(request,'study/youtube.html',{'form':form})

# import requests

# proxies = {
#     "http": "http://proxyserver:port",
#     "https": "https://proxyserver:port"
# }

# response = requests.get("https://example.com", proxies=proxies)
# print(response.text)



def youtube(request):   ## first install youtube using this =pip install youtube-search-python
    if request.method == "POST":
         form = dashbord(request.POST)
         text = request.POST['text']
         video = VideosSearch(text, limit=20)
         result = []
        
         for i in video.result()['result']:
             result_disc = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime'],
             }
             desc = ''
             if 'descriptionSnippet' in i and i['descriptionSnippet']:
                 for j in i['descriptionSnippet']:
                     desc += j['text']
             result_disc['descriptions'] = desc  # Add the concatenated description to result_disc
            
             result.append(result_disc)
        
         return render(request, 'study/youtube.html', {'form': form, 'result': result})
    
    else:
        form = dashbord()
        return render(request, 'study/youtube.html', {'form': form})

# def todo(request):
#     if request.method == "POST":
#             form = noteform(request.POST)
#             if form.is_valid():
#                 # Save the note and associate it with the logged-in user
#                 new_note = form.save(commit=False)
#                 new_note.user = request.user
#                 new_note.save()
#                 return redirect('notes')  # Redirect to the same page after saving
#             else:
#                 todo = todoo.objects.filter(user=request.user)
#                 return render (request,"study/todo.html",{'todo':todo,'form':todopage})
            
def todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = todopage(request.POST)
            if form.is_valid():
                # Save the note and associate it with the logged-in user
                new_note = form.save(commit=False)
                new_note.user = request.user
                new_note.save()
                return redirect('todo')  # Redirect to the same page after saving
        else:
            form = noteform()
        
        # Fetch notes for the authenticated user
        user_notes = todoo.objects.filter(user=request.user)
        # context = {'noted': user_notes, 'form': form}
        return render(request, 'study/todo.html', {'todo':user_notes,'form':todopage})
    else:
        # Redirect unauthenticated users to the login page
        return render(request, 'study/todo.html')  # Adjust the URL name for your login page


def delete__(request,pk):
    todoo.objects.get(id=pk).delete()
    return render(request,'study/todo.html') 

def book(request):
  
    if request.method == "POST":
         form = dashbord(request.POST)
         text = request.POST['text']
         utl = f"https://www.googleapis.com/books/v1/volumes?q={text}"
         r = requests.get(utl)
         result = []
        
         for i in range(5):
             result_disc = {
                'input': text,
                'title': r.json()['items'][i]['volumeInfo']['title'],
                'authors': r.json()['items'][i]['volumeInfo']['authors'],
                'publisher': r.json()['items'][i]['volumeInfo']['publisher'],
                'publishedDate': r.json()['items'][i]['volumeInfo']['publishedDate'],
                'description': r.json()['items'][i]['volumeInfo']['description'],
                'pageCount': r.json()['items'][i]['volumeInfo']['pageCount'],
                'categories': r.json()['items'][i]['volumeInfo']['categories'],
                'thumbnail': r.json()['items'][i]['volumeInfo']['imageLinks']['thumbnail'],
                'previewLink': r.json()['items'][i]['volumeInfo']['previewLink'],
             }
             desc = ''
             if 'descriptionSnippet' in i and i['descriptionSnippet']:
                 for j in i['descriptionSnippet']:
                     desc += j['text']
             result_disc['descriptions'] = desc  # Add the concatenated description to result_disc
            
             result.append(result_disc)
        
         return render(request, 'study/youtube.html', {'form': form, 'result': result})
    
    else:
        form = dashbord()
        return render(request, 'study/youtube.html', {'form': form})