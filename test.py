my_val = "2,4"
val_list = []
if "," in my_val:
    print("yes")
    for char in my_val:
        val_list.append(char)
    for i in range(len(val_list)-1):
        if val_list[i] == ",":
            val_list[i] = "."
    print(val_list)
    my_val = "".join(map(str, val_list))
    print(my_val)