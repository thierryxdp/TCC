def uppCons(frase):
    count = 0
    lista = list(frase)
    caracteres = len(lista)
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ç']
    while count != caracteres:
        if lista[count] in consoantes:
            str.upper(lista[count])
        count = count + 1
    return str(lista)