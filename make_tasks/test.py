# Alice:82,Bob:91,carol:74,dan:91,ellen:59

names = "Alice:82,Bob:91,carol:74,dan:91,ellen:59"
listed = names.title().split(",")
string = ":".join(listed)
adv_Listed = string.split(":")
length = len(listed)
# print(adv_Listed)


print(f"Valid Students: {length}" )


# The Students

first = adv_Listed[0]
second =adv_Listed[2] 
third = adv_Listed[4]
fourth =adv_Listed[6]
fifth = adv_Listed[8]



# The Grades

f = int(adv_Listed[1])
s = int(adv_Listed[3])
th = int(adv_Listed[5])
fo = int(adv_Listed[7])
fi = int(adv_Listed[9])

gr_list = [ f , s , th , fo , fi ]
gr_list.sort()

# Average Score

A_Score = (f+s+th+fo+fi)/length
print(f"Average Score: {A_Score:.2f}")

# Top score

print(f"Top Score: {gr_list[-1]} -> {second} , {fourth}")

# Failing

print(f"Failing: {fifth}")


# Last Thing

pass_st = [ first , second , third , fourth]

with open("passing.txt", "w") as f:
        f.write(str(pass_st))
