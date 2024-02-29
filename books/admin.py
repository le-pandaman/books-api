from django.contrib import admin

from .models import Books


# Register your models here.


class BookAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                "fields": [
                    'title',
                    'author',
                    'isbn',
                    'subtitle',
                ],
            }
        )
    ]

    list_display = [
        'title',
        'author',
        'subtitle',
        'isbn'
    ]

    list_filter = [
        'title',
        'author',
    ]


admin.site.register(Books, BookAdmin)
