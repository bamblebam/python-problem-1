num=input("enter num ")
num_list=[int(x) for x in str(num)]

for j in range(0,len(num_list)-2):
  counter=10
  for i in range(0,len(num_list)):
   if counter>num_list[i]:
     counter=num_list[i]
  num_list.remove(counter)
for i in num_list:
  print(i,end="")


