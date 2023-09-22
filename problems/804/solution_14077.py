#Calcula e realiza a filtragem de uma tupla
def filtra_pares(s):
    final = ()
    if s[0]%2 == 0:
        final += (s[0],)
    if s[1]%2 == 0:
        final += (s[1],)
	if s[2]%2 == 0:
        final += (s[2],)
    if s[3]%2 == 0:
        final += (s[3],)
    return final