# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe como parâmetro uma string contendo uma frase e retorna o número de palavras da frase, podendo a frase ter espaços no início e no final;
	assinatura: string --> int
    Casos de teste:
    quant_palavras('Meu nome é Luciano') == 4
    quant_palavras('Curso Engenharia Naval na UFRJ') == 5
    quant_palavras('E estou fazendo computação 1 no primeiro período') == 8
    """
    frase = frase.split()
    return len(frase)