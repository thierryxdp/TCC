def faltante(list_num_int):
    '''
    função que recebe uma lista de numeros inteiros que representam as peças do quebra cabeças
    nuemradas de 1 a N. Após isso, ela retorna o numero da peça faltante para Joaozinho pedir.
    list -> int
    '''
    
    if 1 not in list_num_int:
        return 1
        
   	x_fora_Lista=0
    contador_stop_exe=0
    
    while contador_stop_exe<(len(list_num_int)-1):
        if list_num_int[contador_stop_exe]!=list_num_int[contador_stop_exe+1]-1:
            x_fora_Lista=x_fora_Lista+(contador_stop_exe+2)
        contador_stop_exe=contador_stop_exe+1
    if x_fora_Lista==0:
               return list_num_int[-1]+1
            
    return x_fora_Lista