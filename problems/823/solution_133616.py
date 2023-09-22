def faltante(pecas):
    N = len(pecas)+2
    
    for i in range(1, N):
    	if i not in pecas:
            return i