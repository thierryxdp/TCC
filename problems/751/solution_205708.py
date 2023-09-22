# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase,retorna o número de palavras presentes na frase;str->int"""
    l=len(str.split(str(frase)))
    return len(str(frase))-l+1