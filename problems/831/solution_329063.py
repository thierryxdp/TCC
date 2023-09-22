#Função para inserir 'pe' após cada vogal
def lingua_p(texto):
    #str --> str
    texto_p=''
    for i in texto:
        if i in 'aeiouAEIOUãÃéÊíÍóÓõÕàÀúÚ':
            texto_p = texto_p + i + 'pe'
        else:
            texto_p = texto_p +i
    return texto_p