def filtra_pares(a):
    	tuplaN = ()
        if a[0] % 2 == 0:
            tuplaN = tuplaN + (a[0],)
        if a[1] % 2 == 0:
            tuplaN = tuplaN + (a[1],)
        if a[2] % 2 == 0:
            tuplaN = tuplaN + (a[2],)
        if a[3] % 2 == 0:
            tuplaN = tuplaN + (a[3],)
            return tuplaN