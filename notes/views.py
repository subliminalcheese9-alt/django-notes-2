from django.shortcuts import render, redirect
from .models import Note

# Create your views here.

def home(request):
    if request.method == 'POST':
        text = request.POST.get('text') 
        Note.objects.create(text=text)
        return redirect('home')
        
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})
    
        
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.done = not note.done
    note.save()
    return redirect('home')


def toggle_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('home')