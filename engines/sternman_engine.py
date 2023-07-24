from abc import ABC

from engines.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date=last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
