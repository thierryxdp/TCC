def conta_frases(texto):

    if str.count(texto,"...") == 0:
        ret = str.split(texto,"...")
        n_ret = len(ret) - 1
        
        pts = str.split(texto,".")
        n_pts = len(pts) - 1
        
        exc = str.split(texto,"!")
        n_exc = len(exc) - 1
        
        ite = str.split(texto,"?")
        n_ite = len(ite) - 1
        
        frases = n_pts + n_exc + n_ite + n_ret
        return frases
    else:
        a = str.count(texto,"...")

        ret = str.split(texto,"...")
        n_ret = len(ret) - 1
        
        pts = str.split(texto,".")
        n_pts = len(pts) - 3*a-1
        
        exc = str.split(texto,"!")
        n_exc = len(exc) - 1
        
        ite = str.split(texto,"?")
        n_ite = len(ite) - 1
        
        frases = n_pts + n_exc + n_ite + n_ret
        return frases