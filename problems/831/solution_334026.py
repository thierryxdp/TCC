def lingua_p(palavra):
    vogal='aeiouáéíóàãõôâê'
    palavra=str.lower(palavra)
    cont=0
    for x in palavra:
        if x in vogal:
            palavra=palavra[:cont+1]+'p'+x+palavra[cont+1:]
        cont=cont+1
    return palavra