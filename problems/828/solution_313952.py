def primo(n):
    """Dado um número, determina se este número é primo ou 
    não; caso seja retorna verdadeiro, caso não seja 
    retorna falso;
    int -> bool"""
    a = list(range(1,n+1))
    resultado = [] 
    
    for x in a : 
        if n%x==0 :
            list.append(resultado,x)
    
    if len(resultado) > 2 :
        return False
    else : 
        return True