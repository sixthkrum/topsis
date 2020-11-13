Apply TOPSIS to a dataset in csv format.

<h1> Usage: </h1>

<h3> For use in code: </h3>

from topsis import csvTopsis

<h3> From the command line: </h3>

csvTopsis <//filename> <//weights> <//impacts> {options: delimiter(,)}

    filename is the name of the csv file which has the dataset
        
        The dataset must have a minimum of three columns and all the parameter columns must have numeric values. The first row is assumed to contain the column names and the first column is assumed to contain the row names
    
    weights is a comma seperated list of weights ex: 1.0,1,1,1
        
        weights must be numeric and the number of weights equal to number of parameter in the dataset
    
    impacts is a comma seperated list of impacts ex: +,+,+,+
        
        impacts must be either - or + and the number of impacts must be equal to number of parameters in the dataset
    
    delimiter is the delimiter to be used to read the csv file
        
        default ','


Sample output:

    scores [0.5633920465033206, 0.3929781508166451, 0.8668523706767487, 0.14869542262467947, 0.5693097043728271]

    ranks [3, 4, 1, 5, 2]


<h1> Functions: </h1>

csvTopsis.topsis(inputCSV, weights, impacts, delimiter = ',')

    arguments:

        inputCSV is a stream containing the dataset, it must have at least 3 columns and the parameter columns must have only numeric values. The first column is assumed to contain column names and the first row is assumed to contain row names
        
        weights is a list with weights for the parameters in the dataset. The list must be numeric and have a size equal to the number of parameters in the dataset
        
        impacts is a list with impacts for the parameters in the dataset. The list must have only '-' or '+' as values and the size must be equal to number of parameters in the dataset
        
        delimiter is the delimiter to be used to read the inputCSV file object (default: ',')

    returns:

        resultCSV is a stream which contains the original dataset with 2 added columns namely 'Topsis Score' and 'Rank' the former contains the topsis score for the rows and the latter the topsis ranks
        
        similarityList is a list containing the topsis scores of all the rows
        
        rankList is a list containing the topsis ranks