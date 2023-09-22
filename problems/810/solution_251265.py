def retira_p(x):
    """Retornar uma função que, dada uma frase, retira-se a pontuação da mesma e que sejam substituídas por espaços; str=>str"""
    exclamacao = str.replace(x,"!", " ")
    interrogacao = str.replace(x,"?", " ")
    virgula = str.replace(x,",", " ")
    reticencias = str.replace(x, "...", " ")
    ponto = str.replace(x,".", " ")
    dois_pontos = str.replace(x,":", " ")
    ponto_virgula = str.replace(x,";", " ")
    travessao = str.replace(x,"-", " ")
    return travessao
def inverte(frase):
    """Função que, data uma determinada frase, retorne uma outra com as mesmas palavras, mas na ordem inversa, além de estar sem letras maiúsculuas e pontuação; str=>str"""
	passo1 = (retira_p(frase))
    passo2 = str.lower(passo1)
    list.split(passo2)
    lista.reverse()
    return str.join(" ",lista)