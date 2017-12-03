Referencing algorithems
-----------------------

HOW TO USE
----------

1. clone from git
`git clone `
2. make a virtual env with python 3.3
3. run code 'main.py -i retail_25k.dat  -o out.dat'
4. the results will be written to out.dat

TODO
----
a. what algorithem to use:
	1. apriori
	2. Eclat algorithm
	3. FP-growth algorithm

	currently given some experiments FP-growth algorithm seems to run the fastest given the data I tested it with given
b. pydocs
c. python 3 types
d. clean up
e. fp_tree pruning
f. unit tests


References
----------
Han (2000). "Mining Frequent Patterns Without Candidate Generation". Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data. SIGMOD '00: 1–12
https://dl.acm.org/citation.cfm?doid=342009.335372

Comparing Dataset Characteristics that Favor the, Apriori, Eclat or FP-Growth Frequent Itemset, Mining Algorithms
https://arxiv.org/pdf/1701.09042.pdf