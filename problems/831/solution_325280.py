def lingua_p(palavra):
    """coment"""
    s=""
    for i in range(len(palavra)+1):
        if palavra[i] in "aeiouAEIOU":
            palavra[i]=palavra[i]+"p"+palavra[i]
        s+=palavra[i]
    return s