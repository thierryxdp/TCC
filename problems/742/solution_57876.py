def substitui(s,x,i):
    """recebe uma str 's', um caractere x e
um int 'i'( entre 0 e o comprimento da string);
exceto que o elemento da posição 'i' deve ser
substituido pelo caractere 'x' | str,int,int -> str
ex: >>> substitui('leonardo','p',5)- 'leonapdo'""" #exemplo basico
    if i >=0 and i < len(s): 
        return s[0:i]+x+s[1+i:] #manipulação através do fatiamento
    else: #caso não esteja dentro do tamanho dado
        return s