def posLetra(frase,letra,numero):
    """esta funçao retorna a posição da letra na frase dada de acordo com a ocorrência pré definida pelo numero
    str, str, int-> int"""
    indice=0
    while indice<len(frase):
        a=frase.find(letra)
        if a==numero:
            return a
        a=frase.find(letra,a)
        indice+=1
    return -1