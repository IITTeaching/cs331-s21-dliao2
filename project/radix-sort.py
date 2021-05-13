import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    word_list = book_to_words(book_url) 
    max_length = 0 
    for word in word_list: 
        if len(word) > max_length: 
            max_length = len(word) 
    sorted = count_sort(word_list, max_length + 1)
    for i in range(max_length, -1, -1): 
        sorted = count_sort(sorted, i) 
    return sorted 

def count_sort(lst, pos): 
    count = [0 for _ in range(127)] 
    sorted = [None for _ in range(len(lst))] 
    for i in lst:
        if len(i) - 1 < pos:
            n = 0
        else:
            n = ord(i.decode('ascii')[pos])
        count[n] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(lst) - 1, -1, -1):
        if len(lst[i]) - 1 < pos:
            n= 0
        else:
            n = ord(lst[i].decode('ascii')[pos])
        sorted[count[n] - 1] = lst[i]
        count[n] += -1
    return sorted  
