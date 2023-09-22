# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Esta função recebe uma string e retorna o número(int) de palavras contidas na string
    
    	Parametros
        ----------
        frase (string) : frase
    """
    f0 = f.split(' ')
    if len(f0[-1]) == 0:
        f0.pop(-1)
    if len(f0[0]) == 0:
        f0.pop(0)
    return len(f0)