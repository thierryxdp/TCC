def freq_palavras(s):
    """Recebe uma string e retorna um dicionário. Cada palavra da string se torna uma chave que retorna a frequência da palavra na string.
    Testes: freq_palavras('samuel samuel samuel') == {'samuel': 3}
    freq_palavras('samuel cursino faria') == {'samuel': 2, 'cursino': 1}
    assinatura: str --> dict
    """
    b = s.split()
    x = 0
    d = {}
    while x < len(b):
        d[b[x]] = d.get(b[x],0) + 1
        x = x+1
    return d