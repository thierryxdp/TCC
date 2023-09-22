def uppCons (frase: str) -> str:
    """Função que recebe uma frase e retorna uma frase com
    todas as suas consoantes em maiúsculas, e os demais 
    caracteres são mantidos os mesmos."""
    i = 0
    novafrase = ""
    while i < len(frase):
        if frase[i] in "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z":
        novafrase += str.upper(frase[i])
        novafrase = frase
        i = i+1
    return frase