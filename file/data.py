number = [90,80,70,50]

total = sum(number)
length = len(number)

print(f"total : {total} & banyak data : {length}")

def rata_rata(total, length):
    return total / length   

rata = rata_rata(total, length)
print(f"rata rata nya yaitu {rata}")