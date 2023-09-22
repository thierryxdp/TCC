def lingua_p(palavra):
    """função que traduz uma palavra para a língua do p
    str->str"""
    palavra2=[]
    for letra in palavra:
        list.append(palavra2,letra)
    for vocal in palavra:
        if vocal in "AEIOUaeiou":
            list.insert(palavra2,list.index(palavra2,vocal)+1,'p'+vocal)
            
        

    return str.join('',palavra2)