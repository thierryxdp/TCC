lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma palavra na língua do P;str->str'''
    palavra2=str.lower(palavra)
    resposta=palavra2
    for letra in palavra2:
        if letra not in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            resposta=str.replace(resposta,letra,letra+'p'+letra)
    return resposta