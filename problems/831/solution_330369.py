def lingua_p(palavra):
    """pega a palavra e retorna a mesma palavra com "p" introduzidos apos
    cada vogal mais a vogal
    string -> string"""# or "e" or "i" or "o" or "u":
    s=''
    for p in palavra:
        if p == "a":
            s+=p+'pa'
        elif p == "e":
            s+=p+'pe'
        elif p == "i":
            s+=p+'pi'
        elif p == "o":
            s+=p+'po'
        elif p == "u":
            s+=p+'pu'
        else:
            s+=p
    return s