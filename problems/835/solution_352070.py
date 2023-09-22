def melhor_volta(mat):
    cnls1=[]
    cnls2=[]
    for i in range(len(mat)):
        cnls1.append(min(mat[i]))
        cnls2.append(mat[i].index(min(mat[i])))
    indtemp=cnls1.index(min(cnls1))
    indvolt=cnls2[indtemp]
    mat1=list(range(1,6))
    venc=mat1[indtemp]

    return (venc,min(cnls1),indvolt+1)