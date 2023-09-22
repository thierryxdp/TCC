def bolos(A,B,C):
    """calcula quantos bolos consegue fazer dados os ingredientes A,B eC"""
    QA = A//2
    QC = B//3
    QC = C//5
    return min(QA,QB,QC)