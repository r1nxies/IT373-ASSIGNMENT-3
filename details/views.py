from django.shortcuts import render, get_object_or_404
from .models import Announcement

def home(request):
    return render(request, 'details/home.html')

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-date_posted')
    return render(request, 'details/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'details/announcement_detail.html', {'announcement': announcement})
