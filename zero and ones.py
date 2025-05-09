#ou are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

# Read the space-separated integers, split them, and convert them into a tuple for shape
shape = tuple(map(int, input().split()))

# Create the arrays with the given shape and integer type
print(np.zeros(shape, dtype=int))  # Print array of zeros
print(np.ones(shape, dtype=int))   # Print array of ones
