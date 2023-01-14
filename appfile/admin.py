
from django.contrib import admin
from .forms import QuoteForm
from .models import Quote, Admin

class QuoteAdmin(admin.ModelAdmin):
    form = QuoteForm
    list_display = ['text', 'author', 'source' ,]
    
    
# def get_queryset(self, request):
#     qs = super().get_queryset(request)
#     if request.user.is_superuser:  
#         return qs
#     if request.user.admin.can_add_quote():
#          return qs
#          return qs.none()

    


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Admin)
