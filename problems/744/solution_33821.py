# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Função que recebe uma string e insere o 
    caractere '#' no início, no meio e no final.
    Entrada: str
    Saída: str """
    meio = len(s)//2
    nova_frase = '#' + s[:meio] + '#' + s[meio:] + '#'
    return nova_frase