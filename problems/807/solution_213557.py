def conta_frases(frase):
    '''Função que recebe uma frase e retorna o somatório de frases que transforma os sinais de final
de frase a seguir (?,!,.,...) em sublista nova
Entrada(lista)
Saída(int)'''
    interrogacao=frase.count('?')
    exclamacao=frase.count('!')
    ponto=frase.count('.')
    reticencia=frase.count('...')
    pontos=ponto - 3*reticencia
    return interrogacao + exclamacao + reticencia + pontos