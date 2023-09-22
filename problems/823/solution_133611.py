def faltante(pecas):
    N = len(pecas)+1
    
    for i in range(N):
    	if i not in pecas:
            return i