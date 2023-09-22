# Conta o número de frases
# seja periodo uma frase qualquer
# str->int
def conta_frases(periodo):
    """Função que calcula e retorna a quantidade de frases do período(valor de entrada)"""
    """str->int"""
    return str.count(periodo,".")-2*(str.count(periodo,"..."))+ str.count(periodo,"!")+str.count(periodo,"?")