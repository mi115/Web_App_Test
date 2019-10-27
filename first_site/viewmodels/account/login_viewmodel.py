from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()
        self.user = user_service.login_user(self.email, self.password)

    def validate(self):
        if not self.email or not self.email.strip():
            self.error = 'You must specify an email.'
        elif not self.password:
            self.error = 'You must specify a password.'
