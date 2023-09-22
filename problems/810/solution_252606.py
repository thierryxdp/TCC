def retira_pontuacao(frase):
    """ Retira todas as pontuações do texto e as substitui por espaçoes"""
    pontuacao = [';',':',',','.','-','!','...']
    for i in pontuacao:
        frase = str.replace(i, ' ',[0:)
    return frase
def inverte(frase):
    """Retorna uma frase com suas palavras em ordem inversa"""
    lista = str.split(retira_pontuacao(frase))
    list.reverse(lista)
    var1 = ''
    for termo in lista:
        if termo != lista[-1]:
            var1 += termo + ' '
        else:
            var1 += termo
        return str.lower(var1)