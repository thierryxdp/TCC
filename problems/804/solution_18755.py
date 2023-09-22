"""
Nesta função eu tive uma enorme dificuldade em fazer e aplicar o conceito 
da "lista", nas primeiras tentativas eu tentei fazer um if dando return 
para cada situação, porém ao usar tupplas esse conceito não funciona do 
jeito que a questão pede, logo tive que mudar toda a estrutura e fazer do
jeito a seguir.
tupple -> tupple
"""
def filtra_pares(tup):
    lista = ()
    if tup[0]%2 == 0:
        lista = lista + (tup[0],)
	if tup[1]%2 == 0:
        lista = lista + (tup[1],)
    if tup[2]%2 == 0:
        lista = lista + (tup[2],)
    if tup[3]%2 == 0:
        lista = lista + (tup[3],)
    return lista