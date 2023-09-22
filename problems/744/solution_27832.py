# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que ao receber uma string, retorna o caractere "#" no início, no meio,
    e no fim dessa string;
    str -> str"""
    return str('#') + s[:len(s)//2]+str('#')+s[len(s)//2:len(s)]+str('#')