from django.contrib import admin

# Register your models here.


from .models import Info, Resume,Contact

admin.site.register(Info)
admin.site.register(Resume)
admin.site.register(Contact)