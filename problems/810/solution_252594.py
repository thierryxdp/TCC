def inverte(frase):
    nova_frase = str.lower(retira_ponto(frase))
    lista = str.split(nova_frase, ' ')
    list.reverse(lista)
    final = str.join(' ', lista)
   
    return final