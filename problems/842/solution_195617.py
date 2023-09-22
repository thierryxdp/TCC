def caso_1(n1,n2,n3,n4):
    if n1>n2 and n4>n3:
        return True
        
def caso_2(n1,n2,n3,n4):
    if (n1>n2 and n4==n3) or (n1==n2 and n4>n3):
        return True
        
def caso_3(n1,n2,n3,n4):
    if (n1>n2 and n4<n3) or (n1<n2 and n4>n3):
        return True
        
def caso_4(n1,n2,n3,n4):
    if n1==n2 and n4==n3:
        return True
         
    
def caso_5(n1,n2,n3,n4):
    if n1<n2 and n4<n3:
        return True
        
        
        
def caso_6(n1,n2,n3,n4):
    if (n1<n2 and n4==n3) or (n1==n2 and n4<n3):
        return True
    
    

def pontos_por_time([x1,x1,[n1,n2]],[n3,n4]):
    """Função que indica entre duas equipes qual fez mais pontos,
    tendo em vista, dois jogos disputados entre essses times.
    Entrada: lista
    Saída: dicionário
    """
   
   
    
    
    if caso_1(n1,n2,n3,n4):
        return {str(x1):6, str(x2):0}
    if caso_2(n1,n2,n3,n4):
        return {str(x1):4, str(x2):1}
    if caso_3(n1,n2,n3,n4):
        return {str(x1):3, str(x2):3}
    if caso_4(n1,n2,n3,n4):
        return {str(x1):2, str(x2):2}
    if caso_5(n1,n2,n3,n4):
        return {str(x1):0, str(x2):6}
    if caso_6(n1,n2,n3,n4) :
        return {str(x1):1, str(x2):4}