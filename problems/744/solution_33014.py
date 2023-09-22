# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe uma string e insere # no inicio, meio e no 
    final dela"""
    
    x=len(s) 
    
    return "#"+str(s[0:x/2])+"#"+str(s[x/2:])+"#"