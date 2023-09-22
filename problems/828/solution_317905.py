def primo(numero):
    """..."""
    contador=0
    divisores=[]
    while contador<=numero:
        if numero%contador == 0:
            divisores.append(contador)
        contador +=1
    if divisores == [1,numero]:
        return true
    else:
        return false