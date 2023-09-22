# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que insere o caractere "#" no início, meio e final de uma string fornecida pelo usuário;
    str -> str'''
    resto = len(s)%2 #calculando se há resto na divisão do comprimento da palavra
    meio = int(len(s)/2)
    if resto == 0:
        return "#" + s[0:meio] + "#" + s[meio:len(s)] + "#"
    else:
        return "#" + s[0:round(meio)+1] + "#" + s[round(meio)+1:len(s)] + "#"