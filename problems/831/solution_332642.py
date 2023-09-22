def lingua_p(s):
    """Funçao que traduz uma palavra para a lingua do p.
    string --> string """
    s= s.lower()
    s = str.replace(s,"a","apa")
    s = str.replace(s,"e","epe")
    s = str.replace(s,"i","ipi")
    s = str.replace(s,"o","opo")
    s = str.replace(s,"u","upu")
    s = str.replace(s,"á","ápá")
    s = str.replace(s,"é","épé")
    s = str.replace(s,"í","ípí")
    s = str.replace(s,"ó","ópó")
    s = str.replace(s,"ú","úpú")
    return s