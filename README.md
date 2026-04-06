# Programming-Assignment-3

### Kevin Jin, 24470226
### Keerat Kohli, 41823869

To run our code, run from main.py in the src folder.

Upon running, user will be prompted to run either "custom" or "standard" tests. Please type the desired mode exactly as it appears to select. 

Standard tests are ten nontrivial input files that have been used to answer Question 1 stored in the tests folder. These tests contain strings with lengths of increasing multiples of 25. The size of the alphabet in all tests is 10. The result will be returned in the corresponding output files in the tests folder.

To run user-defined tests, select custom mode and create an input.in file in the data folder with the correct format. The result will be returned in an output.out file in the data folder. The results will also be printed. An example input.in and output.out file has already been provided.

Both modes assume that the file input is in the following format:

K

x_1 v_1

x_2 v_2

...

x_K v_K

A

B

Where K is the number of characters in the alphabet. The next K lines contain character-value pairs for the scores of each character. A is the first string and B is the second string.

The output gives the maximum value of a common subsequence along with the subsequence that generated that score.

## Question 1

The graph for the runtime of tests of varying input sizes is displayed below.

![Runtime](data/runtime_graph.png)

We can see from the graph that there is a clear quadratic trend, where an increase in input size by 25 causes the runtime to be much slower when the input size is already 200 as opposed to when it is only 25. Since in our test cases the lengths of A and B are the same, we will see that the runtime being quadratic O(n^2) aligns with our theoretical results.
