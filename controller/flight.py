from dataclasses import dataclass


@dataclass
class Flight:
    """
    Dataclass информации о рейсе.
    """
    flight_number: str
    departure_date: str
    departure_time: str
    flight_duration: str
    departure_airport_code: str
    arrival_airport_code: str
    ticket_price: float

    def __str__(self):
        return 'Информация о рейсе: {} {} {} {} {} {} {}'.format(self.flight_number,
                                                                 self.departure_date,
                                                                 self.departure_time,
                                                                 self.flight_duration,
                                                                 self.departure_airport_code,
                                                                 self.arrival_airport_code,
                                                                 self.ticket_price)
