size=10
prob=.12
A=pbinom(2,size,prob)
B=pbinom(1,size,prob)
cat(format(A,digits=3))
cat("\n")
cat(format(1-B,digits=3))
