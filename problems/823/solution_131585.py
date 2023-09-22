def faltante(lista):

    """ Dada uma lista fornecida, esta função nos devolve qual o valor que
        não se apresenta nesta lista. Estamos comparando a lista dada com
        uma outra lista chamada range que tem valores de 1 até N+1 algarismos.
        Este N representa o último termo da lista forncecida.

        list -> int"""

    i=1

    while (i in list(range(1,lista[-1]+1)) and (i in lista)):
        i = i + 1
    return i