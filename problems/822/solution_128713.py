def repetidos(numeros):
    contagem = 0
    ultimo = None
    for numero in numeros:
        if ultimo == numero:
            contagem += 1
            
        ultimo = numero
    
    return contagem