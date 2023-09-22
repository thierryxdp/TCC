#-----------------EXERCICIO 3------------------------

def posLetra (texto,letra,numero):
    '''retorna posicao da 'letra' na ocorrencia 'numero'
       str, str, float -> int'''

    i = 0               #contador
    lista_posicao = []  #acumulador
    
    while i<len(texto):
        if texto[i] == letra:
            list.append(lista_posicao, i)
        i += 1

    if numero>len(lista_posicao):
        return -1
    return lista_posicao[numero-1]