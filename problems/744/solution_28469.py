# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna a string s como hashtag no seu ínicio, no seu meio, e no final.
    string --> string"""
    
    t = len(s)/2
    
    nova_s = '#' + s[:int(t)] + '#' + s[int(t):] + '#'
    
    return nova_s