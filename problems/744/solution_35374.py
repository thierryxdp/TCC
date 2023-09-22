# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
     '''recebe uma string 's' e retorna essa string com um caractere '#' 
    no iníco, no meio e no fim (quando o número ímpar, ela ficará um
    caractere para esquerda em relação ao meio)(str-> str)'''
     n = len(s)
     s_mod = '#' + s[0:((n//2))] + '#' + s[((n//2)+2):] + '#'
     return s_mod