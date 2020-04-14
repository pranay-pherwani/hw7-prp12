"""
hw7.py
Name(s):
NetId(s):
Date:
"""

"""
merge: the helper function for MergeSort that merges two sorted lists.
"""
def merge(L1, L2):
	L = []
	while len(L1)>0 and len(L2)>0:
		if L1[0]<L2[0]:
			L.append(L1[0])
			del L1[0]
		else:
			L.append(L2[0])
			del L2[0]
	if len(L1)>len(L2):
		L = L + L1
	else:
		L = L + L2
	return L

"""
MergeSort
"""
def MergeSort(L):
	if len(L)==2:
		if L[1]<L[0]:
			temp = L[1]
			L[1] = L[0]
			L[0] = temp
	elif len(L)>2:
		mid = len(L)//2
		left = L[:mid]
		right = L[mid:]
		L = merge(MergeSort(left), MergeSort(right))
	return L

"""
partition: the helper function for QuickSort that partitions the input
		   list L based on the value of the pivot at L[p].
"""
def partition(L, p):
	return (newL, i)

"""
QuickSort
"""
def QuickSort(L):
	return L

"""
main
"""
if __name__ == '__main__':
	A = [1,5,6,2,3,9,8,7,4,10]
	print(MergeSort(A))

