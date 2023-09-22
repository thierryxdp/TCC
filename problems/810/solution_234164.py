def inverte(frase):
    '''função que, a partir de uma frase, inverte e retorna a mesma de trás pra frente sem pontuação e letras maiúsculas; str -> str'''
    resultado = str.split(str.lower(frase))
    
    return resultado