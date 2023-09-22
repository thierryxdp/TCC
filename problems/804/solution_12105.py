#Start your python function here

'''Função que filtra os valores da lista informadas e retorna uma tupla
com apenas os valores pares, de inicio a tupla vem vazia, e será incrementada
com um item da lista cada vez que ele for par, apenas para os 4 itens'''

def filtra_pares(elements):
    tupla1 = () #A tupla precisa ser vazia para qualquer item da lista senão os 4 definidos em condição
    if elements[0]%2 == 0:
        tupla1 = tupla1 + (elements[0],)
    if elements[1]%2 == 0:
        tupla1 = tupla1 + (elements[1],)
        
    if elements[2]%2 == 0:
        tupla1 = tupla1 + (elements[2],)
        
    if elements[3]%2 == 0:
        tupla1 = tupla1 + (elements[3],)
       
    return tupla1