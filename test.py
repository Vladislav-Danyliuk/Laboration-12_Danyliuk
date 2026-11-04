my_list = ["a" , "b" , "c" , "d"]
temp = my_list[0]
my_list[0]=my_list[2]
my_list[2] = temp

print(temp)