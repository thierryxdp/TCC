def substitui(s,x,i):
    """Função que retorna uma str 's', mas com o caracter substituido a letra indicada em i.
       str, str, int -> string"""
    p=i+1
    return str(s[0:i]+str(x)+s[p:-1]