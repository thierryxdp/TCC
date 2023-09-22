def conta_frases(texto):
    """Funcao que retorna um texto armazenado em uma string e retorna o
numero de frases que aparecem nesse texto. Cada frase termina com um ponto
final, exclamacao, interrogacao ou reticencias. Exclamacao e interrogacao nao
podem estar em sequencia e so aparecem no texto terminando uma frase"""
    textosubs = texto.replace("!", "#").replace("?","#").replace("...","#").replace(".","#")
    contar = textosubs.count("#")
    return nova_frase