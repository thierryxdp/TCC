#Recebe uma lista
#Precisamos analisar quantas vezes um número da lista
#é igual ao numero imediatamente anterior a ele
#Fazendo essa contagem, precisamos retornar esse valor
def repetidos(lista: list)->int:
    """Recebe uma lista e retorna quantas vezes um número da lista
    é igual ao numero imediatamente anterior a ele"""
    i=0
    numeros=[]
    contador=0
    while i < len(lista):
            if (lista[i] == lista[i-1]):
                contador +=1
            i+=1
    return contador