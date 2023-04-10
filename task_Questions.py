
# cubes of odd digit using comprehension:

# ls = [1,2,3,4,5,6,7,8,9]

# ls1 = [ i**3 for i in ls if i%2!=0]
# print(ls1)


## program to find greatest no. of two integer

# a = int(input("enter no : "))
# b = int(input("enter no : "))
# if a>b :
#     print(a," is greater")
# else:
#     print(b,"is greater")


## count data with using count function

'''a = "i am the king of bollywood you lisen to me"

count_o = 0

for i in a:
    if i == "o":
        count_o += 1
    
print(count_o)

'''


## vowels

# str = "i am the king of bollywood you lisen to me"

# for i in str:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         print(i,"is vowels")



## Factorial

# n = int(input("Enter No :"))

# fact = 1
# for i in range(n,0,-1):
#     fact = fact*i

#     print(fact)


## stars 

# n = 5

# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == 0 or row == 4 or col == 4:
#             print("*" , end = " ")
#         else:
#             print(" " , end = " ")

#     print()


# n = 5 

# for row in range(n):
#     for col in range(n):
#         if row == 4 or col == 0 or row == col:
#             print("*" ,end = " ")
#         else:
#             print(" ",end = " ")

#     print() 



## Iteration using loop


# st = "suraj"

## using for loop
# for i in st:
#     print(i) 



## using while loop
# i = 0
# while i < len(st):
#     print(st[i])
#     i +=1


# count word in string

# st = "hello suraj this is a python lecture"

# count = 0

# for i in st.split(" "):
#     # print(i , end = "\t")
#     count +=1

# print(count)



# ### program to sum of list

# ls = [2,4,6,8]

# sum = 0

# for i in ls:
#     sum = sum+i
#     total = sum/len(ls)

# print(total)


# find greatest no. in list

# ls = [10,30,50,20,40]

# b_n = ls[0]


# for i in ls:
#     if i>b_n:
#         b_n = i
# print(b_n)

#using function

# ls = [10,20,50,30,40]

# def greatest(x):
#     big_no = x[0]
#     for i in x:
#         if i>big_no:
#             big_no = i
    
#     return big_no

# x = greatest(ls)
# print(x)




### 

# ls = [-1,2,-4,-5,6,5,9,-8]

# pls = []
# nls = []
# for i in ls:
#     if i<0:
#         nls.append(i)

#     else:
#         pls.append(i)

# # print(pls , nls)
# c = []

# c.extend(pls)
# c.extend(nls)

# print(c)

# st = "suraj"

# i = 0
# while i<len(st):
#     print(st[i])
#     i +=1

# ls = [-1,3,-4,5,-6,7,8,-9,10]


# n = []
# p = []
# for i in ls:
#     if i>0:
#         p.append(i)
#     else:
#         n.append(i)

# arrange = []

# arrange.extend(n)
# arrange.extend(p)

# print(arrange)


#add two list

# ls1 = [1,2,3,4]
# ls2 = [1,2,3,4]

# ls3 = [ i+j for i,j in zip(ls1,ls2)]
# print(ls3)

# add tuple

# ls1 = (1,2,3,4)
# ls2 = (1,2,3,4)

# ls3 = [ i+j for i,j in zip(ls1,ls2)]
# print(ls3)

# for i in ls3:
#     print(i)


# # anagram
# while True:
#     st1 = input("Enter String1 :")
#     st2 = input("Enter String2 :")

    # print(sorted(st1))
    # print(sorted(st2))

#     if len(st1) != len(st2):
#         print("not anagram")

#     else:
#         if sorted(st1) == sorted(st2):
#             print("String are anagrams")

#         else:
#             print("String are not anagrams")


## remove dupllicate element from list

# ls = [1,2,3,4,5,3,4,5]

# ls1 = []

# for i in ls:
#     if i not in ls1:
#         ls1.append(i)
# print(ls1)


## 

# ls = [1,2,3,4,5]

# for i in ls:
#     if i == 3 or i == 4:
#         continue
#     print(i)


# ls= [1,2,3,4,5,6]

# cube = []

# for i in ls:
#     if i%2 != 0:
#         i = i**3
#         cube.append(i)

# print(cube)



##
# def string_data(data):

#     small = "abcdefghijklmnopqrstuvwxyz"
#     capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     split_d = data.split()
#     # print(split_d)

#     new_st = []
#     for i in split_d:
#         pos = small.index(i[0])
#         # print(pos)

#         i = capital[pos]+i[1:]
#         new_st.append(i)
#         new_st = "".join(new_st)

#         return new_st



# x = string_data("india is my country")
# print(x)

# def string_data(data):

#     small = "abcdefghijklmnopqrstuvwxyz"
#     capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     new_st = [capital[small.index(i[0])]+i[1:] for i in data.split()]

#     return " ".join(new_st)


# x = string_data("india is my country")
# print(x)





##

# generate an infinite fibonacci series by using generator

# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
    
# f1 = fibonacci()

# x = list(f1)
# print(x)

## sort a list with out using sort method

# ls = [2,1,4,53,6,8,7]

# n = len(ls)

# for i in range(n):
#     for j in range(i+1 , n):
#         if ls[i]>ls[j]:
#           ls[i],ls[j] = ls[j],ls[i]

# print(ls)



## task 

# st = "1,2,3,4,5"

# a  = st.split(",")

# m = [int(i) for i in a]

# d = {}

# for i in m:
#     d[i] = i**2

# print(d)



## task-1

# a = [1,2,3,4,5,6]  
# b = ["a" , "b" , "c" , "d" , "e" , "f"]

# z = zip(a,b)
# d = {}
# for i,j in z:
#     d[i] = j 
# print(d)   

