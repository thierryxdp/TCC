def lingua_p(palavra):
    '''retorna a palavra na linga do p
    str->str'''
    palavra=str.lower(palavra)
    palavraNova=''
    for letra in palavra:
        if letra in 'aeiou':
            palavraNova=palavraNova+letra+'p'+letra
        else:
            palavraNova=palavraNova+letra