from app import celery, db
from .models import MetroCard, Station


@celery.task
def update_station_details(metro_card_id, station_id, charges):
    metro_card = MetroCard.query.get(metro_card_id)
    passenger_type = metro_card.passenger_type()

    station = Station.query.get(station_id)
    station.total_collection += charges

    if passenger_type == "KID":
        station.passenger_kid += 1
    elif passenger_type == "ADULT":
        station.passenger_adult += 1
    elif passenger_type == "SENIOR_CITIZEN":
        station.passenger_senior_citizen += 1

    db.session.add(station)
    db.session.commit()
