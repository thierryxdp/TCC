def retira_pontuacao(frase):
    #professor não sabia como chamar a função da questão anterior,
	#por isso reenscrevi
	''' usando a função substituição retiro todos o pontos e 
	depois faço sua inverção primeiro cortando com a função split
	e invertendo com o índice'''
    if '.' in frase:
        frase = frase.replace('.',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
    if '...' in frase:
        frase = frase.replace('...',' ')
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ':' in frase:
        frase = frase.replace(':',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    return frase
def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.split(frase,)
    frase = list(frase[::-1])
    frase = str.join(' ',frase)
    frase = str.lower(frase)
    return frase