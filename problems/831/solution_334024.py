def lingua_p(palavra):
    vogal='aeiouáéíóàãõôâê'
    palavra=str.lower(palavra)
    cont=0
    for x in palavra:
        if x in vogal:
            palavra=palavra[:cont+2]+'p'+x+palavra[cont+12:]
    return palavra