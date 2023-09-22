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
        elif p == "á":
            s+=p+'pá'
        elif p == "é":
            s+=p+'pé'
        elif p == "í":
            s+=p+'pí'
        elif p == "ó":
            s+=p+'pó'
        elif p == "ú":
            s+=p+'pú'
        else:
            s+=p
    return s