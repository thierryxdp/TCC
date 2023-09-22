def substitui(s,x,i):
    """ Retorna um string s com seu elemento na posição i substituido por um carctere x; str, str, int -> str"""
     str1 =str(s)
     a = len(s)
        return str1[0:(i-1)] + str(x) + str1[(i+1):a]