# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Esta funcao recebe duas listas de tamanho 3 e intercala seus elementos,
    na ordem L1 e L2, respectivamente.
    Entrada: list,list ([],[])
    Saída: list ([])"""
    lista3=[0,0,0,0,0,0]
    lista3[0]=lista1[0]
    lista3[1]=lista2[0]
    lista3[2]=lista1[1]
    lista3[3]=lista2[1]
    lista3[4]=lista1[2]
    lista3[5]=lista2[2]