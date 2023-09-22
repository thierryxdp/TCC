def filtraMultiplos(lista, n):
    """função que recebe lista e retorna lista 
    com números múltiplos do número n
    list, int--> list"""

    multiplos = []  #cria lista vazia para múltiplos
    contador = 0  #inicia o contador em zero

    while contador < len(lista):  #enquanto contador for menor que tamanho da lista
        if lista[contador] % n == 0:  #se elemento da lista for divisível por n
            multiplos.insert(contador, lista[contador])  #insere elemento na posição relacionada ao valor do contador
        contador += 1  #incrementa contador
        
    return multiplos  #retorna lista com múltiplos de n