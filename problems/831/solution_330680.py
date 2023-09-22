def lingua_p(frase):
    """Função que recebe uma palavra como parâmetro e retorne a mesma traduzida para a língua do P"""
    frase=str.lower(frase)
    texto=''
    for i in frase:
        if i in "aeiouáéíóú":
            texto+=i+'p'+i
            
        if i not in "aeiouáéíóú":
            texto+=i
    return texto