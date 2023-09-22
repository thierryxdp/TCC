# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase: str) -> int:
    """Recebe uma frase e retorna a quantidade de palavras - ou quantidade
    de elementos separado por ' '- ."""
    #Retira espaços tanto no início quando no fim da string de entrada
    frase_sem_espaco = str.strip(frase)
    #Guarda uma lista com todas palavras - ou elementos separados por ' '- .
    lista_das_palavras = str.split(frase_sem_espaco)
    #Guarda quantas palavras tem em frase
    num_de_palavras = len(lista_das_palavras)
    return num_de_palavras