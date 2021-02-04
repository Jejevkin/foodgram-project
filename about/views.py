from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about/simple_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Об авторе'
        context['text'] = 'Привет, меня зовут Самородов Владимир. ' \
                          'мой github репозиторий: ' \
                          'https://github.com/Jejevkin/'
        return context


class AboutTechView(TemplateView):
    template_name = 'about/simple_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Технологии'
        context['text'] = 'Подробно про использующиеся технологии можно ' \
                          'почитать, перейдя по адресу: ' \
                          'https://github.com/Jejevkin/foodgram-project'
        return context
