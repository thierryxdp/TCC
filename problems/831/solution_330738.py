def lingua_p(palavra):
    ''' dada uma palavra na lingua portugesa, retorna esta palavra
    traduzida para a lingua do P, onde após cada vogal da palavra
    original é inserida a sequencia de letras 'p' mais a vogal;
    str->str'''
    P=''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            P=P+letra+'p'+letra
        else:
            P=P+letra
    return P