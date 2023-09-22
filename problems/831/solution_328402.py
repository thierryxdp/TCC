def lingua_p(palavra):
    pala=''
    for letra in palavra:
        if letra in ('a','e','i','o','u') :
            letra=letra +'p'+letra
        pala+=letra
    return (pala)