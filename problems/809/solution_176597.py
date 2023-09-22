def intercala(lista1, lista2):
    """Recebe duas listas de três elementos cada e retorna uma lista que alterna os elementos de lista1 e lista2.
    list, list -> list
    Explicação: dado que ambas as listas possuem três elementos, basta explicitá-los com variáveis correspondentes aos índices das listas e depois criar uma nova lista que alterne os elemenos deles. """
    a=lista1[0]
    b=lista1[1]
    c=lista1[2]
    d=lista2[0]
    e=lista2[1]
    f=lista2[2]
    lista3=[a,d,b,e,c,f]
    return lista3