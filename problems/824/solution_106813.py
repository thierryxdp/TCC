def uppCons(frase):
    """Função que recebe como entrada uma frase e retorna essa mesma frase com todas
    as suas consoantes em caixa alta, enquanto as vogais permanecem da mesma forma
    que foram fornecidas."""
    """str-->str"""
    i=0
    nova_frase=''
    while i<len(frase):
        if frase[i] not in 'aáeéioóuúAEIOU':
            nova_frase=nova_frase+str.upper(frase[i])
        else:
            nova_frase=nova_frase+frase[i]
        i=i+1
    return nova_frase