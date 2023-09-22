def uppCons(palavra):
    consoantes = ['b', 'c', 'd', 'f', 'g','h', 'j', 'k', 'l', 'm','n','p','q','r', 's','t','v','w','x','y','z','ç']
    lista = list(palavra)
    index = 0
    for letra in palavra:
        if letra in consoantes:
            lista[index] = letra.upper()
        else:
            lista[index] = letra
        index = index + 1
    word = ''.join(lista)
    return word