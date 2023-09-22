def carros(passageiros,capacidade):
    if passageiros%capacidade==0:
        return passageiros/capacidade
    else:
        return (passageiros/capacidade)+1