def uppCons (frase: str) -> str:
    """Função que recebe uma frase e retorna uma frase com
    todas as suas consoantes em maiúsculas, e os demais 
    caracteres são mantidos os mesmos."""
    i = 0
    novafrase = list(frase)
    while i < len(novafrase):
        if novafrase[i] in "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z":
       		novafrase= novafrase.upper(novafrase[i])
        i = i+1
    return frase