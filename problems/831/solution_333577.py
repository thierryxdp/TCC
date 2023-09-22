def lingua_p(palavra):
    n = len(palavra)
    letras = ()
    while letras < n:
        if palavra[n] == 'a':
            letras = letras + ('apa',)
        if palavra[n] == 'e':
            letras = letras + ('epe')
        if palavra[n] == 'i':
            letras = letras + ('ipi')
        if palavra[n] == 'o':
            letras = letras + ('opo')
        if palavra[n] == 'u':
            letras = letras + ('upu')
        else:
            letras = letras 
            return(letras)