def inverte(frase):
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    return str.join(reversed(str.split(ponto_exclamacao)))