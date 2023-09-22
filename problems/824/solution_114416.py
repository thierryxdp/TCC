def uppCons(frase):
    """dado uma frase, a função retorna todas as suas consoantes em maiúsculas, junto
    com os demais caracteres exatamente como estavam na frase original;
    str->str"""
    consoantes='bcçdfghjklmnpqrstvwxyz'
    ind_frase=0
    frasenova=''
    while ind_frase<= (len(frase)-1):
        if frase[ind_frase] in consoantes:
            conUP= str.upper(frase[ind_frase])
            frasenova=frasenova+conUP
        else:
            frasenova=frasenova+frase[ind_frase]
        ind_frase=ind_frase+1
        
    return frasenova