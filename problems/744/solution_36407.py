# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que retorna uma string e insira um dado caractere
    str-> str'''
    x= len(s)
    y= x//2
    return '''#'''+s[:y]+'''#'''+s[y:]+'''#'''