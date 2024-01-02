print("ok")

c = "abc"

# 将c的第2个字母改为d
c = c[:1] + "d" + c[2:]

print(c)

a = 2.2

if a > 0:
    print("a > 0")
else:
    if a == 0:
        print("a == 0")
    else:
        print("a < 0")
