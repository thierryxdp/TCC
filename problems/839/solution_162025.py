def carros(passageiros,capacidade=5):
    if passageiros%capacidade==0:
        return passageiros/capacidade
    else:
        return (passageiros/capacidade)+1