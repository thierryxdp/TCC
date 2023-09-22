'''Função que retira a pontuação de uma string'''
def retira_pontuacao(frase): 
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase= frase.replace(',',' ')
    if ':' in frase:
        frase = frase.replace(':',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    if '.' in frase:
        frase = frase.replace('.',' ')
    if '...' in frase:
        frase = frase.replace('...',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
        
    return frase
'''Função que retorna as palavras da string de trás pra frente,em minúsculo, sem pontuação
	String -> String'''
def inverte(frase):
    frase = retira_pontuacao(frase)
    val = frase.split()
    '''lav = list(reversed(val))'''
    lav = list(val[-1:-(len(val)+1):-1])
    StringFinal = (' '.join(lav))
    return StringFinal.lower()