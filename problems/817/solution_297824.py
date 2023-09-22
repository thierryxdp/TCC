def acima_da_media(lis_aluno):
    quant_aluno=len(lis_aluno)
    soma_nota=sum(lis_aluno)
    media=soma_nota/quant_aluno
    l=list.append(lis_aluno,media)
    l1=list.sort(lis_aluno)
    if media in lis_aluno:
        del lis_aluno[:list.index(lis_aluno,media)]
        li=list.remove(lis_aluno,media)
        return li
    else:
        del lis_aluno[:list.index(lis_aluno,media)]
        return lis_aluno