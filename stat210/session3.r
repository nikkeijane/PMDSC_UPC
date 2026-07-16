mpower <- function(mat, power) {
	product <- rbind(c(1,0), c(0,1))

	for (i in 1:power) {
		product <- product %*% mat
	}
	product
}
