def lingua_p(string):
    palavra=''
    for c in string:
        if c in 'AEIOUaeiouáéíóúãõâêõ':
            palavra+=c+'p'+c
        else:
            palavra+=c
    return palavra