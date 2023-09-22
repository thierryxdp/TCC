def uppCons(frase):
    """função que, dada uma frase como parâmetro, retorna a mesma frase porém
    com suas consoantes maiúsculas.

    str -> str

    exemplos:
    uppCons("abcde")=="aBCDe"
    uppCons("gabriel")=="GaBRieL"
    uppCons("qwerty")=='QWeRTY'
    """
    i=0
    frasef=frase
    while i!=len(frase):
        if frase[i] not in "aeiouAEIOUáÁéÉíÍóÓúÚãÃõÕ":
            frasef=frasef[:i]+frasef[i].upper()+frasef[i+1:]
        i=i+1
    return frasef