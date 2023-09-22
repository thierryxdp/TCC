def filtraMultiplos(n):
    multiplos = ()
    if n[0]/n[1] == 0:
        multiplos = multiplos + (n[0],)
    if n[0]/n[2] == 0:
        multiplos = multiplos + (n[1],)
    if n[0]/n[3] == 0:
        multiplos = multiplos + (n[2],)
    if n[0]/n[4] == 0:
        multiplos = multiplos + (n[3],)
    if n[0]/n[5] == 0:
        multiplos = multiplos + (n[4],)
    if n[0]/n[6] == 0:
        multiplos = multiplos + (n[5],)
    if n[0]/n[7] == 0:
        multiplos = multiplos + (n[6],)