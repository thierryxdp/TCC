'retira caracteres especiais de uma string e a retorna os substituindo por espaço'
def retira_pontuacao(frase):
    palavras = frase.split(' ')
    fraseinv = ' '.join(reversed(palavras))
    lista_ponc = set('-.;:!?/\\,#@$&)(\'"')
    return ''.join(i if i not in lista_ponc else ' ' for i in(fraseinv))