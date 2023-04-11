import csv, datetime, os, psycopg2, random, string
from django.http.response import HttpResponse
from xkcdpass import xkcd_password as xp
from pathlib import Path

from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Messagex
from .forms import MessagexCreate, CustomUserForm
from django.views.generic.edit import CreateView


# Create your views here.

class MessagexCreate(LoginRequiredMixin, CreateView):
  model = Messagex
  template_name = "messagex/messagex_create.html"
  form_class = MessagexCreate

  def form_valid(self, form):
    form.instance.sender = self.request.user
    form.instance.time_stamp = datetime.datetime.now()
    return super().form_valid(form)

def index(request):
  if request.user.is_authenticated:
    return redirect("dashboard")
  else:
    return render(request, "messagex/index.html")
  
@login_required
def dashboard(request):
  myreceived = Messagex.objects.filter(recipient=request.user.id).values()
  mysent = Messagex.objects.filter(sender=request.user.id).values()
  context = {
    "name": request.user,
    "myreceived": myreceived,
    'mysent': mysent,
    }
  return render(request, "messagex/dashboard.html", context)

def logmeout(request):
  logout(request)
  return redirect("index")

class MessageList(LoginRequiredMixin, ListView):
  model = Messagex

@login_required
def getmyinbots(request):
  mydata = Messagex.objects.filter(recipient=request.user.id).all()
  context = {
    "name": request.user,
    "mymessages": mydata
    }
  return render(request, "messagex/messagex_inbots.html", context)

@login_required
def getmysent(request):
  mydata = Messagex.objects.filter(sender=request.user.id).all()
  context = {
    "name": request.user,
    "mymessages": mydata
    }
  return render(request, "messagex/messagex_sent.html", context)

def downloadsqlite3(request):
  filename = 'db.sqlite3'
  filepath = Path(__file__).resolve().parent.parent / filename
  with open(filepath, 'rb') as f:
    response = HttpResponse(f.read(), content_type='application/x-sql')
    response['Content-Disposition'] = 'attachment; filename=' + filename
  return response

def downloaddb(request):
  if "DATABASE_URL" in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    response = HttpResponse (content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Id', 'Sender', 'Recipient', 'Subject Message', 'Text Message', 'Timestamp'])
    with conn.cursor() as postgres_cursor:
      sql = "SELECT id, recipient_id, sender_id, subject, text, time_stamp FROM messagex_messagex;"
      postgres_cursor.execute(sql)
      results = postgres_cursor.fetchall()
      writer.writerows(results)
      postgres_cursor.close()
  else:
    os.system("pg_dump -t 'messagex_messagex' secinbots.v1 > dbdump.sql")  
    with open('dbdump.sql', 'rb') as f:
      response = HttpResponse(f.read(), content_type='application/x-sql')
      response['Content-Disposition'] = 'attachment; filename=dbdump.sql'
  return response

def register(request):
    suggested, reasonning = suggest_pass()
    if request.method != 'POST':
      form = CustomUserForm()
    else:
      form = CustomUserForm(request.POST)
      if form.is_valid():
        user = form.save()
        #user.is_active = False
        user.save()
        return redirect('login')
    context = {
      'form': form,
      'sugested_pass': suggested,
      'reasoning': reasonning
      }
    return render(request, 'registration/register.html', context)

def suggest_pass():
  wordfile = xp.locate_wordfile()
  mywords = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=15, valid_chars='.')
  password=xp.generate_xkcdpassword(mywords,interactive=False, acrostic=False, delimiter="|", case="alternating", numwords=6)
  password.split('|')
  final_pass, full_pass = '', ''
  choices=string.punctuation+ string.digits
  for char in password.split('|'):
      rand_char = random.choice(choices)
      final_pass+=char[0] + rand_char
      full_pass+=char + " " + rand_char + " "
  return final_pass, full_pass