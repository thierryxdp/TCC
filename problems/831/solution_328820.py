def lingua_p(palavra):
    palavra = palavra.lower()
    lista = list(palavra)
    for letra in lista:
        if letra in "aeiou":
            indice = lista.index(letra)
            lista[indice] = '{}p{}'.format(letra, letra)
    return ''.join(lista)