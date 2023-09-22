def posLetra(frase,letra,numero):
    """verificamos se os elementos da frase possuem a letra, ate achar o numero
    pedido de ocorrencia, depois mostramos a localizacao da letra na frase, de
    acordo com o numero de ocorrencia pedido. Se existir menos ocorrencias
    da letra do que a ocorrencia pedia, a funcao retorna -1.
    string, string, int -> int"""
    i=0
    t=0
    while i<len(frase):
        if frase[i] == letra:
            t=t+1
            if t==numero:
                return i
        i=i+1
    return -1