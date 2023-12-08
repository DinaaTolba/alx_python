output = ""
for i in range(99):
    output += "{:d} = 0x{:x}\n".format(i, i)

print(output, end="")
