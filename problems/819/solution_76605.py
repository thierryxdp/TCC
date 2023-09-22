def filtraMultiplos(lista,numero):
    '''A funcao recebe uma lista e um numero, e devolve uma outra lista
    apenas com os elementos que forem multiplos do numero;
    list, int -> list'''
    lista_nova = []
    i = 0
    while i<len(lista):
        if lista[i]%numero == 0:
            list.insert(lista_nova,i,lista[i])
        i = i + 1
        
    return lista_nova
#Defini a função e apartir dai criei as condições
#Com o while eu pude criar toda uma condção e regras para rodar a função
#list.insert insere o valor especificado na posição especificada.