#Como entrada temos uma lista, uma letra e um indice
#Precisamos analisar a lista e ver onde esta a ocorrencia n da letra
#informada na lista
#retornar esse indice
def posLetra(frase, letra, n):
    """Recebe uma lista, uma letra e um indice.
    A função verificar onde está a ocorrencia n da letra informada
    na lista"""
    i=0
    auxiliar=0
    ocorrencia=0
    while i != n: 
        if letra == frase[i]:
        	auxiliar=i
        i+=1
    return auxiliar