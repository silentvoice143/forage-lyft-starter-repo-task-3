import unittest
from datetime import datetime
from car_factory import CarFactory
from batterys.nubbinbattery import NubbinBattery
from batterys.spindlerbattery import SpindlerBattery

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery=SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery=SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())



class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery=SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery=SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery=SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery=SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        
        battery=NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        
        battery=NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    
class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        
        battery=NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        
        battery=NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

  

if __name__ == '__main__':
    unittest.main()
