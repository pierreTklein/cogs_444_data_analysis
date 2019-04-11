if(!require(likert)){install.packages("likert")}
if(!require(psych)){install.packages("psych")}
if(!require(here)){install.packages("here")}
library(likert)
library(psych)
library(here)

# Function to convert input data to likert format with bounded levels
convert_to_likert <- function (method) {
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
method_1 <- read.table(here("data", "method_1.csv"), header=TRUE, 
                     sep=",")
method_2 <- read.table(here("data", "method_2.csv"), header=TRUE, 
                       sep=",")

# Convert to likert objects
likert_1 <- convert_to_likert(method_1)
likert_2 <- convert_to_likert(method_2)

# Generate the box plots
boxplot(method_1$numHelped, method_2$numHelped,
         main = "Number of Students Helped",
         at = c(1,2),
         names = c("Method 1", "Method 2"),
         xlab="Method",
         ylab="Likert Score"
        )
boxplot(method_1$crowdSize, method_2$crowdSize,
         main = "Estimated Crowd Size",
         at = c(1,2),
         names = c("Method 1", "Method 2"),
         xlab="Method",
         ylab="Likert Score"
        )
boxplot(method_1$sessionsCompleted, method_2$sessionsCompleted,
         main = "Ability to Completely Answer Question",
         at = c(1,2),
         names = c("Method 1", "Method 2"),
         xlab="Method",
         ylab="Likert Score"
        )
boxplot(method_1$difficulty, method_2$difficulty,
         main = "Question Difficulty",
         at = c(1,2),
         names = c("Method 1", "Method 2"),
         xlab="Method",
         ylab="Likert Score"
        )
boxplot(method_1$comfort, method_2$comfort,
         main = "Tutor Comfort",
         at = c(1,2),
         names = c("Method 1", "Method 2"),
         xlab="Method",
         ylab="Likert Score"
        )
