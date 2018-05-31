import pandas as pd
from sklearn import preprocessing
import mat_generator as matgen

# 0: idle
# 1: jump
# 2: slide
action_space = [0, 1, 2]
input_size = 12 * 9

def detect_state_jump(mat):
    if mat[7][2] != 1:
        print('state: <jump>')

def need_to_jump(mat):
    for i in range(9):
        if mat[7][3] == 4:
            print('state: <need to jump>')

def detect_state_slide(mat):
    if mat[7][0] == 1:
        print('state: <slide>')


mat_idle = matgen.state_matrix('idle')
matgen.print_colored_matrix(mat_idle)

mat_jump = matgen.state_matrix('jump')
detect_state_jump(mat_jump)
matgen.print_colored_matrix(mat_jump)

mat_slide = matgen.state_matrix('slide')
matgen.print_colored_matrix(mat_slide)



