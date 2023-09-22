def substitui(s,x,i):
    """"Retorna string s substituindo pelo caracter x da posicao i
    da própria string endo 0 a primeira letra da string,
    ou seja, de onde começa a contagem. 
    Temos que os primeiros inputs são da forma string mesmo no teste,
    então apesar de estar como observação o 
    "# string, int, int -> string" vou fazer de forma diferente a 
    assinatura.
    
    Assinatura: string, string, int -> string
    
    Testes:
    substitui('jhonatan', 'x',3)=='jhoxatan'
    substitui('roberto', 'r', 0)=='roberto'
    substitui('padrão','4',1)=='p4drão'
    substitui('teamo','',2)=='temo'
   
    """"
    if i==0:
        return x + s[1:]
    elif i== len(s):
        return s[0:len(s)] + x
    return s[0:i] + x + s[i+1:]