'''Recebe uma frase e retorna a mesma frase com todas as consoantes maiusculas'''
#str -> str

def uppCons(frase):
    lista = list(frase)
    contador = 0
    vogais = 'aeiouAEIOU'
    while contador < len(lista):
        if lista[contador] not in vogais:
            lista[contador] = str.upper(lista[contador])
        contador = contador + 1
    return str.join('', lista)