def lingua_p(palavra):
    pala=''
    for letra in palavra:
        if letra in ('a','á','e','é','i','o','u','ú') :
            letra=letra +'p'+letra
        pala+=letra
    return (pala)