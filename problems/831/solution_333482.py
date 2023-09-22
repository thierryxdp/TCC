def lingua_p(palavra):
    for a in palavra:
        if a == 'aeiouáéíóú':
            palavraa = palavra.replace(a,a+'p'+a)
            return(palavraa)