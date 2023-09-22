def inverte(frase):
    nova_frase = retira_pontuacao(frase)
    nova_frase = str.lower(nova_frase)
    nova_frase = str.split(nova_frase)
    list.reverse(nova_frase)
    nova_frase = str.join(' ',(nova_frase))
    return nova_frase