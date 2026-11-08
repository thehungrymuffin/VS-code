# Ohm's Law
import math
def Solve_DC(V = None, I = None, R = None, P = None):
    known = {"V": V, "I": I, "R": R, "P": P}

    if ([V, I, R, P].count(None) > 2):
        raise ValueError("You did a bad thing and did not give enough info!")
    
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
        V = math.sqrt(P * R)
        I = math.sqrt(P / R)

    try:
        R = V / I
    except ZeroDivisionError:
        raise ZeroDivisionError("You did bad job with 0 in demoninator")
        
    P = V * I
    return V, I, R, P

def get_input(prompt):
    user_val = input(prompt)
    if user_val:
        return float(user_val)
    else:
        return None


Decision = input("Which Function would you like to use? ")
if Decision == "1":
    V = get_input("Voltage (V): ")
    I = get_input("Current (I): ")
    R = get_input("Resistance (R): ")
    P = get_input("Power (P): ")
    print(f"The DC values are (V, I, R, P): { Solve_DC(V, I, R, P) }")

    # Testing purposes
    print(Solve_DC(V=5, I=2, R=3))
    print(Solve_DC(5))
