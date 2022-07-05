# Description 
This script calculate mean values and standart deviation for each sample and condition
Then it calculate the difference to the control condition for each sample
and plot the results

## Required:
1. python3
2. python pacakes: numpy, mathplotlib, pandas

# input 
The first argument to run the script is the file location\name
the second argument is the control condition name
the rest of the argument are all the other conditions

# NOTE: 
It's important to keep the notation of condition the same as in the "Target name" column

## Example:
for example I added the file called example_table.csv 
you can run the following command in the terminal: 
 
```bash
python graph_deltaCT.py example_table.csv "un-cut (C)" "diluted 1:2 (D)" "cut (M)"
```

format:
python graph_deltaCT.py "file path" "control condition" ,,, "other conditions"

## output:  
for each sample (collected by "sample Name" column) 
the script ouput a graph with a difference value for each condition to control condition
