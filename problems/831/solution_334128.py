def lingua_p(palavra):
    vogal='aeiouáéíóúàãõâêô'
    palavra=str.lower(palavra)
    contador=0
    for x in palavra:
        if x in vogal:
            palavra= palavra[:contador+1]+'p'+x+palavra[contador+1:]
            contador=contador+2
        contador=contador+1
    return palavra