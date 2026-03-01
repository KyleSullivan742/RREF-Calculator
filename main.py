import sys


augment = False
showSteps = False
roundAllTo = -1
roundOutputTo = -1
i = 1
while i < len(sys.argv):
    if(sys.argv[i] == "-h" or sys.argv[i] == "help"):
        print(" -a: make the right most column augmented")
        print(" -h: show command line options")
        print(" -s: show intermediate steps to RREF")
        print(" -ra: [int]: round all calculations, along with final output, to [int] decimal places (max 16)")
        print(" -ro: [int]: round final output to [int] decimal places (max 16)")
        exit()
    elif(sys.argv[i] == "-a"):
        augment = True
    elif(sys.argv[i] == "-s"):
        showSteps = True
        stepNumber = 1
    elif(sys.argv[i] == "-ra" and int(sys.argv[i+1])):
        
        roundAllTo = int(sys.argv[i+1])
        if roundAllTo > 16 or roundAllTo < 0:
            print("Invalid round length detected. Terminating.")
            exit()
        i += 1
    elif(sys.argv[i] == "-ro" and int(sys.argv[i+1])):
        
        roundOutputTo = int(sys.argv[i+1])
        if roundOutputTo > 16 or roundOutputTo < 0:
            print("Invalid round length detected. Terminating.")
            exit()
        i += 1
    else:
        print(f"Invalid option \"{sys.argv[i]}\" detected. Exiting.")
        exit()
    i += 1

matrix = []

#matrix swap rows operation
def swap(row1, row2):
    sourceCopy = matrix[row1][:]
    matrix[row1] = matrix[row2][:]
    matrix[row2] = sourceCopy

#matrix scale rows operation
def scale(targetRow, scalar):
    for i in range(len(matrix[targetRow])):
        if(matrix[targetRow][i] != 0):
            matrix[targetRow][i] *= scalar
            if(roundAllTo != -1):
                matrix[targetRow][i] = round(matrix[targetRow][i], roundAllTo)


#matrix subtraction (only sub because goal is to create zeros in matrix indices)
def subtract(sourceRow, sourceScalar, otherRow, otherScalar):
    for i in range(len(sourceRow)):
        sourceRow[i] = (sourceScalar * sourceRow[i]) - (otherScalar * otherRow[i])
        if(roundAllTo != -1):
            sourceRow[i] = round(sourceRow[i], roundAllTo)
       

userInput = input("Enter each entry in the matrix separated by a space, and each line of the matrix separated by a '/'\n")
currRow = []
ind = 0

while(ind < len(userInput)): #parse user input
    if(userInput[ind] == ' '): #space separates entries
        ind += 1
        continue
    elif(userInput[ind] == '/' and ind > 0 and userInput[ind-1] == ' '): #slash with space before signifies new row
        matrix.append(currRow[:])
        currRow.clear()
    else: #otherwise, interpret number
        leftInd = rightInd = ind
        typeFloat = False
        hasSlash = False
        slashInd = -1
        while(rightInd < len(userInput) and userInput[rightInd] != ' '):
            if(userInput[rightInd] == '.'):
                typeFloat = True
            elif(userInput[rightInd] == '/'):
                hasSlash = True
                slashInd = rightInd
            rightInd += 1
        ind = rightInd
        if(typeFloat): #convert to a float
            currRow.append(float(userInput[leftInd:rightInd+1]))
        elif(hasSlash): #divide left value by right value
            currRow.append(int(userInput[leftInd:slashInd])/int(userInput[slashInd+1:rightInd+1]))
        else: #regular decimal integer
            currRow.append(int(userInput[leftInd:rightInd+1]))
    ind+=1
if(len(currRow) > 0): #if input ceases before a '/' is encountered, append current row
    matrix.append(currRow[:])
    currRow.clear()

#integrity check to confirm all rows are the same size
for i in range(len(matrix)):
    if len(matrix[i]) != len(matrix[0]):
        print("Inconsistent row length detected. Exiting")
        exit() 


if augment:
    colLimit = len(matrix[0]) - 1
else:
    colLimit = len(matrix[0])

row = col = 0
while(row < len(matrix) and col < colLimit):
    if(matrix[row][col] == 0): #find a row with a pivot in the desired column
        rowTemp = row + 1
        while rowTemp < len(matrix) and matrix[rowTemp][col] == 0:
            rowTemp += 1
        if rowTemp < len(matrix): #swap matrix[row] with desired pivot row matrix[rowTemp]
            swap(row, rowTemp)
            if showSteps:
                print(f"step {stepNumber}: R{row+1} <-> R{rowTemp+1}")
                stepNumber += 1
                for p in matrix:
                    print(p)
                print("\n")
    if matrix[row][col] != 0: # if == 0, desired pivot column was not found
        if matrix[row][col] != 1.0: # if because no need to scale if pivot already 1
            if showSteps:
                print(f"step {stepNumber}: R{row+1} -> {1/matrix[row][col]}R{row+1}")
                stepNumber += 1
            scale(row, 1/matrix[row][col])
            if showSteps:
                for p in matrix:
                    print(p)
                print("\n")
        for i in range(len(matrix)): 
            if i != row: #row subtract all rows besides itself from current pivot row
                if showSteps:
                    print(f"step {stepNumber}: R{i+1} -> 1R{i+1} - {matrix[i][col]}R{row+1}")
                    stepNumber += 1
                subtract(matrix[i], 1, matrix[row], matrix[i][col])
                if showSteps:
                    for p in matrix:
                        print(p)
                    print("\n")
        row += 1
        col += 1
    else:#if desired pivot not found, increment the row but maintain the column
        col += 1    

if augment == True: #check for zero rows with augmented values. If discovered, inconsistent
    for row in reversed(matrix):
        if(row[len(row)-1] != 0):
            for col in range(0, len(row)-1):
                if(row[col] != 0):
                    print(row[col])
                    break
            else: #else statement when for loop exhausts. Break ceases inner for and iterates outer.
                print(row)
                print("The matrix is inconsistent. Thus, no RREF form.")
                exit()

print("RREF matrix:")   
if(roundOutputTo != -1):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = round(matrix[i][j], roundOutputTo)
        print(matrix[i])
else:
    for i in matrix:
        print(i)

