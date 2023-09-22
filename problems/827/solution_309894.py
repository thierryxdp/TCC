def qtd_divisores(numero):
    """..."""
    divisores=()
    contador=0
    while contador<=numero:
        contador+=1
        if numero%contador == 0:
            divisores+=contador
    return len(divisores)