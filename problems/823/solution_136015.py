def faltante(lista):
    '''
       Função para achar o numero da peça faltando de um 
       quebra-cabeça de N peças. Recebe uma lista com numeros
       inteiros de 1 a N das peças do quebra-cabeça presentes
       (lista) e retorna o numero que pertence ao intervalo
       [1,N] mas que nao pertence a lista de entrada;
       int->int
    '''
    i=1
    list.sort(lista)
    while lista.count(i)=1:
        peca=i
        i=i+1
    return peca