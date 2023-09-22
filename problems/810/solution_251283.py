def retira_p(x):
    """Retornar uma função que, dada uma frase, retira-se a pontuação da mesma e que sejam substituídas por espaços; str=>str"""
    exclamacao = str.replace(x,"!", " ")
    interrogacao = str.replace("!","?", " ")
    virgula = str.replace("?",",", " ")
    reticencias = str.replace(",", "...", " ")
    ponto = str.replace("...",".", " ")
    dois_pontos = str.replace(".",":", " ")
    ponto_virgula = str.replace(":",";", " ")
    travessao = str.replace(";","-", " ")
     
def inverte(frase):
    """Função que, data uma determinada frase, retorne uma outra com as mesmas palavras, mas na ordem inversa, além de estar sem letras maiúsculuas e pontuação; str=>str"""
	passo1 = (retira_p(frase))
    passo2 = str.lower(passo1)
    passo3 = str.split(passo2)
    passo3.reverse()
    return str.join(" ",passo3)