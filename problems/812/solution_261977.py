def retira_pontuacao(frase):
    virgula= str.replace(frase,',',' ')
    dois_pt= str.replace(frase,':',' ')
    pt_virula= str.replace(frase,';',' ')
    ponto= str.replace(frase,'.',' ')
    interrogacao= str.replace(frase,'?',' ')
    exclamacao= str.replace(frase,'!',' ')
    travessao_virgula= virgula.replace('-',' ')
    if ',' in frase:
        return str.replace(virgula,'.',' ')
    elif ('-' and '.' and '.') in frase:
        return travessao_virgula.replace('.',' ')
    elif '-' and '!' in frase:
        return str.replace(travessao,'!',' ')
    elif ':' in frase:
        return str.replace (dois_pt,'.',' ')
    elif ';' in frase:
        return str.replace(pt_virgula,'.',' ')
    elif '!' in frase:
        return exclamacao
    elif '?' in frase:
        return interrogacao