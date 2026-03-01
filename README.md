# RREF Calculator
A python program that calculates reduced row echelon form (RREF) matrices of user inputted matrices.

## Program Requirements: 
RREF Calculator simply consists of a single .py file, developed in Python version 3.14.2.

## Running the Program
To start the program, simply enter "Python RREF.py", assuming your working directory contains RREF.py. The program supports several command line options including: 
  -a: make the right most column augmented
  -h: show command line options
  -s: show intermediate steps to RREF
  -ra \[int]: round all calculations, along with final output, to \[int] decimal places (max 16)
  -ro \[int]: round final output to \[int] decimal places (max 16)
Multiple options can be entered at once. For example, "Python RREF.py -ra 3 -s". This includes -h, however, using -h will cause the program to simply display the possible options, then terminate. Therefore, using -h negates all other options and the RREF calculation itself.  

Upon running the program, the user will be asked to enter a matrix. This matrix inhabits a single line, with each entry separated by a space, and each row of the matrix separated by a '/'. For example, the 2 x 2 matrix with elements \[1 2] in the first row and \[3 4] in the second is represented as 1 2 / 3 4. The program excepts a variety of format for matrix index values, including integers (ex. 5), decimal numbers in standard notation (ex. 3.125), and fractions of the previous two types (ex. 3.125/5), in the exampled formats. 

