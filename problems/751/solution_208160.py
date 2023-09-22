# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase qualquer, a função irá dizer quantas palavras esta frase possui.
	É necessário inserir as informações em aspas simples.
    Recebe valores do tipo string e retorna um inteiro que será a quantidade de palavras."""
    quantidade_de_palavras = frase.split()
    return len(quantidade_de_palavras)