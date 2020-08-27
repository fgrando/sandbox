state <- read.csv(file="~/Downloads/github-sandbox/data-science/estatistica-pratica/homicidios-populacao.csv")
avg <- mean(state[["populacao"]])

avg_trim <- mean(state[["populacao"]], trim=0.1)

med <- median(state[["populacao"]])

weight_avg <- weighted.mean(state[["homicidio"]], w=state[["populacao"]])
#install.packages("matrixStats")

library("matrixStats")
weight_median <- weightedMedian(state[["homicidio"]], w=state[["populacao"]])
