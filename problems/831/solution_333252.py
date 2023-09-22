def lingua_p(palavra):
    '''função que dada uma palavra, retorna ela escrita com a liguagem do P, que consiste basicamente em acrescentar uma letra p antes e cada vogal'''
    palavra = palavra.lower()
    consoantes = 'bcçdfghjklmnpqrstvwxyz'
    vogais = 'a,ã,á,â,e,é,ê,i,í,î,o,õ,ó,ô,u,ú,û'
    lingua_do_p = ''
    for letra in palavra:
        if letra in consoantes:
            lingua_do_p += letra
        if letra in vogais:
            lingua_do_p += letra + 'p' + letra
    return lingua_do_p