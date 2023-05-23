from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    role_options = (
        ("Junior", "Junior"),
        ("Mid-level", "Mid-level"),
        ("Senior", "Senior"),
        ("Principal", "Principal"),
        ("C-level", "C-level"),
        ("VP", "VP"),
        ("Director", "Director"),
        ("Manager", "Manager"),
    )
    work_options = (
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
        ("Freelance", "Freelance"),
        ("Internship", "Internship"),
        ("Apprenticeship", "Apprenticeship"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_images', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    subscription = models.BooleanField(default=False)
    subscription_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=50, choices=role_options, default='Mid-level')
    work_type = models.CharField(max_length=50, choices=work_options, default='Full-time')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    new_profile = models.BooleanField(default=True)
    open_to_work = models.BooleanField(default=True)
    open_to_relocation = models.BooleanField(default=True)
    open_to_remote = models.BooleanField(default=True)
    notifications = models.BooleanField(default=True)   
    sms_notifications = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    languages = models.ManyToManyField('LanguageProficiency', blank=True)
    available_for_remote_work = models.BooleanField(default=False)
    preferred_working_hours = models.CharField(max_length=50, blank=True)
    project_contributions = models.ManyToManyField('Project', blank=True)
    publications = models.ManyToManyField('Publication', blank=True)
    awards = models.ManyToManyField('Award', blank=True)
    preferred_tech_stack = models.ManyToManyField('Technology', blank=True)
    email = models.EmailField(blank=True)
    email_verified = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=50, blank=True)
    stripe_subscription_id = models.CharField(max_length=50, blank=True)
    stripe_subscription_status = models.CharField(max_length=50, blank=True)
    stripe_subscription_end_date = models.DateTimeField(blank=True, null=True)
    stripe_subscription_cancel_at_period_end = models.BooleanField(default=False)
    stripe_subscription_cancel_at = models.DateTimeField(blank=True, null=True)
    stripe_subscription_created = models.DateTimeField(blank=True, null=True)
    stripe_subscription_current_period_start = models.DateTimeField(blank=True, null=True)
    stripe_subscription_current_period_end = models.DateTimeField(blank=True, null=True)
    stripe_subscription_start_date = models.DateTimeField(blank=True, null=True)
    stripe_subscription_days_until_due = models.PositiveIntegerField(blank=True, null=True)
    stripe_invoice_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_invoice_status = models.CharField(max_length=50, blank=True, null=True)
    stripe_invoice_paid = models.BooleanField(default=False, blank=True, null=True)
    hired = models.BooleanField(default=False)
    hired_date = models.DateTimeField(blank=True, null=True)
    hired_by = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True)
    hired_by_name = models.CharField(max_length=50, blank=True, null=True)
    currently_interesting = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class LanguageProficiency(models.Model):
    language = models.CharField(max_length=50)
    proficiency_level = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)

   
class Publication(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Award(models.Model):
    title = models.CharField(max_length=100)
    date_received = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
