def lingua_p(palavra):
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=[]
    for p in list(palavra):
        if vogal in list(palavra):
            vogal=vogal+1
    return vogal