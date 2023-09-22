# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    meio = int(len(s)/2)
    
    s_list = list(s)
    
    hash_str = "#"
    
    for i in range(meio):
        hash_str += s[i]
    
    hash_str += "#"
    
    for i in range(meio,len(s)):
        hash_str += s[i]
    
    hash_str += "#"
    
    return hash_str