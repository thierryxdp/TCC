def faltante(lista_de_pecas):
    """dada uma lista com N − 1 inteiros numerados de 1 a N, descubra qual número inteiro deste
    intervalo está faltando (list[int,int,...,int] --> int"""
    i = 0 #define-se o contador
    while i < len(lista_de_pecas): #repete-se o comando da linha 6 a 8 enquanto o valor do contador for menor que o da lista, ou seja, o processo será repetido para todos os elementos da lista
        if lista_de_pecas[i] != i+1 : #verifica-se se elemento i da lista está fora de ordem
            return i+1 #se estiver, retorna o número da peça que falta
        i = i+1 #aumenta-se o valor do contador
    return len(lista_de_pecas)+1 #caso a peça faltando seja a última da lista ordenada do número de peças, devolve o número da peça que falta   
     

#Problemas propostos no classroom para o IDLE
from random import randint