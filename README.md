# Implementing OpenMP in Conway's Game of Life
- https://github.com/saboj1999/Conways-Game-of-Life-with-OpenMP.git

1. Compile 'hw2.c' with the following command: "gcc -fopenmp hw2.c -o hw2.o"
2. Run the 'test' script inside of the 'Tests' folder with: "./test"
- This will compile and run the sequential and parallel versions of the script and test to make sure they have identical outputs for a series of parameters.
3. Run the time performance script with: "./runTimePerformance"
- This will run the command "./hw2.o 500 500 5000 x" with x as 1,2,4,8,10,16, and 20 threads. It will generate average times for 5 runs of each threadcount and populate the file 'time_average_outputs.txt'.
4. Run the size performance script with: "./runSizePerformance"
- This will run the command "./hw2.o z y 5000 x" with z and y and the (x,y) sizes of the grid as (1,16),(2,8),(4,4),(8,2), and(16,1). Just as in step 3, x will represent the thread counts. It will generate average times for 100 runs of each threadcount and grid size and populate the file 'size_average_outputs.txt'.
5. Run the graphing script for time performance with: "python3 graphTimePerformance.py"
- This will generate 1 graph of time versus threadcount for 500x500 grid, 5000 generations.
6. Run the graphing script for size performance with: "python3 graphSizePerformance.py"
- This will generate 5 graphs, one for each grid size specified of time versus threadcount.
