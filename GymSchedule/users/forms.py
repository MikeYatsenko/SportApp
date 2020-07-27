from  django_registration.forms import RegistrationForm
from users.models import SiteUser


class SiteUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = SiteUser