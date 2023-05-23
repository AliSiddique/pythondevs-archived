from django.contrib import admin
from .models import Skill, LanguageProficiency, Project, Publication, Award, Technology, Profile
# Register your models here.
admin.site.register(Skill)
admin.site.register(LanguageProficiency)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Award)
admin.site.register(Technology)
admin.site.register(Profile)