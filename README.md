# DSAD-assignment-2

## Problem Statement:
An aspiring chef Sam is learning to prepare a dish that needs just two ingredients salt(S) and pepper(P). As per the instructions given to him, in order to make a balanced dish, he must use equal quantities of salt and pepper. In the pantry the salt and pepper packets are placed in a random sequence. Sam’s job is to try and make as many balanced dishes as he can. But there is a rule in the kitchen that he can only use chunks of ingredients that are placed together. Can you help Sam figure out the maximum number of balanced dishes he can make using all the salt and pepper packets in the pantry? You can assume that the pantry always has an equal quantity of salt and pepper packets. Which means that Sam can make at least one balanced dish using all the salt and pepper in the pantry.

### For Example:
- If the salt (S) and pepper (P) packets in the pantry are in the sequence SPSSPP. Sam can make a maximum of 2 good dishes: SP | SSPP (remember good dishes have an equal amount of salt and pepper)
- If the salt (S) and pepper (P) packets in the pantry are in the sequence SPPPPSSSPS. Sam can make a maximum of 3 good dishes: SP | PPPSSS | PS (remember he can only use ingredients that are adjacent)
- If the salt (S) and pepper (P) packets in the pantry are in the sequence SPSSSPPSPP:. Sam can make a maximum of 2 good dishes: SP | SSSPPSPP (remember you have to use all the ingredients)
- If the salt (S) and pepper (P) packets in the pantry are in the sequence SSSSPPPP: Sam can make a maximum of 1 good dish: SSSSPPPP

### Requirements:
- Formulate an efficient algorithm using Greedy Method to perform the above task.
- Provide a description about the design strategy used
- Analyse the time complexity of the algorithm and show that it is an “efficient” one.
- Implement the above problem statement using Python 3.7

#### Sample Input:
Input will be taken from the file(inputPS6.txt) here each line represents the pantry.

SPSSPP

SPPPPSSSPS

SPSSSPPSPP

SSSSPPPP

Note that the input/output data shown here is only for understanding and testing, the actual file used for evaluation will be different.

#### Sample Output:
For every line in the input find the maximum number of good dishes and write it in the output file.

2

3

2

1

Note that the input/output data shown here is only for understanding and testing, the actual file used for evaluation will be different.
Display the output in outputPS6.txt.

## Deliverables
- Word document designPS6_<group id>.docx detailing your design and time complexity of the algorithm.
- [Group id]_Contribution.xlsx mentioning the contribution of each student in terms of percentage of work done. Download the Contribution.xlsx template from the link shared in the Assignment Announcement.
- inputPS6.txt file used for testing
- outputPS6.txt file generated while testing
- .py file containing the python code. Create a single *.py file for code. Do not fragment your code into multiple files
Zip all of the above files including the design document and contribution file in a folder with the name:
[Group id]_A2_PS6_RestaurantIngredients.zip and submit the zipped file.
Group Id should be given as Gxxx where xxx is your group number. For example, if your group is 26, then you will enter G026 as your group id.
