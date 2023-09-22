# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe uma string e insere # no inicio, meio e no 
    final dela"""
    
    x=len(s) 
    
    y=x//2
    
    
    return "#"+str(s[0:y)+"#"+str(s[y:])+"#"