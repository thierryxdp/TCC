'''Função que recebe uma tupla com 4 elementos e retorna apenas os
que são pares'''
# int, int, int, int -> int
def filtra_pares(tupla):
    #cria uma lista para os elementos
    lista_tupla = []
    
    #cria um for para checar todos os elementos
    for elemento in tupla:
        
        #cria uma condição para que só haja elementos pares
        if elemento%2==0:
            
            #adiciona o elemento par na lista, foi usado o .append para adicionar na lista MAIS itens
            lista_tupla.append(elemento)
    
    #retorna a tupla, foi usado tuple() para retornar na forma de tupla
    return tuple(lista_tupla)