def lingua_p(string):
    '''funçao que recebe uma string e retorna ela na lingua do p.
str->str'''  
    palavra=''
    for c in string:
        if c in 'AEIOUaeiouáéíóúãõâêõ':
            palavra+=c+'p'+c
        else:
            palavra+=c
    return palavra