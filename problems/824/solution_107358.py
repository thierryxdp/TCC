def uppCons(frase:str)->str:
    """Dada uma frase, retorna todas as consoantes em maiúscula, e as demais exatamente como estavam, e na mesma ordem."""
    nova_frase=''
    proximo=0
    while proximo<len(frase):
        caracter=frase[proximo]
        if frase[proximo] in 'bcçdfghjklmnpqrstvwxyz':
            caracter=str.upper(caracter)
        nova_frase=nova_frase+caracter
        proximo=proximo+1
    return nova_frase