def lingua_p(palavra):
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=[]
    for p in list(palavra):
        if vogal in list(palavra):
            nova_palavra=vogal+'p'+vogal
        if vogal not in list(palavra):
            nova_palavra=nova_palavra
    return nova_palavra