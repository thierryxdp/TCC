def retira_pontuacao(texto):
    texto = str.replace(texto,'.',' ')
    texto = str.replace(texto,'!',' ')
    texto = str.replace(texto,'?',' ')
    texto = str.replace(texto,'...',' ')
    texto = str.replace(texto,',',' ')
    texto = str.replace(texto,';',' ')
    texto = str.replace(texto,':',' ')
    texto = str.replace(texto,'-',' ')
    return texto

def inverte(frase):
    '''função que, dada uma frase e com a ajuda de uma
    outra função (que retira todods os caracteres de 
    pontuação da mesma frase), retorna uma outra frase 
    que contém as mesmas palavras da frase de entrada 
    na ordem inversa e sem letras maiúsculas
    str -> str'''
    texto = retira_pontuacao(frase)
    texto = str.lower(texto)
    lista = str.split(texto)
    y = len(lista)
    x = 0
    novo = ''
    while x != y - 1:
        novo = novo + lista[y - 1 - x] + ' ' 
        x = x + 1
    novo = novo + lista[y - y]
    return novo