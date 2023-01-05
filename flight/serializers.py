from rest_framework import serializers
from .models import Flight, Reservation, Passenger


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True)
    flight = serializers.StringRelatedField()
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",
            "flight_id",
            "user",
            "passenger"
        )
