def conta_frases(texto):
    ''' conta a quantidade de frases de um texto dado, sendo que cada frase vai ate uma certa pontuacao,
    nesse caso seria exclamacao, interrogacao,ponto final ou reticencias
    str->int'''
    texto=texto.replace(('!'),'final frase ')
    texto=texto.replace(('?'),'final frase ')
    texto=texto.replace(('...'),'final frase ')
    texto=texto.replace(('.'),'final frase ')
    
    return texto.count('final frase')