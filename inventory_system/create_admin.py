import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Fetch credentials securely from Render's environment variables
username = os.environ.get('ADMIN_USERNAME')
email = os.environ.get('ADMIN_EMAIL')
password = os.environ.get('ADMIN_PASSWORD')

if not password:
    print("❌ Script skipped: ADMIN_PASSWORD environment variable not set.")
else:
    if not User.objects.filter(username=username).exists():
        print(f"🚀 Creating cloud superuser: {username}...")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("✅ Superuser created successfully!")
    else:
        print(f"ℹ️ Superuser '{username}' already exists. Skipping creation.")