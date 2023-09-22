def filtra_pares(t):
    if t[0]%2 == 0:
    	t_final = t[0]
    if t[1]%2 == 0:
    	t_final = t_final + tuple(t[1])
    if t[2]%2 == 0:
    	t_final = t_final , tuple(t[2])
    if t[3]%2 == 0:
    	t_final = t_final , tuple(t[3])
    return t_final