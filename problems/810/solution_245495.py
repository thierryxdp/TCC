'retira caracteres especiais de uma string e a retorna os substituindo por espaço, as invertendo'
def inverte(frase):
    lista_ponc = set('.;:!?/\\,#@$&)(\'"-')
    palavras = frase.split(' ')
    fraseinv = ' '.join(reversed(palavras))
    return ''.join(i if i not in lista_ponc else '' for i in(fraseinv)).lower()