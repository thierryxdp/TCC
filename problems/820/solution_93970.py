def posLetra(texto,letra,n):
    """Retorna a posição da ocorrência de número n da letra dentro do texto; string,string,int -> int"""
    if list(texto).count(letra)>=n:
        return str.find(str.replace(texto,letra,"@",n-1),letra,0,-1);
    else:
        return -1