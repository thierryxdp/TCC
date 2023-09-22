'retira caracteres especiais de uma string e a retorna os substituindo por espaço, as invertendo'
def inverte(frase):
    lista_ponc = set('-.;:!?/\\,#@$&)(\'"')
    frasessemp = ''.join(i if i not in lista_ponc else ' ' for i in(frase))
    palavras = frasessemp.split(' ')
    return ' '.join(reversed(palavras)).lower()