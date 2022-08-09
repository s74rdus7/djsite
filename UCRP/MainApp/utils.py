from .models import *

menu = [{'title': 'Главная', 'url_name': 'mainpage'},
        {'title': 'Добавить сотрудника', 'url_name': 'add_employee'},
        {'title': 'Добавить событие', 'url_name': 'add_event'},
        ]

class DataMixin:
        paginate_by = 10

        def get_user_context(self, **kwargs):
                context = kwargs
                places = PLACES.objects.all()

                user_menu = menu.copy()
                if not self.request.user.is_authenticated:
                        try:
                                user_menu.pop(1)
                                user_menu.pop(1)
                        except:
                                next

                context['menu'] = user_menu
                return context