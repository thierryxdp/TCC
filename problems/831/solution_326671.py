def lingua_p(palavra):
    palavra.lower()
    vogal='aâãäáàeêéèëiïíìoõöóòuüúù'
    i=0
    for vogal in palavra:
        palavra[i]=palavra[i]+'p'+palavra[i]
        i+=1
    return palavra