''' 
You've got a 5x5 matrix, consisting of 24 zeroes and a single number one.
Let's index the matrix rows by numbers from 1 to 5 from top to bottom,
let's index the matrix columns by numbers from 1 to 5 from left to right.
In one move, you are allowed to apply one of the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i+1 for some integer i (0<i<5)
Swap two neighboring matrix columns, that is, columns with indexes j and j+1 for some integer j (0<j<5)

You think that a matrix looks beautiful,
if the single number one of the matrix is located in its middle
(in the cell that is on the intersection of the third row and the third column).
Count the minimum number of moves needed to make the matrix beautiful.


Input:

The input consists of five lines, each line contains five integers:
the j-th integer in the i-th line of the input represents the element of the matrix
that is located on the intersection of the i-th row and the j-th column.
It is guaranteed that the matrix consists of 24 zeroes and a single number one.


Output:

Print a single integer, the minimum number of moves needed to make the matrix beautiful.
'''




# ------------------------------------------------- Solution -------------------------------------------------


#First input the matrix from the user which is performed in the line below
ar = [[input() for j in range(5)] for i in range(5)]
k=0
l=0 #Initialize 2 variables 
#Printing the list of lists (A 2D List) for confirmation
print (ar)

for i in range(5):
	for j in range(5):
		if ar[i][j] == '1': #We are finding that digit whose value is 1 and not 0
			k = i   
			l = j         #Once we obtain the position, store the indices in the variables k & l 
			break		  #Come out the loop once obtained the indices

''' To know the number of moves needed to reach the center of the  matrix i.e., (2,2), we need to subtract the positions from (2,2)
    and perform abscissa to get a positive value and add those to get the total number of moves
	

Example Matrix:
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

Position of 1 is (1,4)
We need to go to (2,2)
So, final = abs(1-2) + abs (4-2)
          = 1 + 2
          = 3
'''
final = abs(k-2) + abs(l-2)

print (final)

