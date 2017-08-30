
import numpy as np

def nextthing():
    var = np.random.rand(1)
    if var<0.3:
        print('Attack human!')
    elif var<0.7:
        print('Be cute.')
    else:
        print('Make weird noises.')