def lingua_p(palavra):
    '''Retorna a palavra de entrada na lingua do P,
       isto é, a própria palavra com cada vogal seguida
       de 'p' e dela mesma;
       str -> str'''
    palavraP=''
    for letra in palavra:
        palavraP+=letra
        if letra in 'aeiouAEIOU':
            palavraP+='p'+letra
    return palavraP