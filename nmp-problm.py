import datetime
import numpy as np
import calendar

#Creating a matrix which is the multiplication of 2 matrices

matrix_a = np.array(([1,3,5],[7,9,11]))
matrix_b = np.array(([2,4],[6,8],[10,12]))
matrix_c = np.dot(matrix_a, matrix_b)

print(matrix_c)

#Creating a matrix and transposing it

matrix = np.array(([10,20,30],[40,50,60],[70,80,90]))
transposed_matrix = np.transpose((matrix))

print(transposed_matrix)

#All days of November 2024 as an array (Y-M-D format)

november = np.arange("2024-11", "2024-12", dtype="datetime64[D]")
print(november)
#Also:
print(calendar.month(2024,11))
