def lingua_p(palavra):
    palavra.lower()
    lp=""
    for i in palavra:
        if i in "aeiouãâàáúé":
            lp += i+ "p"+ i
        else:
            lp+=i
    return lp