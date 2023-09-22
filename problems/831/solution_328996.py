def lingua_p(palavra):
    vogal='aeiouáéíóú'
    resultado=''
    for l in palavra:
        if l in vogal:
            resultado+=l+'p'+l
        else:
            resultado+=l
    return resultado