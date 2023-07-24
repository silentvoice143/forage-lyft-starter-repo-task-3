from batterys.battery import Battery
from engines.engine import Engine
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from batterys.spindlerbattery import SpindlerBattery
from batterys.nubbinbattery import NubbinBattery
from car import Car

class CarFactory:
    # print("hello")
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery=SpindlerBattery(last_service_date)
        car=Car(engine,battery)
        return car
    
    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery=SpindlerBattery(last_service_date)
        car=Car(engine,battery)
        return car
    
    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery=NubbinBattery(last_service_date)
        car=Car(engine,battery)
        return car
    
    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        engine=CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery=NubbinBattery(last_service_date)
        car=Car(engine,battery)
        return car
    
    @staticmethod
    def create_palindrome(last_service_date,warning_light_is_on):
        engine=SternmanEngine(last_service_date, warning_light_is_on)
        battery=SpindlerBattery(last_service_date)
        car=Car(engine,battery)
        return car