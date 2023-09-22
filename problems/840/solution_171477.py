def receita(Xicaras, Ovos, Colheres):
    a = Xicaras//2
    b = Ovos//3
    c = Colheres//5
    if a<=b and a<=c:
        return "No Máximo " + str(a) + " Bolos"
    elif b<=a and b<=c:
        return "No Máximo " + str(b) + " Bolos"
    elif c<=a and c<=b:
        return "No Máximo " + str(c) + " Bolos"