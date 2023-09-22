def lingua_p(palavra):
    """função que traduz uma palavra para a língua do p
    str->str"""
    palavra2=[]
    for letra in palavra:
        list.append(palavra2,letra)
    for vocal in palavra2:
        if vocal in "AEIOUaeiou":
            palavra2[list.index(palavra2,vocal)]=vocal+"p"
        

    return str.join('',palavra2)