from django.core.management.base import BaseCommand
from listings.models import Listing
from django.utils import timezone
import random


class Command(BaseCommand):
    help = "Seed database with sample listings"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        sample_listings = [
            {
                "title": "Luxury Beachfront Apartment",
                "description": "A beautiful apartment overlooking the ocean.",
                "price_per_night": 350.00,
                "location": "Lagos Beach",
            },
            {
                "title": "Cozy Mountain Cabin",
                "description": "Perfect getaway with a fireplace.",
                "price_per_night": 150.00,
                "location": "Obudu Cattle Ranch",
            },
            {
                "title": "Modern City Studio",
                "description": "Located in the heart of Abuja.",
                "price_per_night": 200.00,
                "location": "Abuja",
            },
        ]

        for item in sample_listings:
            Listing.objects.create(
                title=item['title'],
                description=item['description'],
                price_per_night=item['price_per_night'],
                location=item['location'],
                is_available=True,
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
