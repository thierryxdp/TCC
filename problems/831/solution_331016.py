def lingua_p(palavra):
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=[]
    for p in list(palavra):
        if vogal in list(palavra):
            nova_palavra=nova_palavra+palavra[p]
    return nova_palavra