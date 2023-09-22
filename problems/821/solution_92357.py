def fatorial(numero):
    fator=numero
    seguinte=numero-1
    
    while numero-seguinte<numero:
        fator=fator*(seguinte)
        seguinte=seguinte-1
        return fator