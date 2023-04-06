
#Program to convert roman numerals into decimal numbers

d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

x=input("Enter the Roman Number:").upper()
num=0
l=[]

def convert(num,d,x,l):
    for i in range(0,len(x)):
        if x[i] not in d.keys():
            print("Invalid roman num")
            return "error"
        
    for i in range(0,len(x)):
        l.append(d[x[i]])
        
    for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
            l[i]=-(l[i])
            #logic 1<5 so negate 1 so that it will be subtracted ,xiv=[10,-1,5], sum of the list =14
                     
    for i in range(0,len(l)):
            num+=l[i]

    return num

print('The numeric value of ',x,' is ',convert(num,d,x,l))

    
        
    
     
        

            

