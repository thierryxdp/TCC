def substitui(s,x,i):
    """A função substitui o caractere de valor i na string por um caractere x imputado
    assinatura: str, int, str --> str
    Uso do fatiamento de strings para contornar a imutabilidade. Devo lembrar da notação ":", pois
    estava confundindo com as vírgulas de tuplas
    """
    return s[0:i] + x + s[i+1:]