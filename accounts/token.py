
from rest_framework_simplejwt.tokens import RefreshToken


def create_tokens(user):
    refresh = RefreshToken()
    refresh["user_id"] = str(user.id)
    refresh["email"] = user.email
    refresh["mobile"] = user.mobile
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }