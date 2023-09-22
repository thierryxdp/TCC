def conta_frases(texto):
    ''' Função que conta a quantidade de frases que há na str texto
    dada de entrada
    str -> int '''

    quant_tres_pontos = str.count(texto,'...')
    sem_tres_pontos = str.replace(texto,'...',' ')
    quant_ponto_final = str.count(sem_tres_pontos,'.')
    quant_exclamacao = str.count(sem_tres_pontos,'!')
    quant_interrogacao = str.count(sem_tres_pontos,'?')

    return quant_tres_pontos + quant_ponto_final + quant_exclamacao + quant_interrogacao