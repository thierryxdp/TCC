def inverte(frase):
    '''Código que conta uma frase de traz pra frente
    str -> str'''
    final = frase.replace('.', ' ')
    interrogacao = final.replace('?', ' ')
    exclamacao = interrogacao.replace('!', ' ')
    virgula = exclamacao.replace(',', ' ')
    travessao = virgula.replace('-', ' ')
    pontos = travessao.replace(':', ' ')
    pontovirg = pontos.replace(';', ' ')
    minusc = str.lower(pontovirg)
    split = minusc.split()
    invertida = split.reverse()
    return str.join(' ', split)