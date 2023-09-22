def conta_frases(texto):
    """Funcao que recebe um texto armazenado em uma string e retorna o
numero de frases que aparecem nesse texto. Cada frase termina com um ponto
final, exclamacao, interrogacao ou reticencias. Exclamacao e interrogacao nao
podem estar em sequencia e so aparecem no texto terminando uma frase"""
    frase_subst = texto.replace("!", "#").replace("?","#").replace("...","#").replace(".","#")
    nova_frase = frase_subst.count("#")
    return nova_frase