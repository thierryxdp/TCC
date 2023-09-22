def conta_frases(texto):
    '''Função que calcula o número de frases escritas em um texto dado.
    Conta-se como frase todo texto terminado por ., ..., ? e !
    str->int'''
    quant1=str.count(texto,'.')
    quant2=str.count(texto,'!')
    quant3=str.count(texto,'?')
    quant4=str.count(texto,'...')
    return (quant1 + quant2 + quant3 + quant4)- quant4*3