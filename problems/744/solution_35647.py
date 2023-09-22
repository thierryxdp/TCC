# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que retorna, dada uma string como valor de entrada, essa mesma string acrescentada de uma "#" no início, uma no meio e uma no fim da string
    str-> str"""
    x= len(s)
    y= x//2
    return "#"+s[:y]+"#"+s[y:]+"#"