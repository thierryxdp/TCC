def retira_pontuacao(frase):
    """funcao que, dada uma frase, retorna a frase em que todos
    os caracteres de pontuacao (travessao, virgula, dois pontos, ponto
    e virgula, etc) tenham sido substituidos por espaco
    str -> str"""
    if ',' in frase:
        lista = str.split(frase,',')
        frase = str.join(' ',lista)
    if '-' in frase:
        lista = str.split(frase,'-')
        frase = str.join(' ',lista)
    if ';' in frase:
        lista = str.split(frase,';')
        frase = str.join(' ',lista)
    if ':' in frase:
        lista = str.split(frase,':')
        frase = str.join(' ',lista)
    if '?' in frase:
        lista = str.split(frase,'?')
        frase = str.join(' ',lista)
    if '!' in frase:
        lista = str.split(frase,'!')
        frase = str.join(' ',lista)
    if '.' in frase:
        lista = str.split(frase,'.')
        frase = str.join(' ',lista)
    return frase

def inverte(frase):
    """funcao que dada uma frase, retorna outra fase com as mesmas palavras,
porem na ordem inversa, sem letras maiusculas e sem pontuacao
str->str"""
    frase_sem_pontuacao = str.lower(retira_pontuacao(frase))
    lista = str.split(frase_sem_pontuacao)
    lista_inversa = list.reverse(lista)
    frase_inversa = str.join(' ',lista)
    return frase_inversa