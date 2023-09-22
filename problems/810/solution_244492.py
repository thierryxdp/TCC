def retira_pontuacao (frase):
    """Função que, dada uma frase, retorna com todos os caracteres de pontuação substituídos por espaço
    entrada:string
    saída:string"""
    if '-' in frase:
        frase=str.replace(frase,'-',' ')
    if ',' in frase:
        frase=str.replace(frase,',',' ')
    if ':' in frase:
        frase=str.replace(frase,':',' ')
    if ';' in frase:
        frase=str.replace(frase,';',' ')
    if '!' in frase:
        frase=str.replace(frase,'!',' ')
    if '?' in frase:
        frase=str.replace(frase,'?',' ')
    if '...' in frase:
        frase=str.replace(frase,'...',' ')
    if '.' in frase:
        frase=str.replace(frase,'.',' ')
    return frase

def inverte(frase):
	"""Função que, dada uma frase, retorna outra frase, contendo as mesmas palavras na ordem inversa, sem letras maiúsculas e sem pontuação
    entrada:string
    saída:string"""
    frase1= retira_pontuacao(frase)
    minuscula= str.lower(frase1)
    lista= str.split(minuscula)
    lista_reversa= list.reverse(lista)
    return str.join(' ',lista)