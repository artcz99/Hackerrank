#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    else:
        if n in range(2, 5 + 1):
            print("Not Weird")
        elif n in range(6, 20 + 1):
            print("Weird")
        else:
            print("Not Weird")