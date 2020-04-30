def fibbonacci (number):
    fibb_seq=[]
    for n in range (number+1):
        if n==0:
            fibb_seq.append(n)
            continue
        elif n ==1:
            fibb_seq.append(1)
            continue
        else:
            next_num = fibb_seq[n-2] + fibb_seq[n-1]
            fibb_seq.append(next_num)
    for l in fibb_seq:
        print (l)
        
number= int(input("Enter any interger: "))
fibbonacci (number)