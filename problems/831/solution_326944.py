def lingua_p(palavra):
    "Retorna a palavra traduzida pela língua do P. str->str"
    vogais = 'aeiouáàâãéêíóôõúAEIOUÁÀÂÃÉÊÍÓÔÕÚ'
    resultado = ''
    for letra in palavra:
        if letra in vogais:
            resultado += letra+'p'+str.lower(letra)
        else: 
            resultado += letra
    return resultado