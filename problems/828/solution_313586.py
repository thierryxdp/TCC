#Armazenarei os divisores de n numa lista
#Se len(lista) = 0, logo o número é primo
def primo(n):
    ''' Função que diz se um dado número n é primo
    int -> bool '''
    lista = []
    numero = list(range(n))
    for x in numero:
        if x >= 2 and n % x == 0:
            list.append(lista, x)
    return len(lista) == 0