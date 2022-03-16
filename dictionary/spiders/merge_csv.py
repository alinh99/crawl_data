# import pandas as pd

# a = pd.read_csv("../words.csv")
# b = pd.read_csv("../definitions.csv")
# b = b.dropna(axis=1)
# merged = a.merge(b)
# merged.to_csv("output.csv", index=False)

def check_duplicate_list(mylist):
    if len(mylist) != len(set(mylist)):
        return "Tồn tại phần tử trùng lặp trong list"
    else:
        return "Không có phần tử trùng lặp trong list"    

# l = [0, 1, 2]
# print(check_duplicate_list(l))
##> Không có phần tử trùng lặp trong list

l = ['a', 'b', 'c', 'a']
print(check_duplicate_list(l))