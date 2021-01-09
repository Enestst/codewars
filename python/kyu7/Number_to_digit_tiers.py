def create_array_of_tiers(n):
	lst = []
	for i in range(1,len(str(n)) + 1):
		lst.append(str(n)[0:i])
	return lst


print(create_array_of_tiers(0))
