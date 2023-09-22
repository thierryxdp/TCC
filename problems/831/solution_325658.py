def lingua_p (palavra):
    ''' a funcao recebe uma palavra e retorna a mesma palavra porem na lingua de p
    entrada:string saida: string'''
    nova = ''
    lista = ['a','e','i','o','u','A','E','I','O','U','á','â','Á','Â','ã','Ã','é','ê','É','Ê','Í','í','ó''Ó','ô','Ô','Õ','õ','ú','Ú']
    for i in range (0, len(palavra)):
        if palavra[i] in lista:
            nova = nova + palavra[i] + 'p' + palavra[i]
        elif palavra[i] not in lista:
            nova = nova + palavra[i]
    return str.lower (nova)