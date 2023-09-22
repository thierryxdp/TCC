def uppCons(frase:str)->str:
    """Dada uma frase, retorna todas as consoantes em maiúscula, e as demais exatamente como estavam, e na mesma ordem."""
    nova_frase=''
    proximo=0
    while proximo<len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyz':
            frase[proximo]=str.upper(frase[proximo])
        nova_frase=nova_frase+frase[proximo]
        proximo=proximo+1
        return nova_frase