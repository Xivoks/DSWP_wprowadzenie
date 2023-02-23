numbers_int=[1,2,3,4,5,6,7,8,111,1223,5434,6324352]
print("\nhow many bits does the number have?\n")
for x in numbers_int:
    print(x , " => " , x.bit_count())

numbers_float=[1.0,2.0,3.0,4.0,5.0,5.55,6.66,765.3,22.0,65.0]

print("\nIs the number a integer?\n")
for x in numbers_float:
    print(x , " => " , x.is_integer())
