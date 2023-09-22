def retira_pontuacao(frase):
    """Função que dado uma frase, retirará todas os caracteres de pontuação da mesma"""
    if '.' in frase:
        frase=frase.replace('.', ' ')
    if '?' in frase:
        frase=frase.replace('?', ' ')
    if '-' in frase:
        frase=frase.replace('-', ' ')
    if ':' in frase:
        frase=frase.replace(':', ' ')
    if ',' in frase:
        frase=frase.replace(',', ' ')
    if ';' in frase:
        frase=frase.replace(';', ' ')
	if '!' in frase:
        frase=frase.replace('!', ' ')
    return frase
def inverte(frase):
    """Função que dada uma frase, retornará o contrario da mesma, sem pontuação e sem letras maiusculas"""
    var=retira_pontuacao(frase)
    str.join(( ),(str.split(var))[::-1])