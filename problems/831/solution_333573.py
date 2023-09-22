def lingua_p(palavra):
    n = len(palavra)
    for a in range(1,n+1):
        if a == 'a' or a =='e' or a =='i' or a =='o' or a =='u':
            palavrap = palavra.replace(a,a+'p'+a)
            return(palavrap)