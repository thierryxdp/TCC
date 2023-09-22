def lingua_p(palavra):
    '''dada uma palavra, retorna a mesma com uma letra p após cada vogal
    str->str'''
    for i in (palavra):
        if i in 'aeiouAEIOUÁÉÍÓÚáéíóú':
            palavra=i+'p'+(i+1)
            else:
                palavra=i
    return palavra