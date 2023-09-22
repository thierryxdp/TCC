# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe uma frase e diz quantas palavras tem nessa frase
    	string --> int"""
    string_separada = str.split(frase)
    return len(string_separada)