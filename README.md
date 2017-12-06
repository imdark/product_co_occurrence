Super-market frequent item sets
===============================

HOW TO USE
----------

1. clone from git
`git clone https://github.com/imdark/product_co_occurrence.git`
1. cd into the folder you cloned it in
`cd product_co_occurrence`
1. make a virtual env with python 3.5 and run it (might change slightly depending on your local setup)
```
virtualenv -p python3 envname
source activate
```
1. prepare an input file in the format "<sku 1 id >, <sku 2 id>, …. <sku N id>" called "retail_25k.dat" and make sure
 there no file called "out.dat"
1. run code 'main.py -i retail_25k.dat  -o out.dat'
1. the results will be written to out.dat in the format <item set size (N)>, <co-occurrence frequency>, <item 1 id >, <item 2 id>, …. <item N id>

Considurations and next steps
----
The original question I had in mind was, what algorithem to use:
	1. apriori
	1. Eclat algorithm
	1. FP-growth algorithm

	Currently given some experiments FP-growth algorithm seems to run the fastest given the data I tested it with and in general is considered 
	Best of Breed in term of memory performance and time

things still left to do
1. verify input file, in currect format 
1. profile and impove performance, I believe it could run much faster
1. fp_tree pruning
1. see if there is a more efficent way to make the set size limit work


Steps to make FP-growth work:
-----------------------------
1. ~make sure it generates all permutations~ looks like working fine
1. ~add frquencies~
1. ~add conditions for frequencies~
1. ~add limit on set size~

To run unit tests
----------------
```python -m unittest```

To test perfomance
------------------
*. To run profiling:
```python -m cProfile main.py -i retail_25k.dat > out.profile```

*. it currently takes about ~4.5~ 3 minutes to process the big retail_25k.dat, does not seem reasonable

*. current slow downs:
```
   299024   27.095    0.000   32.429    0.000 fp_growth.py:25(get_conditional_ (might be solvable using set() union set() for suffix)
   2387221    8.595    0.000   14.855    0.000 fp_tree.py:12(__init__)
   3437740   66.066    0.000  124.169    0.000 fp_tree.py:16(add)
   23903711   64.363    0.000   64.363    0.000 fp_tree.py:4(__init__)
   28293302    4.574    0.000    4.574    0.000 {method 'append' of 'list' objec (can be solved with using static arrays with sizes)
```
References
----------
Han (2000). "Mining Frequent Patterns Without Candidate Generation". Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data. SIGMOD '00: 1–12
https://dl.acm.org/citation.cfm?doid=342009.335372

Comparing Dataset Characteristics that Favor the, Apriori, Eclat or FP-Growth Frequent Itemset, Mining Algorithms
https://arxiv.org/pdf/1701.09042.pdf

The FP-Growth Algorithm variaty of oprimiztion
https://en.wikibooks.org/wiki/Data_Mining_Algorithms_In_R/Frequent_Pattern_Mining/The_FP-Growth_Algorithm

Contains a very good visualiztion of building and usefulness of an FP tree
Apriori and Eclat algorithm in Association Rule Mining
https://www.slideshare.net/wanaezwani/apriori-and-eclat-algorithm-in-association-rule-mining