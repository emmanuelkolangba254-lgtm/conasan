from .models import Profil


def est_superadmin(user):
    if not user.is_authenticated:
        return False

    try:
        return user.profil.role == "SUPERADMIN"
    except:
        return False


def est_admin(user):
    if not user.is_authenticated:
        return False

    try:
        return user.profil.role in [
            "SUPERADMIN",
            "ADMIN"
        ]
    except:
        return False


def est_agent(user):
    if not user.is_authenticated:
        return False

    try:
        return user.profil.role in [
            "SUPERADMIN",
            "ADMIN",
            "AGENT"
        ]
    except:
        return False
