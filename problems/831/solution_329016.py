def lingua_p(palavra):
    palavra=palavra.lower()
    palavra_p=""
    for letra in palavra:
        if letra in 'aeiouáéíóúàâêôãõ':
            letra+="p"+letra
        palavra_p+=letra
    return palavra_p