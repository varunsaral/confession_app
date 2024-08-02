from django.contrib import admin


from .models import Confession

@admin.register(Confession)
class ConfessionAdmin(admin.ModelAdmin):
    list_display = ('content', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('content',)


# Register your models here.
