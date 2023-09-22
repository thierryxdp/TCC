def lingua_p(palavra):
    n=0
    nova=""
    for i in palavra:
        if nova[n] in "aeiouAEIOU":
            nova=nova+palavra[n]+"p"+palavra[n:]
        n=n+1
    return nova