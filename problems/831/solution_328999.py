def lingua_p(palavra):
    vogal='aeiouáéíóú'
    resultado=''
    for letra in palavra:
        if letra in vogal:
            resultado+=letra+'p'+letra
        else:
            resultado+=letra
    return resultado
'''dado uma palavra, retorna a mesma traduzida para
a lingua do p
str->str'''