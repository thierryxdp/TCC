def primo(numero):
    '''funcao que retorna se o numero da entrada é primo ou nao
    list->bool'''
    primo=0
    resultado=''
    for valor in list(range(1,numero+1)):
        if numero%valor==0:
            divisao=numero/valor
            primo=int((divisao/divisao)+primo)
        if primo==2:
            resultado=True
        if primo!=2:
            resultado=False
    return resultado