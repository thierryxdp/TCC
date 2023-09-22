# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas de tamanho 3,gera uma nova lista(L3) que é formada intercalando os elementos 
    da lista1 e da lista2
    
    exemplo
    L1=[a,c,e] e L2=[b,d,f] gera L3[a,b,c,d,e,f]
    entrada-> lista,lista. cada lista com 3 elementos 
    retorna-> lista( com seis elementos)"""
    
    L3=lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]
    
    return L3