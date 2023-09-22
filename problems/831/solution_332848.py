def str_lista(string):
    lista = []
    for letra in string:
        lista.append(letra)
    return lista

def lista_str(lista):
    string = ''
    for elem in lista:
        string += elem
    return string

def lingua_p(string):
    palavra = str_lista(string)
    for i,letra in enumerate(palavra):
        if letra in "aeiouAEIOU":
            palavra[i] = letra + 'p'
    return lista_str(palavra)