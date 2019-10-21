from django.contrib import admin
from .models import Math
from .models import Stat

# Register your models here.

@admin.register(Math)
class MathAdmin(admin.ModelAdmin):
	list_display = ('_id','si_no', 'level','question','ch_1','ch_2','ch_3','ch_4','answer')
	ordering = ("si_no",)

# admin.site.register(Math)
# admin.site.register(Stat)
@admin.register(Stat)
class MathAdmin(admin.ModelAdmin):
	list_display = ('_id','si_no', 'level','question','ch_1','ch_2','ch_3','ch_4','answer')
	ordering = ("si_no",)