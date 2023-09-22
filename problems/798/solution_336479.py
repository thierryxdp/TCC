def freq_palavras(f):
    '''
    Recebe uma frase na string f. Transforma essa frase
    em uma lista l. Abre um dicionário. Verifica se a
    palavra p está contida em l. Posteriormente conta a
    quantidade de vezes que aparece e insere em c.
    E por fim adiciona a chave no dicionário.
    '''
    l = f.split(); d = {}
    for p in l:
        c = l.count(p)
        d[p] = c
    return d