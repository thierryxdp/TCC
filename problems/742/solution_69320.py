def substitui(s,x,i):
    """Função que retorna uma str 's', mas com o caracter substituido a letra indicada em i.
       str, str, int -> string"""
   
    return str(s[0:i])+str(x)+str(s[i+1:])