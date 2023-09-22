def lingua_p(palavra):
    for a in palavra:
        if a == 'a' or a =='e' or a =='i' or a =='o' or a =='u':
            palavrap = palavra.replace(a,a+'p'+a)
            return(palavrap)