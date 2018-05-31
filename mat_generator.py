import random
from termcolor import colored

# 12*9의 우리 grid와 동일한 크기의 2차원 list matrix를 뽑는다.
def rmatrix():
    matrix = []
    for _ in range(9):
        rand = [random.choice(range(5)) for _ in range(12)]
        matrix.append(rand)
        print(rand)
    return matrix

# 수동으로 state 생성
# idle의 경우
def state_matrix(state):
    matrix = [[0] * 12 for i in range(9)]    # 0으로 초기화
    if state == 'idle':
        for i in range(9):
            for j in range(12):
                if i == 8:
                    matrix[i][j] = 3   # 바닥

                matrix[5][1] = 1    # 쿠키
                matrix[5][2] = 1
                matrix[6][1] = 1
                matrix[6][2] = 1
                matrix[7][1] = 1
                matrix[7][2] = 1

                matrix[6][4] = 7    # 젤리
                matrix[6][5] = 7
                matrix[6][6] = 7
                matrix[4][8] = 7
                matrix[4][9] = 7

                matrix[6][8] = 4    # 장애물
                matrix[6][9] = 4
                matrix[7][8] = 4
                matrix[7][9] = 4

    if state == 'jump':
        for i in range(9):
            for j in range(12):

                if i >= 3:
                    matrix[1][1] = 1    # 쿠키
                    matrix[1][2] = 1
                    matrix[2][1] = 1
                    matrix[2][2] = 1
                if i == 8:
                    matrix[i][j] = 3   # 바닥


                matrix[0][3] = 7    # 젤리
                matrix[0][4] = 7
                matrix[1][5] = 7
                matrix[1][6] = 7

                matrix[4][3] = 4    # 장애물
                matrix[4][4] = 4
                matrix[5][3] = 4
                matrix[5][4] = 4
                matrix[6][3] = 4
                matrix[6][4] = 4
                matrix[7][3] = 4
                matrix[7][4] = 4

    if state == 'slide':
        for i in range(9):
            for j in range(12):

                if i <= 4:
                    matrix[0][3] = 4     # 장애물
                    matrix[0][4] = 4
                    matrix[1][3] = 4
                    matrix[1][4] = 4
                    matrix[2][3] = 4
                    matrix[2][4] = 4
                    matrix[3][3] = 4
                    matrix[3][4] = 4

                if i >= 6:
                    matrix[7][0] = 1
                    matrix[7][1] = 1
                    matrix[7][2] = 1
                    matrix[7][3] = 1

                if i == 8:
                    matrix[i][j] = 3     # 바닥

                matrix[5][3] = 7         # 젤리
                matrix[5][4] = 7
                matrix[6][3] = 7
                matrix[6][4] = 7

    return matrix


def print_colored_matrix(mat):
    # 그리드 매트릭스 출력
    for i in range(9):
        for j in range(12):
            value = mat[i][j]
            if value == 1:  # 쿠키
                color = 'yellow'
            elif value == 7:  # 젤리
                color = 'blue'
            elif value == 4 or value == 3:
                color = 'red'  # 4: 장애물, 3: 바닥
            elif value == 0:
                color = 'white'
            print(colored(value, color), end="  ")
        print("\t")
            # gridstring+= str(value)+"   "
    print("-----------------------------------------------")


