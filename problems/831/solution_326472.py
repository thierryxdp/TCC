def lingua_p(s):
    """
    traduz para a lingua do p
    """
    vogais=["a","e","i","o","u","A","E","I","O","U","á","é","í","ó","ú","Á","É","Í","Ó","Ú"]
    for i in range(len(vogais)):
        if vogais[i] in s:
            s=str.join(vogais[i]+"p"+vogais[i],str.split(s,vogais[i]))
    return s