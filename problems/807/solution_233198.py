#Função que dado um texto armazenado em uma string,conta e retorna o número de frases que aparecem neste texto;str = int
def conta_frases(texto):
    pontofinalA = str.count(texto,'.')
    interrogacao = str.count(texto,'?')
    exclamacao = str.count(texto,'!')
    reticencias = str.count(texto,'...')
    verificacao = reticencias * 3
    pontofinalB = pontofinalA - verificacao

    
    return pontofinalB + interrogacao + exclamacao + reticencias