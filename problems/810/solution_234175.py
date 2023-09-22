def inverte(frase):
    '''função que, a partir de uma frase, inverte e retorna a mesma de trás pra frente sem pontuação e letras maiúsculas; str -> str'''
    frase_pura = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-', ' '),',', ' '),':', ' '),';', ' '),'.', ' '),'!', ' '),'?', ' ')
    frase1 = str.split(str.lower(frase_pura))
    frase2 = frase1[:0:-1]
    resultado = str.join(' ',frase2)
    
    
    return resultado