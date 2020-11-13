import os
import sys
import csv

from topsis import csvTopsis

def main():
    if len(sys.argv) not in [4, 5] :
        print("please enter the arguments and only the arguments:")
        print("<filename> <weights> <impacts> <delimeter = ','>")
        exit()

    fileName = sys.argv[1]

    if not os.path.isfile('./' + fileName):
        print("please put file in same directory as the script")
        print(fileName + " does not exist")
        exit()

    f = open(fileName, 'r')

    if len(sys.argv) == 4:
        delimiter = ','
    
    else:
        delimiter = sys.argv[4]

    weights = []

    for i in sys.argv[2].split(','):
        try:
            weights.append(float(i))
        except:
            print("weights must be numeric values only")
            exit()

    impacts = []

    for i in sys.argv[3].split(','):
        if i not in ['-', '+']:
            print("impacts must be either '+' or '-' only")
            exit()    
        else:
            impacts.append(i)

    results = csvTopsis.topsis(f, weights, impacts, delimiter)
    print("scores", results[1])
    print('\n')
    print("ranks", results[2])

if __name__ == "__main__":
    main()
    