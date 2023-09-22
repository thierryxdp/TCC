def faltante(lista):
    '''Função que recebe uma lista de numeros inteiros(sem repetição), em ordem crescente
    e de tamanho N-1, onde cada numero corresponde à uma peça de um quebra-cabeça que está com 1
    peça faltando.A função retorna um numero inteiro que está no intervalo da lista
    e que não pertence à lista, logo é a peça que está faltando.
    Entrada: list. Saída:int'''
    num_pecas=len(lista)-1
    list.sort(lista)
    c=0
    if lista[0]!=1:
        return 1
    while c<num_pecas:
        if lista[c]!=lista[c]+1:
            return lista[c]+1
        if lista[-1]!=lista[-2]+1:
            return lista[-2]+1
        c=c+1