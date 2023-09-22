def removepontuacao(frase):
    '''função que da uma frase com pontuação, retornando sem pontuação'''
    interrogacao=frase.replace("?"," ")
    exclamacao=interrogacao.replace("!"," ")
    ponto=exclamacao.replace("."," ")
    doispontos=ponto.replace(":"," ")
    pontovirgula=doispontos.replace(";"," ")
    travessao=pontovirgula.replace("-"," ")
    virgula=travessao.replace(","," ")
    return virgula
def inverte(texto):
    '''função que da uma frase, e retorna sem pontuação, minúscula e invertida'''
    pontos=removepontuacao(texto)
    minuscula=str.lower(pontos)
    lista=minuscula.split(" ")
    stringreversa=" ".join(reversed(lista))
    return stringreversa