def lingua_p(palavra):
    '''Recebe uma palavra em portugues e a retorna em lingua do p
    string -> string'''
    i=0
    palavra_f=''
    palavra=palavra.lower()
    palavra_separada=[]
    for i in range(0,len(palavra)):
        palavra_separada.append(palavra[i])
        i=i+1
    for letra in palavra_separada:
        if letra in 'bcdfghjklmnpqrstvxywz':
            palavra_f=palavra_f+letra
        else:
            palavra_f=palavra_f+letra+'p'+letra
    return palavra_f