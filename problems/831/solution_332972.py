def lingua_p(p):
    '''dada uma palavra, retorna esta palavra tradutiza para lingua P
    str-> str'''
    minusc=palavra.lower()
    palavraP=''
    vogais='aeiouáéíóúã'
    for p in minusc:
        palavraP+=p
        if p in vogais:
            palavraP+='p'+p
    return palavraP