mean=20
std=2
a=pnorm(19.5,mean,std)
b=pnorm(22,20,2)-pnorm(20,20,2)
cat(format(a,digits=3))
cat("\n")
cat(format(b,digits=3))
