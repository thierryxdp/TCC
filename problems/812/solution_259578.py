def retira_pontuacao(frase):
    """Função que dado uma frase, retirará todas os caracteres de pontuação da mesma"""
    frase.split(" ")
    frase1=""
    if '.' in frase:
        frase1=str(frase1)+frase.replace('.', ' ')
    if '?' in frase:
        frase1=str(frase1)+frase.replace('?', ' ')
    if '-' in frase:
        frase1=str(frase1)+frase.replace('-', ' ')
    if ':' in frase:
        frase1=str(frase1)+frase.replace(':', ' ')
    if ',' in frase:
        frase1=str(frase1)+frase.replace(',', ' ')
    if ';' in frase:
        frase1=str(frase1)+frase.replace(';', ' ')
	if '!' in frase:
        frase1= str(frase1)+frase.replace('!', ' ')
    return frase1