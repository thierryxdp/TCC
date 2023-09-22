def lingua_p(s):
    """
    traduz para a lingua do p
    """
    vogais=["a","e","i","o","u","A","E","I","O","U"]
    for i in range(len(vogais)):
        if vogais[i] in s:
            nova=str.join(vogais[i]+"p"+vogias[i],str.split(s,vogais[i]))
    return nova