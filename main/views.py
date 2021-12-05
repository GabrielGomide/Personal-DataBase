from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import date, datetime, timedelta

# Create your views here.
def dashboard(request):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    names = []

    people = People.objects.all()

    for person in people:
        if person.birthday:
            person_birthday_this_year = datetime(datetime.today().year, person.birthday.month, person.birthday.day)
            today = datetime.today()
            if today < person_birthday_this_year:
                if today + timedelta(days=30) > person_birthday_this_year:
                    names.append(f"{person.name} ({person.birthday.strftime('%B %d, %Y')})")

    context = {'names': names}

    return render(request, 'main/dashboard.html', context)

def people(request):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    context = {'people': People.objects.all()}
    
    return render(request, 'main/people.html', context)

def add(request):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    if request.method == 'POST':
        form = AddPeople(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            instagram = form.cleaned_data['instagram']
            notes = form.cleaned_data['notes']
            person = People(name=name, birthday=birthday, email=email, number=number, instagram=instagram, notes=notes)
            person.save()
            return redirect('people')
    else:
        form = AddPeople()

    context = {'form': form}

    return render(request, 'main/add.html', context)

def person(request, id):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    person = People.objects.filter(id=id)

    if len(person) == 1:
        person = People.objects.get(id=id)
        exist = True
    else:
        exist = False

    context = {'person': person, 'exist': exist}

    return render(request, 'main/person.html', context)

def edit_person(request, id):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    person = People.objects.filter(id=id)

    if len(person) == 1:
        person = People.objects.get(id=id)
        exist = True
    else:
        exist = False

    if request.method == 'POST':
        form = AddPeople(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            instagram = form.cleaned_data['instagram']
            notes = form.cleaned_data['notes']

            person.name = name
            person.birthday = birthday
            person.email = email
            person.number = number
            person.instagram = instagram
            person.notes = notes

            person.save()
            
            return redirect(f'../../people/{person.id}')
    else:
        form = AddPeople()

        form.fields['name'].initial = person.name
        form.fields['birthday'].initial = person.birthday
        form.fields['email'].initial = person.email
        form.fields['number'].initial = person.number
        form.fields['instagram'].initial = person.instagram
        form.fields['notes'].initial = person.notes

    context = {'person': person, 'exist': exist, 'form': form}

    return render(request, 'main/edit_person.html', context)

def notes(request):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    notes = Note.objects.all()
    context = {'notes': notes}

    return render(request, 'main/notes.html', context)

def add_note(request):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    if request.method == 'POST':
        form = AddNote(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            notes = form.cleaned_data['notes']
            note = Note(title=title, notes=notes)
            note.save()
            return redirect('notes')
    else:
        form = AddNote()

    context = {'form': form}

    return render(request, 'main/add_note.html', context)

def note(request, id):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    note = Note.objects.filter(id=id)

    if len(note) == 1:
        note = Note.objects.get(id=id)
        exist = True
    else:
        exist = False

    context = {'note': note, 'exist': exist}

    return render(request, 'main/note.html', context)

def edit_note(request, id):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    note = Note.objects.filter(id=id)

    if len(note) == 1:
        note = Note.objects.get(id=id)
        exist = True
    else:
        exist = False

    if request.method == 'POST':
        form = AddNote(request.POST)

        if form.is_valid():
            note.title = form.cleaned_data['title']
            note.notes = form.cleaned_data['notes']
            note.save()
            return redirect(f'../{id}')
    else:
        form = AddNote()

        form.fields['title'].initial = note.title
        form.fields['notes'].initial = note.notes

    context = {'form': form, 'note': note, 'exist': exist}

    return render(request, 'main/edit_note.html', context)

def delete_note(request, id):
    password = request.COOKIES.get('password')

    if not password:
        return redirect('login')

    note = Note.objects.filter(id=id)

    if len(note) == 1:
        note = Note.objects.get(id=id)

    note.delete()

    return redirect('notes')
