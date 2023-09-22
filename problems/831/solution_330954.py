def lingua_p(palavra):
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=()
    for p in range(len(palavra)):
        if palavra[p] in vogal:  
            nova_palavra=nova_palavra+palavra[p]
        if palavra[p] not in vogal:
            nova_palavra=nova_palavra
    return nova_palavra