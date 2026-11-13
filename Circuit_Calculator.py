# Ohm's Law
import math
def Solve_DC(V = None, I = None, R = None, P = None):
    known = {"V": V, "I": I, "R": R, "P": P}
    if ([V, I, R, P].count(None) > 2):
        raise ValueError("You did a bad thing and did not give enough info!")

    try:   
        if known["V"] is not None and known["I"] is not None:
            pass
        elif known["V"] is not None and known["R"] is not None:
            I = V / R
        elif known["V"] is not None and known["P"] is not None:
            I = P / V
        elif known["I"] is not None and known["P"] is not None:
            V = P / I
        elif known["I"] is not None and known["R"] is not None:
            V = I * R
        else:
            try:
                V = math.sqrt(P * R)
                I = math.sqrt(P / R)
            except ValueError:
                raise ValueError("You used a negative inside a square root")
        R = V / I    
        P = V * I
        results = {"V": V, "I": I, "R": R, "P": P}
        for initial in known:
            if known[initial] is not None:
                if not math.isclose(results[initial], known[initial]):
                    raise ValueError("Your values are impossible")
    except ZeroDivisionError:
        raise ZeroDivisionError("You did bad job with 0 in demoninator")
    
    return V, I, R, P

def resistance_calculator(Parallel = 0, Series = 0, Ohms = 0):
    try:
        Resistance_parallel = (1/Ohms) * Parallel
        Resistance_series = (Ohms) * Series
        Resistance_Total = Resistance_parallel + Resistance_Total
    except ZeroDivisionError:
        raise ZeroDivisionError("You Divided by 0 buddy")
    
    return Resistance_Total
    


def get_input(prompt):
    while True:
        user_val = input(prompt)
        try:
            if user_val:
                return float(user_val)
            else:
                return None
        except ValueError:
            print("Not whole number so try again")
            





Decision = input("Which Function would you like to use? 1. DC_calculator ")


if Decision == "1":
    V = get_input("Voltage (V): ")
    I = get_input("Current (I): ")
    R = get_input("Resistance (R): ")
    P = get_input("Power (P): ")

    result = Solve_DC(V, I, R, P)
    print(f"The DC values are Voltage: {result[0]:.3f} Volts, Current: {result[1]:.3f} , Resistance: {result[2]:.3f} Ohms and Power: {result[3]:.3f} Watts")

elif Decision == "2":
    Resistances_Series = []
    Resistances_Parallel = []
    Series = input("How many resistors do you have in series? ")
    Parallel = input("How many resistors do you have in parallel? ")
    for i in range(0, len(int(Series))):
        Ohms = input("What is the resistance for each one in Series?")
        Resistances_Series.append(Ohms)
        print(Resistances_Series)
    for i in range(0, len(int(Parallel))):
        Ohms = input("What is the resistance for each one in Parallel?")
        resistance_calculator(1, 0, Ohms)

        print(Resistances_Series)


