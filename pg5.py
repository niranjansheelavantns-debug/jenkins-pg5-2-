import sys
if len(sys.argv)==4:
    script_name=sys.argv[0]
    principal=sys.argv[1]
    rate=sys.argv[2]
    time=sys.argv[3]
else:
    principal=1000.0
    rate=5.0
    time=10
simple_interest=(principal*rate*time)/100
print("principal amount is:",principal)
print("Rate of interest is:",rate)
print("Time period is:",time)
print("Simple interest is:",simple_interest)