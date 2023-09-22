def inverte(frase):
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    if '-' or ',' or '.' in frase:
    return str.join(reversed(str.split(ponto_final)))
    
    elif '?' in frase:
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    return str.join(reversed(str.split(ponto_interrogacao)))
    
    elif '!' in frase:
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    return str.join(reversed(str.split(ponto_exclamacao)))