from django.shortcuts import render, redirect
from .models import WikiPage, PageVersion
from .forms import CreateNewPage


def index(request):
    records = WikiPage.objects.all()
    content = {
        'records': records,
        'title': 'Головна сторінка',
    }
    return render(request, 'index.html', content)


def add_new_record(request):
    if request.method == 'POST':
        form = CreateNewPage(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PageVersion.objects.create(title=data['title'],
                                       content=data['content'],
                                       current_version=1,
                                       )
            WikiPage.objects.create(title=data['title'],
                                    )
        return redirect('home')
    else:
        form = CreateNewPage()
        return render(request, 'add_new.html',
                      {
                          'form': form
                      }
                      )


def view_record(request, record_id):
    record = WikiPage.objects.get(pk=record_id)
    current_version = PageVersion.objects.filter(title=record.title)
    content = {
        'title': record.title,
        'record': record,
        'current_version': current_version,
    }
    return render(request, 'record.html', content)


def edit_record(request, record_id):
    if request.method == 'POST':
        record = WikiPage.objects.get(pk=record_id)
        next_version = record.current_version + 1
        WikiPage.objects.create(title=request.POST.get("title"),
                                content=request.POST.get("content"),
                                current_version=next_version)
        content = {
            'title': f'Редагування сторінки {record_id}',
            'record': record,
        }
        return render(request, 'record.html', content)
    else:
        record = WikiPage.objects.get(pk=record_id)
        content = {
            'title': f'Редагування сторінки {record_id}',
            'record': record,
        }
        return render(request, 'edit.html', content)


def delete_record(request, record_id):
    record = WikiPage.objects.get(pk=record_id)
    record.delete()
    return redirect('home')
