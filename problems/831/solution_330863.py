def lingua_p(palavra):
    palavra=palavra.lower()
    palavra=palavra.split()
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=()
    for p>=0 in vogal:
        if palavra[p] in vogal:
            nova_palavra=palavra[:p]+'p'+palavra[p:]
        p=p+1        
    return nova_palavra