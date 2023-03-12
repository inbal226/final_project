

file1 = open("test_result.txt", "w")
lst= [1,2,3]

file1.writelines(str(lst))
file1.close()

file1 = open("test_result.txt", 'r')
print(file1.read())
file1.close()

file1 = open("test_result.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()