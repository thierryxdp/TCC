def bolos(a,b,c):
    '''calcula o numero minimo de bolos com o numero de 
    xicaras de farinha(a), numero de ovos(b) e o numero 
    de colheres de leite(c)'''
    x=int(a/2)
    y=int(b/3)
    z=int(c/5)
    return min(x,y,z)