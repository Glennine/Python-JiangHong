a = float(input("请输入三角形的边a："))
b = float(input("请输入三角形的边b："))
c = float(input("请输入三角形的边c："))
if (a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a):
    #print("三角形三边：a=",a,",b=",b,",c=",c)
    if (a == b and b == c):print("该三角形为等边三角形！")
    elif (a==b or b==c or a==c):print("该三角形为等腰三角形！")
    elif (a*a+b*b == c*c or a*a+c*c == b*b or c*c+b*b == a*a):print("该三角形为直角三角形！")
    else:print("该三角形为其他三角形！")
else:print("无法构成三角形！")
