def lingua_p(palavra):
    palavra=palavra.split()
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=0
    for p in range(len(palavra)):
        if palavra[p] in vogal:  
            nova_palavra=nova_palavra+palavra[p]
        if palavra[p] not in vogal:
            nova_palavra=nova_palavra
    return nova_palavra