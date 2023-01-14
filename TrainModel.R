library(pmml)
library(e1071)
dataDir <- "data/features.csv"
data <- read.csv(dataDir, header = TRUE)
data$SongName = NULL

# make model
modelsvm = svm(Difficulty~., data = data, epsilon = 0.5)
tuneResult <- tune(svm, Difficulty~.,  data = data, ranges = list(epsilon = 0.5, cost = seq(0.01,50,0.1)))
pmmldata <- pmml(tuneResult$best.model)
saveXML(pmmldata, file="Edda-MLDP-R.pmml")