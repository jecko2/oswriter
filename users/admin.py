from django.contrib import admin
from .models import CustomUser, Complaint, ClientReview


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff', 'is_superuser', 'is_active', ]
    fieldsets = (
        ('USER VISUALIZATION', {
            'fields': ('email', 'is_superuser', 'is_staff', 'is_active',)
        }),)

    @admin.display(ordering='-email')
    def user_email(self, obj):
        return obj.user.email


class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date_posted']
    fieldsets = (
        ('CLIENT REVIEW', {
            'fields': ('client', 'subject', 'issue_burning', 'date_posted')
        }),)

    @admin.display(ordering='-date_posted')
    def client_review_date(self, obj):
        return obj.client_review_date.date_posted


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date_posted']
    fieldsets = (
        ('CLIENT REVIEW', {
            'fields': ('client', 'subject', 'complaint', 'date_posted')
        }),)

    @admin.display(ordering='-date_posted')
    def client_complaint_date(self, obj):
        return obj.client_complaint_date.date_posted


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ClientReview, ClientReviewAdmin)
admin.site.register(Complaint, ComplaintAdmin)
