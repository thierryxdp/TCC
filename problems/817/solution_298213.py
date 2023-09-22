def acima_da_media(lis_aluno):
    '''Calcula a média do parâmetro lis_aluno e 
    retorna os valores maiores que a média
    list->list'''
    quant_aluno=len(lis_aluno)
    soma_nota=sum(lis_aluno)
    media=soma_nota/quant_aluno
    if media in lis_aluno:
        list.sort(lis_aluno)
        del lis_aluno[:list.index(lis_aluno,media)]
        list.remove(lis_aluno,media)
        return lis_aluno
    else:
        list.append(lis_aluno,media)
        list.sort(lis_aluno)
        del lis_aluno[:list.index(lis_aluno,media)]
        list.remove(lis_aluno,media)
        return lis_aluno