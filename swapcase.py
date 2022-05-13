# First Method By Function
def swap_case(s):
    y = ''
    for x in t:
        if x.isalpha():
            y+=x.swapcase()
        else:
            y+=x
    return y

# Second Method 
z = ""
t = "zOhAib"
for x in t:
    if x.isupper() :
       z+= x.lower()
    else:
        z+=x.upper()
print(z)
    
# One liner
print("".join([i.lower() if i.isupper() else i.upper() for i in input()]))

