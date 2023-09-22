def lingua_p(frase):
    '''função que retorna uma frase com um P adcionado a vogal anterior'''
    vogais = ['a','e','i','o','u']
    novafrase = []
    for index in range (0,len(frase)):
        list.append(novafrase,frase[index])
    indice = 0
    for vezes in range(0,len(novafrase)):
        if novafrase[indice] in vogais:
            list.insert(novafrase, indice + 1, 'p' + str(novafrase[indice]))
            indice = 2 + indice
        else:
            indice  = 1 + indice
    return str.join('', novafrase)