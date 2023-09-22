# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,alturaH,larguraL) :
    
 """funçao que recebe as dimensões de um colchão e medidas
   e retorna se é possível ou não passar por ela;
   list,int, int -> bool"""
 a=[alturaH,larguraL]
 if medidas [0] ‹= min(a) and medidas [1] ‹= max(a):
   return True
 else:
   return False