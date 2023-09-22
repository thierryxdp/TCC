def conta_frases(texto):
    """Retorna o número de frases dentro de um texto armazenado em uma string
    Testes: conta_frases('sim. não... talvez? claro!') == 4
    conta_frases('a. b... c... d! e? f.') == 7 
    assinatura: str --> int
    """
    a = texto.count('...')
    b = texto.replace('...', 'xxxxxxxxxxxxx')
    c = b.count('.')
    d = texto.count('?')
    e = texto.count('!')
    return a + c + d + e