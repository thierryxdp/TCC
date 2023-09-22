def lingua_p(palavra):
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=[]
    for p in list(palavra):
        if vogal in list(palavra):
            nova_palavra = vogal + 'p' + vogal+1      
    return nova_palavra