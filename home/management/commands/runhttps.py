# myapp/management/commands/runhttps.py
from django.core.management.commands.runserver import Command as RunserverCommand
import ssl
import os


class Command(RunserverCommand):
    help = "Runs the Django development server with HTTPS."

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--cert', dest='cert_file', default='cert.pem',
            help='Path to the SSL certificate file (e.g., cert.pem)'
        )
        parser.add_argument(
            '--key', dest='key_file', default='key.pem',
            help='Path to the SSL key file (e.g., key.pem)'
        )

    def handle(self, *args, **options):
        cert_file = options['cert_file']
        key_file = options['key_file']

        if not os.path.exists(cert_file):
            self.stderr.write(self.style.ERROR(f"Error: Certificate file '{cert_file}' not found."))
            exit(1)
        if not os.path.exists(key_file):
            self.stderr.write(self.style.ERROR(f"Error: Key file '{key_file}' not found."))
            exit(1)

        # Create SSL context
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)

        # Inject SSL context into options
        options['ssl_options'] = ssl_context

        # Call parent handler
        super().handle(*args, **options)

    def run(self, **options):
        """Override to inject SSL context into the runserver."""
        from django.core.servers.basehttp import run
        run(
            self.addr,
            int(self.port),
            self.get_handler(**options),
            ssl_options=options.get('ssl_options'),
        )
