if (!require(likert)) { install.packages("likert") }
if (!require(psych)) { install.packages("psych") }
if (!require(here)) { install.packages("here") }
library(likert)
library(psych)
library(here)
par(cex.lab=1.2) # is for y-axis

par(cex.axis=1.2) # is for x-axis

# Function to convert input data to likert format with bounded levels
convert_to_likert <- function(method) {
  method$numHelped = factor(method$numHelped,
                        levels = c("1", "2", "3", "4", "5"),
                        ordered = TRUE)
  method$crowdSize = factor(method$crowdSize,
                        levels = c("1", "2", "3", "4", "5"),
                        ordered = TRUE)
  method$sessionsCompleted = factor(method$sessionsCompleted,
                        levels = c("1", "2", "3", "4", "5"),
                        ordered = TRUE)
  method$difficulty = factor(method$difficulty,
                        levels = c("1", "2", "3", "4", "5"),
                        ordered = TRUE)
  method$comfort = factor(method$comfort,
                        levels = c("1", "2", "3", "4", "5"),
                        ordered = TRUE)
  return(likert(method))
}


# Read the data files
method_1 <- read.table(here("data", "method_1.csv"), header = TRUE,
                     sep = ",")
method_2 <- read.table(here("data", "method_2.csv"), header = TRUE,
                       sep = ",")

# Convert to likert objects
likert_1 <- convert_to_likert(method_1)
likert_2 <- convert_to_likert(method_2)

fills <- c("grey", "grey")
method_names <- c("Method 1 (FIFO)", "Method 2  (MIMU)")
xlab <- "Method"
ylab <- "Likert Score"

# Generate the box plots
boxplot(method_1$numHelped, method_2$numHelped,
         main = "Question 1: Number of Students Helped",
         at = c(1, 2),
         names = method_names,
         xlab = xlab,
         ylab = ylab,
         col = fills
        )
boxplot(method_1$crowdSize, method_2$crowdSize,
         main = "Question 2: Estimated Crowd Size",
         at = c(1, 2),
         names = method_names,
         xlab = xlab,
         ylab = ylab,
         col = fills
        )
boxplot(method_1$sessionsCompleted, method_2$sessionsCompleted,
         main = "Question 3: Ability to Completely Answer Question",
         at = c(1, 2),
         names = method_names,
         xlab = xlab,
         ylab = ylab,
         col = fills
        )
boxplot(method_1$difficulty, method_2$difficulty,
         main = "Question 4: Question Difficulty",
         at = c(1, 2),
         names = method_names,
         xlab = xlab,
         ylab = ylab,
         col = fills
        )
boxplot(method_1$comfort, method_2$comfort,
         main = "Question 5: Tutor Comfort",
         at = c(1, 2),
         names = method_names,
         xlab = xlab,
         ylab = ylab,
         col = fills
        )
