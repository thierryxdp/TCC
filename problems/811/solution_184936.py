# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def calchao(lista,H,L):
    
    A= lista[0]
    B= lista[1]
  
    if (B<=H and A<=L) or (B<=L and A=H):
        return True
    else:
        return False