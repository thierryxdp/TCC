def inverte(frase):
    '''Função que dada uma determinada frase retorna o seu inverso, retirando todos os sinais de pontuação e
    colocando todas as letras em caixa baixa'''
    frase = frase.replace('.', '').replace('?', '').replace('!', '').replace(';', '').replace(':', '').replace(',',' ').replace('-',' ')
    frase = frase.lower().split
    frase = frase[-1::-1]
    frase = str.join(' ',frase)
    return frase