# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere o caractere "#" no ínicio, no meio e no final da string de 
    entrada;
    str -> str'''
    string = s
    meio = len(string)//2
    caractere = "#"
    return caractere + string[0:meio] + caractere + string[meio:] + caractere