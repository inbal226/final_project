lst = [1, 2, 3]
file1 = open("test_result.txt", "w")

file1.writelines(str(lst))
file1.close()

file1 = open("test_result.txt", 'r')
print(file1.read())
file1.close()


