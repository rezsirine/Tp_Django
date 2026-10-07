from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
import meetings
from meetings.forms import MeetingsForm
from meetings.models import Meetings

def get_all_view(request):
    meetings = Meetings.objects.all()
    return render(request, 'getall.html', {'meets': meetings})

def detail_view(request, id):
    meeting = get_object_or_404(Meetings, id=id)
    return render(request, 'detail.html', {'meeting': meeting})

def delete_view(request, id):
    meeting = get_object_or_404(Meetings, id=id)
    if request.method == 'POST':
     meeting.delete()
     return redirect('getall')
    return render(request, 'delete.html', {'meeting': meeting})

def create_view(request):
    form = MeetingsForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('getall')
        form = MeetingsForm()
    return render(request, 'create.html', {'form': form})

def update_view(request, id):
    meeting = get_object_or_404(Meetings, id=id)
    form = MeetingsForm(request.POST, instance=meeting)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('getall')
        form = MeetingsForm(instance=meeting)
    return render(request, 'update.html', {'form': form})


