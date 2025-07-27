class ApiFoncierError(Exception):
    """Exception de base pour le module apifoncier."""

    pass


class AuthenticationError(ApiFoncierError):
    """Erreur d'authentification."""

    pass
