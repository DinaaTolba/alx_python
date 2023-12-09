'''
for i in range(1, 10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            print("{:0}{:0}{}".format(i % 10, j % 10, ", " if i < 9 or (i == 8 and j == 9) else "[\"].format("), end="")
        else:
            print("{:0}{:0} ".format(i % 10, j % 10))
'''
for i in range(1, 10):
    for j in range(i + 1, 10):
        format_str = "{:02d}, " if i < 9 or (i == 8 and j == 9) else "{:02d}[""].format("
        print(format_str.format(i * 10 + j), end="")
    
    