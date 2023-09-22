def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma palavra na língua do P;str->str'''
    palavra2=str.lower(palavra)
    resposta=palavra2
    usadas=''
    for letra in palavra2:
        if letra not in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'+usadas:
            resposta=str.replace(resposta,letra,letra+'p'+letra)
            usadas=usadas+letra
    return resposta