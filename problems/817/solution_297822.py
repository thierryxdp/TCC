def acima_da_media(lis_aluno):
    quant_aluno=len(lis_aluno)
    soma_nota=sum(lis_aluno)
    media=soma_nota/quant_aluno
    l=list.append(lis_aluno,media)
    l1=list.sort(lis_aluno)
    if media in lis_aluno:
        li=list.remove(lis_aluno,media)
        del lis_aluno[:list.index(lis_aluno)]
        return lis_aluno
    else:
        del lis_aluno[:list.index(lis_aluno)]
        return lis_aluno