def uppCons(palavra):
    ''' Função que recebe uma string e coloca todas as letras em maiúsculo, exceto pelas vogais.
str -> str
'''
    palavra = palavra.upper()
    palavra = palavra.replace("A", "a")
    palavra = palavra.replace("E", "e")
    palavra = palavra.replace("I", "i")
    palavra = palavra.replace("O", "o")
    palavra = palavra.replace("U", "u")
    return palavra