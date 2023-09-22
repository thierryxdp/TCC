def lingua_p(plvr):
    #estou definindo a variavel plvr para p_lvr, denotando que foi traduzido para linha do P
    #str->str
    p_lvr = ''
    #deixa em branco para o programa colocar a palavra
    for k in plvr.lower():
        if k in "aáàãeéèiíoóòõuúù":
            p_lvr += k + "p" + k
        else:
            p_lvr += k
    return p_lvr