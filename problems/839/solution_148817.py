def carros (passageiros, capacidade=5):
    if passageiros < capacidade:
        saida = 1
    elif passageiros >= capacidade:
        saida = (passageiros // 6) 
    
    return saida