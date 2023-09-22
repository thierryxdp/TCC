def pontos_por_time(lista):
    """[['Cormengo','Flamínthians',[1, 0]],['Flamínthians','Cormengo', [2,2]]]"""
    
    m=lista[0]
    
    
    em=()
    va=()
    vb=()
    
    a= m[0]
    b= m[1]

    n=lista[1]
    p= m[2]
    q= n[2]

    d= p[0]
    e= p[1]
    f=q[0]
    g=q[1]



    pontosa= 3*var+1*er
    pontosb= 3*vbr+1*er

    
    
    if d==e:
        em= em + (1,)
    if f==g:
        em= em + (2,)
    if d>e:
        va= va + (1,)
    if g>f:
        va= va + (2,)
    if e>d:
        vb= vb + (1,)
    if f>g:
        vb= vb +  (1,)
    
    var= int(len(va))
    vbr= int(len(vb))
    er= int(len(em))


    return {a:pontosa, b: pontosb}