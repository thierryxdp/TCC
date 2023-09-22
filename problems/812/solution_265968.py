def retira_pontuacao(frase):
    '''função que transforma os caracteres de pontuação de um texto
    em espaço
    str->str'''
    
    travessao = frase.replace('-', ' ')
    virgula = travessao.replace(',', ' ')
    dois_pontos = virgula.replace(':', ' ')
    ponto_virgula = dois_pontos.replace(';', ' ')
    ponto_final = ponto_virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    return ponto_exclamacao