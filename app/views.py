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
            version = PageVersion.objects.create(title=data['title'],
                                                 content=data['content'],
                                                 current_version=1,
                                                 )
            WikiPage.objects.create(title=data['title'],
                                    version=version
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
    current_version = record.versions
    content = {
        'title': record.title,
        'record': record,
        'current_version': current_version,
    }
    return render(request, 'record.html', content)


def edit_record(request, record_id):
    if request.method == 'POST':
        last_version = PageVersion.objects.get(id=record_id)
        new_version = int(last_version.id) + 1
        new_version = PageVersion.objects.create(title=request.POST.get("title"),
                                                 content=request.POST.get("content"),
                                                 current_version=new_version,
                                                 active_version=new_version)
        page = WikiPage.objects.get(title=new_version.title)
        page.versions = new_version
        page.save()
        return redirect('home')
    else:
        record = PageVersion.objects.get(pk=record_id)
        content = {
            'title': f'Редагування сторінки {record_id}',
            'record': record,
        }
        return render(request, 'edit.html', content)


def delete_record(request, record_id):
    record = PageVersion.objects.get(pk=record_id)
    record.delete()
    return redirect('home')
