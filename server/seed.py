from random import randint
import bcrypt


from app import app
from models import db, User, Route, Bus, Booking, Pickup_Dropoff_Location
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # USERS
    user1 = User(name="Alice Wanjiku", email="alice@nairobi.com")
    user1.password = "alice123"

    user2 = User(name="Brian Otieno", email="brian@nairobi.com")
    user2.password = "brian123"

    user3 = User(name="Cynthia Mwikali", email="cynthia@nairobi.com")
    user3.password = "cynthia123"

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # ROUTES in Nairobi County
    route1 = Route(origin="Kahawa West", destination="CBD")
    route2 = Route(origin="South B", destination="CBD")
    route3 = Route(origin="Zimmerman", destination="CBD")  
    route4 = Route(origin="Kibera", destination="CBD")

    db.session.add_all([route1, route2, route3, route4])
    db.session.commit()

    # PICKUP / DROPOFF LOCATIONS for route3
    dropoff_data = [
        {"name_location": "Mirema Gate", "GPSystem": "-1.23400,36.78900"},
        {"name_location": "Greenwood School", "GPSystem": "-1.23050,36.79230"},
        {"name_location": "Sunrise Apartments", "GPSystem": "-1.23670,36.78020"},
        {"name_location": "Hilltop View", "GPSystem": "-1.24010,36.79540"},
        {"name_location": "Maple Cross", "GPSystem": "-1.22890,36.78560"},
        {"name_location": "Kahawa West Junction", "GPSystem": "-1.25000,36.80000"},
    ]

    dropoffs = [
        Pickup_Dropoff_Location(
            name_location=item["name_location"],
            GPSystem=item["GPSystem"],
            route_id=route3.id
        )
        for item in dropoff_data
    ]

    db.session.add_all(dropoffs)
    db.session.commit()

    # BUSES
    bus1 = Bus(route=route1, numberplate="KCN 123A", capacity=44)
    bus2 = Bus(route=route2, numberplate="KDA 345B", capacity=40)
    bus3 = Bus(route=route3, numberplate="KDC 567C", capacity=42)
    bus4 = Bus(route=route4, numberplate="KDE 789D", capacity=48)

    db.session.add_all([bus1, bus2, bus3, bus4])
    db.session.commit()

    # BOOKINGS
    booking1 = Booking(
        user=user1,
        bus=bus3,
        pickup_location="Mirema Gate",
        dropoff_location="CBD",
        seats_booked=2,
        booking_date=date.today(),
        price=2000.00
    )

    booking2 = Booking(
        user=user2,
        bus=bus3,
        pickup_location="Greenwood School",
        dropoff_location="CBD",
        seats_booked=1,
        booking_date=date.today(),
        price=1500.00
    )

    booking3 = Booking(
        user=user3,
        bus=bus1,
        pickup_location="Kahawa West",
        dropoff_location="CBD",
        seats_booked=1,
        booking_date=date.today(),
        price=1000.00
    )

    db.session.add_all([booking1, booking2, booking3])
    db.session.commit()

    print("Seed data successfully.")
