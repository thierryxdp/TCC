def filtra_pares(vari):
    final = ()
    if vari[0] % 2 == 0:
       final = final + (vari[0],)

    if vari[1] % 2 == 0:
        final = final + (vari[1],)

    if vari[2] % 2 == 0:
        final = final + (vari[2],)

    if vari[3] % 2 == 0:
        final = final + (vari[3],)

    return final