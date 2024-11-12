import hi
import sys
import os
'''
import random as rd
import time as ti
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
'''

s1 = '{x}'
s2 = '''
    This is a MultiLine String that I can use as a Multiline Comment as well
'''


if __name__ == '__main__':
    sys.stdout.write(hi.sayHi(hi.say_hi("hello_world\n\n")))
    print(s1.format(x = "How you're doing?"), s2, sep = '\n\n ## \n\n', end = f'\n\n{locals()}')