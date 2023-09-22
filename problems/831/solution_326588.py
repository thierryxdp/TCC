def lingua_p(palavra):
    
    palavra.capitalize()
    vogal='aàãäáâeèëéiïíìoõôóòöuùúûü'
    i=0
    string=str()
    for vogal[i] in palavra[i]:
        palavra[i] = palavra[i]+'p'+palavra[i]
        i+=1
    return palavra