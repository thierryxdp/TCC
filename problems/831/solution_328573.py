def lingua_p(palavra):
    """Dado uma palavra, retorna essa palavra na lingua do P. string>string"""
    resultado =''
    i=0
    while i < len(palavra):
        if palavra[i] in "aeiouáéíóú":
            resultado += palavra[i] +'p'+palavra[i]
        else:
            resultado += palavra[i]
		i+=1
    return resultado