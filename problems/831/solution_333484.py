def lingua_p(palavra):
    for a in palavra:
        if a == 'a','e','i','o','u','á','é','í','ó','ú':
            palavraa = palavra.replace(a,a+'p'+a)
            return(palavraa)