def filtra_pares(tupla):
	final=()
    if tupla[0]%2==0:
        final=final+(tupla[0],)
    if tupla[1]%2==0:
        final=final+(tupla[1],)
    if tupla[2]%2==0:
        final=final+(tupla[2],)
    if tupla[3]%2==0:
        final=final+(tupla[3],)
    return final