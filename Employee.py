class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def get_number(self, number):
        return self.number

    def set_name(self):
        return self.name




class ProductionWorker(Employee):
    def __init__(self, shift_number, hourly_payrate):
        Employee.__init__(self)
        self.shift_number = shift_number
        self.hourly_payrate = hourly_payrate

        def set_shift_number(self, shift_number):
            self.shift_number = shift_number

        def set_hourly_payrate(self, payrate):
            self.hourly_payrate = hourly_payrate

        def get_hourly_payrate(self):
            return self.hourly_payrate 

        def get_shift_number(self):
            return self.shift_number
        