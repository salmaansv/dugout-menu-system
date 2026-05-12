import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dugoutmenu.settings')
django.setup()

from menu.models import MenuItem

print("Checking Menu Item Image Paths:")
print("-" * 30)
for item in MenuItem.objects.all():
    if item.image:
        print(f"Item: {item.name}")
        print(f"  Path in DB: {item.image.name}")
        full_path = item.image.path
        print(f"  Full path: {full_path}")
        print(f"  Exists on disk: {os.path.exists(full_path)}")
    else:
        print(f"Item: {item.name} - No image assigned")
    print("-" * 30)
