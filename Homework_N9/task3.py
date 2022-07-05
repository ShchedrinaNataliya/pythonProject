class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self. position = position
        self._income = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def get_name(self):
        return f"{self.name} {self.surname}"

    def get_profit(self):
        return f"{sum(self._income.values())}"

manager = Position("Steave", "Morison", "JuniorSpecialist", 350000, 100000)
print(manager.get_name())
print(manager.position)
print(manager.get_profit())