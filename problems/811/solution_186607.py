def colchao(medidas,H,L):
    """Retorna um booleano respondendo se um colchao passa por uma
    porta a partir das medidas do colchao e da porta dadas como entrada.
    list -> bool"""
    if medidas[1]<=H or medidas[2]<=H:
        return True 
    if medidas[1]<=L or medidas[2]<=L:
        return True
    else:
        return False
    
# Casos de testes:
# colchao([25,120,250],120,200)== True
# colchao([30,150,200],120,200)== True
# colchao([25,175,200],120,150)== False