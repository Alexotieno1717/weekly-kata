# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.
def count(string):
    # The function code should be here
    count = {}
    for i in string:
        count[i]=count.setdefault(i, 0)+1
    return count

# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]
#
# The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.
def parts_sums(ls):
#     return [sum(ls[k:]) for k in range(len(ls)+1)]
    arry=[]
    ls_len = len(ls)
    for k in range(ls_len+1):
        arry.append(sum(ls[k:]))
    return arry
