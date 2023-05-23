from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    skills = serializers.StringRelatedField(many=True)
    languages = serializers.StringRelatedField(many=True)
    project_contributions = serializers.StringRelatedField(many=True)
    publications = serializers.StringRelatedField(many=True)
    awards = serializers.StringRelatedField(many=True)
    preferred_tech_stack = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "is_employer",
            "profile_picture",
            "cover_image",
            "name",
            "bio",
            "skills",
            "phone_number",
            "subscription",
            "subscription_date",
            "location",
            "website",
            "github",
            "linkedin",
            "twitter",
            "role",
            "work_type",
            "created_at",
            "updated_at",
            "is_active",
            "title",
            "new_profile",
            "open_to_work",
            "open_to_relocation",
            "open_to_remote",
            "notifications",
            "sms_notifications",
            "email_notifications",
            "experience_years",
            "languages",
            "available_for_remote_work",
            "preferred_working_hours",
            "project_contributions",
            "publications",
            "awards",
            "preferred_tech_stack",
            "email",
            "email_verified",
            "stripe_customer_id",
            "stripe_subscription_id",
            "stripe_subscription_status",
            "stripe_subscription_end_date",
            "stripe_subscription_cancel_at_period_end",
            "stripe_subscription_cancel_at",
            "stripe_subscription_created",
            "stripe_subscription_current_period_start",
            "stripe_subscription_current_period_end",
            "stripe_subscription_start_date",
            "stripe_subscription_days_until_due",
            "stripe_invoice_id",
            "stripe_invoice_status",
            "stripe_invoice_paid",
            "hired",
            "hired_date",
            "hired_by",
            "hired_by_name",
            "currently_interesting",
        )


class UserSerializer(UserDetailsSerializer):

    profile = ProfileSerializer()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("profile",)
