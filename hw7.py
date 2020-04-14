"""
hw7.py
Name(s): Pranay Pherwani
NetId(s): prp12
Date: 4/14/20
"""

"""
merge: the helper function for MergeSort that merges two sorted lists.
"""
def merge(L1, L2):
	# Initialize final list
	L = []
	# Append the lower value of the first value of each list
	# and delete it until one of the lists runs out of elements
	while len(L1)>0 and len(L2)>0:
		if L1[0]<L2[0]:
			L.append(L1[0])
			del L1[0]
		else:
			L.append(L2[0])
			del L2[0]
	# Determine the list with remaining elements and append it to the final list
	if len(L1)>len(L2):
		L = L + L1
	else:
		L = L + L2
	return L

"""
MergeSort
"""
def MergeSort(L):
	# If the length is 2, swap the values if not in order
	if len(L)==2:
		if L[1]<L[0]:
			temp = L[1]
			L[1] = L[0]
			L[0] = temp
	# Recursively call MergeSort on the left half and right half of the list and merge them
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
	# Initialize the new list
	newL = [0]*len(L)
	# Initialize the starting indices
	i = 0
	j = len(L)-1
	# Place smaller elements before the pivot and larger elements after
	for k in L:
		if k<L[p]:
			newL[i] = k
			i+=1
		else:
			newL[j]=k
			j-=1

	return (newL, i)

"""
QuickSort
"""
def QuickSort(L):
	# Recursively call QuickSort on both parts of the partitioned set
	# and add it to the list with the pivot
	if len(L)>1:
		(newL, pIndex) = partition(L,-1)
		L = QuickSort(newL[:pIndex])+[newL[pIndex]]+QuickSort(newL[pIndex+1:])
	return L

"""
main
"""
if __name__ == '__main__':
	A = [1,5,6.3,2,3,9.001,8,7.8,4,10]
	B = [-1,5,-6,2,3,-9,8,7,4,10]
	C = [1,5,5,5,5,5,5,4,4,6]
	print(QuickSort(A))
	print(QuickSort(B))
	print(QuickSort(C))

	print(MergeSort(A))
	print(MergeSort(B))
	print(MergeSort(C))

