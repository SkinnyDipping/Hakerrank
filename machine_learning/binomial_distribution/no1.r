size=4
prob=0.8
A=1-pbinom(2,size,prob)
B=pbinom(1,size,prob)
cat(format(A,digits=3))
cat("\n")
cat(format(B,digits=2))
