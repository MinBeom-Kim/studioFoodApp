from django.contrib import admin
from . import models

@admin.register(
    models.Food,
)
class FoodsAdmin(admin.ModelAdmin):

    """ Foods Admin Definition """

@admin.register(
    models.Diet,
 )
class DietsAdmin(admin.ModelAdmin):

    """ Foods Admin Definition """
    fieldsets = [
        (None, {'fields': ['user_name', 'start_at', 'end_at']}),
        ('Menu', {'fields': ['menu1', 'menu2', 'menu3', 'menu4', 'menu5']}),
        ('Before', {'fields': ['before_menu1', 'before_menu2', 'before_menu3', 'before_menu4', 'before_menu5']}),
        ('After', {'fields': ['after_menu1', 'after_menu2', 'after_menu3', 'after_menu4', 'after_menu5']}),
        ('Eaten', {'fields': ['eaten_menu1', 'eaten_menu2', 'eaten_menu3', 'eaten_menu4', 'eaten_menu5']}),
    ]

    list_display = (
        'id', 'title', 'kcal', 'protein', 'carbohydrate', 'fat', 
    )

    list_display_links =('id', 'title')

