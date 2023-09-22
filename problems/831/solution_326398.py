def lingua_p(palavra):
    n=0
    nova=palavra
    for i in palavra:
        if palavra[n] in "aeiouAEIOU":
            nova=str.replace(nova,nova[n],nova[n]+"p"+nova[n])
        n=n+1
    return nova