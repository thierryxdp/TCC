def inverte(frase):
    '''Faça uma função que retorne a frase sem pontuação, minúscula e invertida, str -> str'''
    pontuacao = str('')
    oracao = str.split(str.lower(str.replace(frase,',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao)))
    inverter = [::-1]
    return str.join(oracao, inverter)