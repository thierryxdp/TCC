# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
"""Resulta em uma string com # no início,no meio e no final dela.
Entrada:string
Saída:String"""
    i=len(s)//2
    return "#"+s[0:i]+"#"+s[i:]+"#"