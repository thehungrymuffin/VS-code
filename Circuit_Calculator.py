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

def resistance_series(Ohms):
    Series = 0
    if len(Ohms) != 0:
        for r in Ohms:
            Series += r
        return Series
    
def resistance_parallel(Ohms):
    try:
        Parallel = 0
        if len(Ohms) != 0:
            for r in Ohms:
                Parallel += (1/(r))
            Parallel = Parallel ** -1
        return Parallel
    except ZeroDivisionError:
        raise ZeroDivisionError("You Divided by 0 buddy")
    
    
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
            





if __name__ == "__main__":
    Decision = input("Which Function would you like to use? 1. DC_calculator 2. Resistance Calculator ")

    if Decision == "1":
        V = get_input("Voltage (V): ")
        I = get_input("Current (I): ")
        R = get_input("Resistance (R): ")
        P = get_input("Power (P): ")

        result = Solve_DC(V, I, R, P)
        print(f"The DC values are Voltage: {result[0]:.3f} Volts, Current: {result[1]:.3f} , Resistance: {result[2]:.3f} Ohms and Power: {result[3]:.3f} Watts")

    elif Decision == "2":
        Resistors_Series = []
        Resistors_Parallel = []

        Series = int(input("How many resistors do you have in series? "))
        Parallel = int(input("How many resistors do you have in parallel? "))

        for i in range(0, Series):
            Ohms = float(input("What is the resistance for each one in Series? "))
            Resistors_Series.append(Ohms)

        for i in range(0, Parallel):
            Ohms = float(input("What is the resistance for each one in Parallel? "))
            Resistors_Parallel.append(Ohms)
 

        if (len(Resistors_Series) and len(Resistors_Parallel) != 0):
            Total_REQ = resistance_parallel(Resistors_Parallel) + resistance_series(Resistors_Series)
            print(f"The Total Resistance in your circuit is {Total_REQ:.3f} Ohms")
        else:
            print("Hey you did not put any resistors")

