# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
 """Funcao que retorna True ou False caso um colchão consiga passar, ou não
        por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões
        do colchão D.
        Entrada: lista(float,float,float) ; Saída: int,int"""
    

    if list(medidas)[1] <= H:
        return True
    else:
        return False