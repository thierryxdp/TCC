# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    recebe duas listas de mesmo tamanho, e retorna uma lista 
    ,de tamanho dobrado, com itens sendo os itens das duas recebidas só que intercalados
   
    list, list -----> list
    
    """
    nova = lista1*2
    nova[1::2] = lista2
    nova[::2] = lista1
    
    return nova