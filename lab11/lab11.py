from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if high > low:
        pivot = pivot_fn(lst, low, high)
        i = low - 1
        j = high + 1
        while j > i:
            i += 1  
            while True: 
                if (lst[i] < pivot) and (not i > high):
                    i += 1 
                else: 
                    break
            j -= 1 
            while True: 
                if (lst[j] > pivot) and (not j < 1): 
                    j -= 1
                else: 
                    break
            if i < j:
                lst[i], lst[j] = lst[j], lst[i]
        qsort(lst, low, j, pivot_fn)
        qsort(lst, j + 1, high, pivot_fn)
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    return lst[low]
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    return lst[random.randrange(low,high)]
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    return lst[(low + high) // 2]
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
