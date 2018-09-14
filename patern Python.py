N,M=  map(int, input().split())

if(N>5 and N<101):
    if (N%2 != 0 and M == N*3):
        r=1
        n1 = N//2;
        for i in range(0,N):
            if(i<n1):
                str = ".|."*r
                print(str.center(M, '-'),end="\n")
                r=r+2
            if(i==n1):
                str1 = "WELCOME"
                print(str1.center(M,'-'))
            if(i>n1):
                r=r-2
                str = ".|."*r
                print(str.center(M, '-'),end="\n")
        

