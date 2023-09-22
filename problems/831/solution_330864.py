def lingua_p(palavra):
    palavra=palavra.lower()
    palavra=palavra.split()
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=()
    for p>=0 in vogal:
        if palavra[p] in vogal:
            p=p+1
        nova_palavra=palavra[:p]+'p'+palavra[p:]        
    return nova_palavra