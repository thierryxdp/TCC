def lingua_p(palavra):
    palavra=palavra.split()
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=()
    p=0
    for p in range(len(palavra)):
        if palavra[p] in vogal:
            p=p+1