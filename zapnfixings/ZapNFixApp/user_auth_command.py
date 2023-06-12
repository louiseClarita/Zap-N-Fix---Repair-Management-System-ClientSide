from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError

class Command(createsuperuser.Command):
    help = 'Create a superuser with an email address'

    def handle(self, *args, **options):
        username = options.get('username')
        email = options.get('email')
        password = options.get('password')

        if not username:
            raise CommandError("You must provide a username.")

        if not email:
            raise CommandError("You must provide an email address.")

        if not password:
            raise CommandError("You must provide a password.")

        self.UserModel._default_manager.db_manager().create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS("Superuser created successfully."))