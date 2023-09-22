def posLetra(string,letra,n):
    """retorna em que posição da string está a ocorrencia 'n' da letra.
    str,str,int->int"""
    i=0
    x=0
    lista=[]
    while i<n:
        r=str.find(string,letra,x)
        x=str.find(string,letra,x)+1
        i=i+1