def lingua_p(palavra):
    s=""
    for i in range(len(palavra)):
        if palavra[i] not in "bcdfghjklmnpqrstvwxyzç":
            s+=palavra[i]+"p"+palavra[i]
        else:
            s+=palavra[i]
    return s