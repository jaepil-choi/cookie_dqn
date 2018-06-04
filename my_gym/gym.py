import sqlite3
import numpy as np
# import pandas as pd
from sklearn import preprocessing
from mat_generator import rmatrix
import random

# columns = ['ratio', 'amount', 'ends', 'foreigner', 'insti', 'person', 'program', 'credit']
input_size = 9*12

# 0: jump
# 1: slide
# 2: do nothing
action_space = [0, 1, 2]

index = 0
earn = 0 #번돈
deposit = 1 #살수 있는 수량
buy = 0 #산 수량
buy_cost = 0 #산 가격
isTestMode = False

# " isTest: training모드일때는 false, test모드일때는 true"
def reset(isTest=False):
    global index, earn, deposit, buy, isTestMode

    # state = []
    # for col in columns:
    #     state.append( cur[col] )
    # state.append( deposit )

    state = rmatrix()

    return state

# state, reward, done, _
def step(action):
    global index, earn, deposit, buy, buy_cost
    reward = 0
    done = False

    if action==0: #####JUMP
        # if deposit>0:
        #     deposit -= 1
        #     buy += 1
        #     buy_cost = cur['ends']
        # else:
        #     # 살 수 없는 경우에 대한 penalty
        #     #reward = -.1
        #     pass
        change = 0
        reward = 0

    elif action==1: #####SLIDE
        # if buy>0:
        #     deposit += 1
        #     buy -= 1
        #     reward = cur['ends'] - buy_cost
        # else:
        #     # 팔수 없는 경우에 대한 penalty
        #     #reward = -.1
        #     pass
        change = 1
        reward = 1
    elif action == 2: ####DO NOTHING
        change = 2
        reward = 2

    state = []
    # for col in columns:
    #     state.append( cur[col] )
    # state.append(deposit)
    state = rmatrix()
    state = [change]*12*9

    # if isTestMode:
    #     print( index, action, reward )

    # earn : total reward
    #earn += reward

    # 너무 많이 잃으면 그만 두게 할까?
    # if earn<-1:
    #     reward = -100
    #     done = True

    done = True if (random.random() < 0.1) else False

    return [state, reward, done, None]


