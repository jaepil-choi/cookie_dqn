import random

# 12*9의 우리 grid와 동일한 크기의 2차원 list matrix를 뽑는다.
def rmatrix():
    matrix = []
    for _ in range(9):
        rand = [random.choice(range(5)) for _ in range(12)]
        matrix.append(rand)

    return matrix
# 1차원 배열로 해야하지는 않을까?


