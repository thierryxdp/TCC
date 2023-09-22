def retira_pontuacao(frase):
    lista_pares=[n for n in frase if n =='!']
    del lista_pares
    lista_filtrada=(''.join(frase))
    return lista_pares