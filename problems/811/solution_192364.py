# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis]:
def colchao (col,h,l):
    """função que retorna a coesão entre dimensões da porta e colchão"""
             if col[1]<=h or col[1]<= l:
                 return True
             elif col[2] <=h or col[2]<=l:
                return True 
             else:
                return False