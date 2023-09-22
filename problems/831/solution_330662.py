def lingua_p(palavra):
    nova_palavra = ""
    for i in range(len(palavra)):
        if palavra[i] not in "bcdfghjklmnpqrstvwxyz":
            nova_palavra = nova_palavra + palavra[i] + "p"
        nova_palavra = nova_palavra + palavra[i]
    return nova_palavra