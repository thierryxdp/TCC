def retira_pontuacao(frase):
    """dada uma frase, essa função retorna a frase cm todos os travessoes
    virgulas , dois pontos, ponto e virgula e ponto substituidos por espaço
    str->str"""
    rem_trav=str.replace(frase,'-',' ')
    rem_vir=str.replace(rem_trav,',',' ')
    rem_doispts=str.replace(rem_vir,':',' ')
    rem_pts=str.replace(rem_doispts,'.',' ')
    rem_ptevir=str.replace(rem_pts,';',' ')
    rem_interr=str.replace(rem_ptevir,'?',' ')
    rem_exc=str.replace(rem_interr,'!',' ')
    rem_total=rem_exc
    return rem_total