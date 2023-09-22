def carros(x,y=5):
    carros_nec = 0
    passageiros = 0
    while passageiros < x:
        carros_nec += 1
        passageiros += 5
    return carros_nec