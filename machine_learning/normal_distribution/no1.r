mean=30
std=4
cat(format(pnorm(40,mean,std),digits=3))
cat("\n")
cat(format(1-pnorm(21,mean,std),digits=3))
cat("\n")
cat(format(pnorm(35,mean,std)-pnorm(30,mean,std),digits=3))
