def lingua_p(palavra):
    palavra=palavra.split()
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=()
    p=0
    for p in range(len(palavra)):
        if palavra[p] in vogal:            
            nova_palavra=palavra[:p]+'p'+palavra[p:]
        if palavra[p] in not vogal:
            nova_palavra=palavra[:]
    return nova_palavra