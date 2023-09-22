def lingua_p(palavra):
    "Altera uma palavra adequando-a a língua do P"
    "str -> str"
    palavra_nova = str.lower(palavra)
    resultado = ''
    for caractere in palavra_nova:
        if caractere in 'aeiou':
            resultado = carectere + 'p' + caractere
    return resultado