# another way(using comprehension)

# d = { i:j for i,j in zip(a,b)}
# print(d)

## task-2

# a = "python is easy"
# x = a.split()
# print(x)



##############
#way1

# a = ["python" , "is" , "easy"]

# x = len(a[0])
# y = len(a[1])
# z = len(a[2])
# # print(x,y,z)
# b = x,y,z
# # print(s)

# d = {}

# z = zip(a,b)
# for i,j in z:
#     d[i]=j
# print(d)


#another way2

# a = ["python" , "is" , "easy" , "suraj" , "yadav"]

# x= []
# for i in a:
#     x.append(len(i))
# print(x)

# z = zip(a,x)
# d ={}
# for i,j in z:
#     d[i] = j

# print(d)

## way 3

# a = ["python" , "is" , "easy"]

# # b = []
# # for i in a:
# #     b.append(len(i))

# b = [ len(i) for i in a]

# d = { i:j for i,j in zip(a,b)}
# print(d)


#####################################################################################3

# a = ["python is easy"]

# for i in a:
#     a = i.split()

# length = [len(i) for i in a]
# # print(length)
# z = zip(a,length)
# d = { i:j for i,j in z}
# print(d)
    
##


#split a string without using split method
# s = "the way she look at me"

# l = []

# temp = ""

# for i in s:
#     if i == " ":
#         l.append(temp)
#         # print(temp)
#         temp = ""
#     else:
#         temp = temp+i
#         # print(temp2)

# l.append(temp)
# print(l)



## program to combine two different dictionary while combining, if you find the same keys , you can add the values of these same keys..output the new ditionary.

# d1 = {"a" : 10 , "b" : 20 , "c" :30 }
# d2 = {"d" : 40 , "a" : 20 , "c" :30 }

# for i in d1:
#     if i in d2:
#         d2[i] = d1[i]+d2[i]
#     else:
#         d2[i] = d1[i]

# print(d2)

## write a program for counting the number of every characetr of a given text file

# with open("Example1.txt" , "w") as f1:
#     data = input("Enter Data :")
#     x = f1.write(data)

# with open("Example1.txt" , "r") as f2:
#     x = f2.read()

# print(x)

# count = 0
# for i in x:
#     count += 1
# print(count)

## using while loop

# count = 0
# i = 0
# while i<len(x):
#     count += 1
#     i +=1

# print(count)

##


'''
# bottle = "water"

# if "water" in bottle:
#     print("yes ")

# else:
#     print("aymania bottle in watter")


cup = " "

var1  = "sugar"

var2 = "water"

var3 = "teapowder"

ready = var1,var2,var3 


if var1 and var2  in ready:
    # print("tea ready")
    if ready:
        print("tea is ready")

else:
    print("tea is not rady")




'''

# exam questions 


'''a = [1,2,3,4,5,6,7]
g = iter(a)
next(g)
for i in g:
    print(i)
    next(g)
    next(g)'''



# output 2 5 

'''x = 10 
y = 8
assert x>y 'X too small  '''

# output  assertion error


'''a = (1,2,4,3,8,9)
a1 = [a[i]  for i in range(0,len(a),2)]
print(a1)
'''
# output [1, 4, 8]

# set([[1,2],[3,4]])

'''set([1,2,2,3,4]) #correct'''

'''set((1,2,3,4)) # correct'''

'''{1,2,3,4}  # correct'''
# print(set)'''


'''test = {1:'a',2:'b',3:'c'}
test = {}
print(len(test))'''

#output 0

'''import math 
try:
    print(math.sqrt(81),end="")
except:
    print(0,end="")
finally:
    print(2,end="")'''

# output is 9.02
'''
s1 = {1,2,3}
s2 = {3,4,5,6}
s1.difference(s2)
s2.difference(s1)

print(s2)'''

# output #1,2 and 4,5,6

'''class demo(dict):
    def __test__(self,key):
        return []
a = demo()
a['test'] = 7
print(a)'''

# output  True

'''test = {1:"a",2:"b",3:"c"}
test = {}
print(len(test))'''

# output 0

'''a = [5,5,6,7,7,7]
b = set(a)
def test(lst):
    if lst in b:
        return 1
    
    else:
        return 0
for i in filter(test,a):
    print(i,end=" ")
'''

# output = 5 5 6 7 7 7 

'''
a,b,c = 1,2,3
a,b,c'''
# print(a,b,c)


'''a = (1:"a",2:"b",3:"c")
del a 
print(a)'''



'''my_tuple = (1,2,3,4,5)
my_tuple.append(5,6,7)
print len(my_tuple)'''

# output error 

'''test = {1:"a",2:"b",3:"c"}
test = {}
print(len(test))'''

# output 0

'''class demo(dict):
    def __test__(self,key):
        return []

a = demo()
a['test'] = 7
print(a)
'''
# output {'test': 7}


'''a = (1,2)
b = (3,4)
c = a+b

print(c)'''

# output (1, 2, 3, 4)

'''s1.issubset(s1)
if s1 = {1,2,3}

error outout '''

'''try:
    print(x)
except:
    print("an expeasdfasfg")


output = an expeasdfasfg'''

'''t = (1,2,3,4)
t[1:3]
print(t)'''

'''
count = {}
count[(1,2,4)] = 5
count[(4,2,1)] = 7
count[(1,2)] = 6
count[(4,2,1)] = 2
tot = 0
for i in count:
    tot = tot+count[i]
print(len(count) + tot)'''

# output 16

'''t = (1,2,4,8,9)
[t[i] for i in range(0,len(t),2)]

print(t)'''

# output   (1, 2, 4, 8, 9)

# a = dict()
# a[1]
# print(a)


# write the program to check water in bottle 