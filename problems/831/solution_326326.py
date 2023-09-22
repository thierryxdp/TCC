def lingua_p(palavra):
    '''recebe uma palavra e retorna a mesma com uma letra p após cada vogal contida na palavra original
    str->str'''
    plavra=''
    for i in palavra:
        if i in 'aeiouAEIOUÁÉÍÓÚáéíóú':
            plavra+=i+'p'+i
        else:
            plavra+=i
    return plavra