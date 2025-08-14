from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'age')
    search_fields = ('email', 'name')
    list_filter = ('email', 'name')

    class Meta:
        model = User
        verbose_name = 'User'
        verbose_name_plural = 'Users'

