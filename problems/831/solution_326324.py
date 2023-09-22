def lingua_p(palavra):
    '''dada uma palavra, retorna a mesma com uma letra p após cada vogal
    str->str'''
    vogais='aeiouAEIOUÁÉÍÓÚáéíóú'
    for i in (palavra):
        if i in vogais:
            palavra=i+'p'+i    
        else:
                palavra=i
    return palavra