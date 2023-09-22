def faltante(pecas):
    N = len(pecas)
    
    for i in range(1, N):
    	if i not in pecas:
            return i