def inverte(frase):
    """funcao que dada uma frase, retorna outra fase com as mesmas palavras,
porem na ordem inversa, sem letras maiusculas e sem pontuacao
str->str"""
    frase_sem_pontuacao = str.lower(retira_pontuacao(frase))
    lista = str.split(frase_sem_pontuacao)
    lista_inversa = list.reverse(lista)
    frase_inversa = str.join(' ',lista)
    return frase_inversa