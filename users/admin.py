from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #make own section 
    fieldsets = (
        ("Profile", {
                "fields":(
                    "avartar",
                    "username",
                    "password",
                    "name",
                    "is_host"
                    "gender",
                    "language",
                    "currency",
                ),
                "classes" : ("wide",),
            }
        ),
        ("Permissions", {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes":("wide",),
            },
        ),
        ("Important dates", {
            "fields": ("last_login", "date_joined"),
            "classes":("collapse",),
            }
        ),
    )
    list_display = ("username", "email", "name", "is_host",),