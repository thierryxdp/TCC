def bolos (A,B,C):
    """calcula e retorna o número máximo de bolos que podem ser feitos por João considerando que ele tem A xícaras de farinha de trigo,
B ovos e C colheres de sopa de leite. Int, Int, Int-> Int"""
    return min(A//2,B//3,C//5)