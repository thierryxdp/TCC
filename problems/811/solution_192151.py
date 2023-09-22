# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,H,L) :
    
 """funçao que recebe as dimensões de um colchão e medidas
   e retorna se é possível ou não passar por ela;
   list,int, int -> bool"""
 if medidas [0] ‹= L and medidas [1] ‹= H:
   return True
 else:
   return False