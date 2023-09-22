#Recebe uma frase,uma letra e um indice 
#Retorna qual é a posição da letra na frase no dado indice
#se nao houver, retornar -1
def posLetra(frase:str,letra:str, n:int)->int:
    i=0
    tamanho=len(frase)
    while i<tamanho:
        if letra not in frase:
            return -1