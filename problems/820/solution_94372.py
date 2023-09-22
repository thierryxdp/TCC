def posLetra(frase,letra,numero):
    """esta funçao retorna a posição da letra na frase dada de acordo com a ocorrência pré definida pelo numero
    str, str, int-> int"""
    while indice<len(frase):
        a=frase.find(letra,numero)
        if numero==a:
            return a
        else:
            b=frase.find(letra,a)
            return b