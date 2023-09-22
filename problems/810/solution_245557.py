'retira caracteres especiais de uma string e a retorna os substituindo por espaço, as invertendo'
def inverte(frases):
    frase = frases.replace(',', '')
    lista_ponc = set('.-;:!?/\\,#@$&)(\'"') 
    frasessemp = ''.join(i if i not in lista_ponc else ' ' for i in(frase)).lower( )
    palavras = frasessemp.split(' ')
    r = ' '.join(reversed(palavras))
    return r[1:]