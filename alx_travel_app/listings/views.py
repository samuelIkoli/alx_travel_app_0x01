from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
