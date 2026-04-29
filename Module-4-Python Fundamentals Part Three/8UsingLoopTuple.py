tup = (1,2,3,4,5,6,7)

secondTuple= (1,2,3,4,2,3)

# koto number element a ase 
print(secondTuple.index(1))

# 3 word ta koto bar ase tuple a ta ber kora 
print(secondTuple.count(3))


# print 
# for val in tup:
#     print(val)

sum = 0 ; 

for val in tup:
    sum+=val 
print("Total is ", sum)