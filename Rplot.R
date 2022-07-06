library(ggplot2)
library(data.table)

# RENBP (601/602)

# Difference to control average
average <- data.table(
  names=c("Diluted by 1:2","MspJI digested", "NC"),
  HEK=c(-0.2355963389,2.899072647,6.28086408),
  HeLa=c(-0.2798614502,3.730486552,5.022163391),
  MCF=c(0.01104990641,4.550682068,5.936459859)
)

setkey(average,names)  

dtAV = as.matrix(average, rownames=TRUE)

# Difference to control deviation

stdev <- data.table(
  names=c("Diluted by 1:2","MspJI digested", "NC"),
  HEK=c(0.4681343739,0.7698417225,0.5043162904),
  HeLa=c(0.4920205207,0.4256293517,0.2265993952),
  MCF=c(0.2568224415,2.642113508,0.2193727545)
)

setkey(stdev,names)  

dtSD = as.matrix(stdev, rownames=TRUE)

# Limit to graph
limup <- 1.2*max(dtAV)
limdown <- 1.2*min(dtAV)

# Error bar or something
error.bar <- function(x, y, upper, lower=upper, length=0.1,...){
  arrows(x,y+upper, x, y-lower, angle=90, code=3, length=length, ...)
}

# Graph this shit
ze_barplot <- barplot(dtAV ,
                      beside=T ,
                      legend.text=T,
                      col=c("gray48", "gray64", "gray82"),
                      ylim=c(limdown-10,limup), 
                      ylab="delta CT", 
                      main = "RENBP primers - difference to not treated gDNA",
                      args.legend = list(x = "topright",inset = c(-0.2, 0.8)))

error.bar(ze_barplot,dtAV, dtSD)

