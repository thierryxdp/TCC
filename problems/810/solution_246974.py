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
    texto = retira_pontuacao(frase)
    texto = str.lower(texto)
    lista = str.split(texto)
    y = len(lista)
    x = 0
    novo = []
    while y >= x:
        novo[x] = lista[y - 1 - x]
        x = x + 1
    novo = str(novo)
    novo = str.replace(novo,',',' ')
    novo = str.replace(novo,'[','')
    novo = str.replace(novo,']','')
    return novo