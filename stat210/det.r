vec <- c(2, -1, 3, 2, 0, 2, 1, 2, 2)
mat <- matrix(vec, byrow = TRUE, nrow = 3)

determinant <- det(mat)

cat("given matrix:\n")
print(nrow)
cat("determinant:", determinant, "\n")
