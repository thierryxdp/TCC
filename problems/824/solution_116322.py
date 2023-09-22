def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna
    a frase com todas as suas consoantes em maiúsculas (e
    os demais caracteres exatamente como estavam na frase
    original)
    str -> str"""
    con_maiusc = ''
    carac = 0
    cons = 'BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjklmnpqrstvwxyz'
    while carac<len(frase):
        	if frase [carac] in cons:
                con_maiusc = con_maiusc +str.upper(frase[carac])
            else:
                con_maiusc = con_maiusc + frase[carac]
            carac= carac+1
            return con_maiusc