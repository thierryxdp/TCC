def retira_pontuacao(frase):
    """Essa funcao recebe 'frase' str -> str
substitui as pontuacoes utilizando a funcao replace
de str
Obs: no hifen (-) eh adicionado um espaco ' ', diferentemente
das demais pontuacoes pois elas jah contam com ele naturalmente
na escrita.
str -> str"""
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ",", "")
    frase = str.replace(frase, ":", "")
    frase = str.replace(frase, ";", "")
    frase = str.replace(frase, ".", "")
    frase = str.replace(frase, "!", "")
    frase = str.replace(frase, "?", "")
    frase = str.replace(frase, "...", "")
    
    return frase

def inverte(frase):
    """Essa funcao faz uso da funcao retira_pontuacao(frase).
str -> str
Apos obtermos a frase da funcao retira_pontuacao(frase), utilizamos
o atributo .lower() de str para deixar todos caracteres minusculos.
Apos isso, transformamos a frase (str) em list, removendo seus espacos
Depois invertemos a lista [::-1] e retornamos a frase em str invertida."""

    frase = retira_pontuacao(frase).lower()
    lista = str.split(frase, " ")
    lista = lista[::-1]
    return str.join(" ", lista)