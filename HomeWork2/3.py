eps = 1.0
one_Plus_eps = 2.0
while (one_Plus_eps != 1):
	eps = eps /2
	one_Plus_eps = 1.0 + eps
	print ( " eps = " , eps , " , one + eps = " , one_Plus_eps )
