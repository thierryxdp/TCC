def faltante(pecas):
    N = len(pecas)+1
    
    for i in range(1, N):
    	if i not in pecas:
            return i