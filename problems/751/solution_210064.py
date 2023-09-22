# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Esta funcao recebe uma string e conta quantas palavras ela tem.
    Entrada: str
    Saida: int"""
	semesp=frase.strip()
    semvirg=semesp.strip(',')
    palavras=semvirg.split()
    return len(palavras)