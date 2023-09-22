def concatenacao(a, b):
    """função que recebe a, b e retorna a concatenação dessas strings na forma abba.
    string -> string
    Explicação: basta criar duas listas, uma para a e outra para b e concatená-las usando o sinal +, agrupando todos os elementos."""
    lista1 = a
    lista2 = b
    return lista1[0:]+lista2[0:]+lista2[0:]+lista1[0:]