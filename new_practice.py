# find surname and firstname based name 
'''ls = ["pushpendra maurya", 'suraj yadav',"ritesh sharma","cuman cnshari","gaurab ghosh", "sidhi navghare"]

ls.sort(key = lambda x:x.split() [-1])
print(ls)
'''


# count name of string 
'''a = 'i am pushpendra maruay from thane'

countt_a  = 0
countt_e = 0
for i in a:
    if i == "a":
        countt_a +=1

    elif i =="e":
        countt_e  +=1
print(countt_a, countt_e)
'''

# count no of vowels is there in string 
## vowels

'''str = "i am the king of bollywood you lisen to me"
count = 0
for i in str:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
print(count)'''

# count string is there 
'''str = "i am the king of bollywood you lisen to me"
count = 0
for i in str:
    count = count+1
print(count)'''

# find factorial 
'''n = 5 

fact = 1
for i in range(n,0,-1):
    fact = fact*i
print(fact)''' 

'''a = "pushpendra"
count = 0
count = 1
while count < len(a):
    count = count +1
    # i = i+1
    print(count)'''



# total sum of list 
ls = [1,2,34,4,66]
'''sum = 0 
for i in ls:
    sum = sum+i 
print(sum)'''

'''
count = 0 
for i in ls:
    count = count +1

print(count)'''

# find greated no in list 
'''ls = [1,2,3,4,6,7,8,9,9,90]

a = 0
for i in ls:
    if i>a:
        a = i
print(a)'''

# store positive and negative no in the list 

'''a = [-1,-2,-3,-5,-6,1,2,3,4,5,6,7,8,82]
pos = []
neg = []
for i in a:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)

print(f"this is positve no{pos}  and this is negative {neg} ")
'''

# add two list in a single list 

'''a = [1,2,3,4,5]
b= [2345,2345,2452,45234,5,132132,1234123,41234,2341]

ls = [ i+j for i,j in zip(a,b)]
print(ls)'''


a = "pushpendra"
b = "ardnephsup"
if len(a) != len(b):
    print("not anagram")
else:
    if sorted(a) == sorted(b):
        print("string are anagrams")

    else:
        print("string are not anagrams")
