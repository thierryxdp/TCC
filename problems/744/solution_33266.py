# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
     
    
    # A M A # N D A # --> len(nome) = 6
    # J U # L I A #
    
    '''
    n_caract = len(s) 
    meio= n_caract//2
    meio_1 = s[0:meio]
    meio_2 = s[meio:]
    return '#'+ meio_1 + '#' +meio_2+ '#'