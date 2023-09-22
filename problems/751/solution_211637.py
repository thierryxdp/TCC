# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retornar uma quantidade de palavras de uma frase;
    string - > int"""
    palavras = frase.split(" ")
    return len(palavras)

def conta_frases(texto):
    """Retornar uma quantidade de frases de um texto;
    string - > int"""
    texto = texto.replace("!",".").replace("?",".").replace("...",".")
    frases = texto.split(". ")
    return len(frases)