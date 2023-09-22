def inverte(s):
    lista = retira_pontuacao(s)
    lista1 = lista.split()
    lista1.reverse()
    invertida_str = ','.join(lista1)
    invertida_M = retira_pontuacao1(invertida_str)
    return str.lower(invertida_M)