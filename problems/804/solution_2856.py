def filtra_pares1(tupla):
    '''Filtra uma tupla de 4 elementos inteiros para retornar uma nova tupla com os elementos pares da tupla original
    entrada: tupla(int,int,int,int)
    saida: tupla(int,int,int,int)'''
    tupla_vazia = () 
    if tupla[0]%2==0:
        tupla_vazia + (tupla[0],)
    if tupla[1]%2==0:
        tupla1=tupla_vazia + (tupla[0],)
        tupla1 + (tupla[1],)
    if tupla[2]%2==0:
        tupla2=tupla1 + (tupla[1],)
        tupla2 + (tupla[2],)
    if tupla[3]%2==0:
        tupla3=tupla2 + (tupla[2],)
        return tupla3 + (tupla[3],)