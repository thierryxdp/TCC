def lingua_p(palavra):
    """traduz a palavra para alíngua do p"""
    palavra.lower()
    lis=palavra.split()
    i=0
    trad=""
    while i<len(lis):
        if lis[i] in  "aeiou":
            trad=trad+"p"+str(lis[i])
        i=i+1
        else:
            i=i+1
            
    return trad