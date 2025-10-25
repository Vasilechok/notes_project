

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class OwnerRequiredMixin(LoginRequiredMixin):
    """
    Міксин для перевірки, що об'єкт належить користувачу.
    Використовувати в DetailView, UpdateView, DeleteView.
    """
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("Ви не маєте доступу до цього об'єкта")
        return super().dispatch(request, *args, **kwargs)

class FormUserMixin(LoginRequiredMixin):
    """
    Міксин для встановлення користувача перед збереженням форми.
    Використовувати в CreateView.
    """
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
