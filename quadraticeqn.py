import math
a=int(input("Enter value for a: "))
b=int(input("Enter value for b: "))
c=int(input("Enter value for c: "))
d=(b**2)-(4*a*c)
if a==0:
    print("a can't be zero")
elif d < 0:
    print("roots cannot be complex")
else:

    sqr_rt1=(-b-math.sqrt(d))/(2*a)
    sqr_rt2=(-b+math.sqrt(d))/(2 * a)
    print("The square_roots are {} and {}:".format(sqr_rt1,sqr_rt2))