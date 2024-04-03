from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView


# Create your views here.


class NewListView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news_page/index.html'
    extra_context = {
        'title': 'Главная страница'
    }


class SearchNew(NewListView):
    def get_queryset(self):
        word = self.request.GET.get('q')
        news = News.objects.filter(title__icontains=word.lower()) or News.objects.filter(
            title__icontains=word.capitalize())
        return news


def about_page(request):
    context = {
        'title': 'О сайте'
    }

    return render(request, 'news_page/about_page.html', context)
