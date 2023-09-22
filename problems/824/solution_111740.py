def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    vogais=['A','E','I','O','U']
    consoante='b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'
    c_maiuscula=''
    while consoante in frase:
        c_maiuscula+=str.replace(frase,consoante,str.upper(consoante))
    return c_maiuscula