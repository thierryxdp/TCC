def lingua_p(palavra):
    palavra=palavra.lower()
    palavra=palavra.split()
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=()
    p=0
    for p in range(len(palavra)):
        nova_palavra=palavra[p]