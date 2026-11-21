from Circuit_Calculator import log_result
import math
class Resistor:
    def __init__(self, resistance):
        self.resistance = resistance

    @property
    def resistance(self) -> float:
        return self._resistance

    @resistance.setter
    def resistance(self, resistance: float):
        if resistance <= 0:
            raise ValueError("Resistance cannot be negative or zero.")
        self._resistance = resistance

    def current(self, voltage):
        current = voltage/ self.resistance
        return current
    def voltage_drop(self, current):
        drop = current * self.resistance
        return drop
    def power_output(self, voltage):
        power = (voltage ** 2) / self.resistance
        return power
    def __str__(self):
        return f"The resistor is {str(self.resistance)} ohms"
    


r1 = Resistor(5)
print(r1)

r1.current(20)
r1.voltage_drop(8)