def lingua_p(palavra):
    '''dada a palavra recebida, devolve uma em que depois de cada vogal da palavra
    original e inserido a sequencia 'p'mais a vogal original.A palavra e devolvida
    toda em minusculo
    str-->str'''
    novap=''
    for i in palavra:
        if(str.lower(i) not in 'bcdfghjklmnpqrstvwxyzç'):
            novap+=i+'p'+i
        else:
            novap+=i
    return str.lower(novap)