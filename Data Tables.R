# Create the data
test_case_sizes <- c(200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000)
milliseconds <- c(76.27615, 689.775835, 2100.743835, 6354.11386, 6514.340905, 20058.94233, 20063.06538, 60182.29921, 60812.82248, 60311.54698)

# Create a data frame
data <- data.frame(Test_Case_Sizes = test_case_sizes, Milliseconds = milliseconds)

# Print the data frame
print(data)

# Plot the data
plot(data$Test_Case_Sizes, data$Milliseconds, type = "o", 
     xlab = "Test Case Sizes", ylab = "Milliseconds",
     main = "Test Case Sizes vs. Milliseconds")
