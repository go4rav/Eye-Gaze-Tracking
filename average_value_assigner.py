from scipy.spatial import distance as dist
import interface2 as interface
import main2
def callibration(ratios,ear,iris_ratios,minLoc):
	mini=100000
	min_index=-1
	for i in range(len(ratios)):
		temp=abs(ratios[i]-ear)
		if temp < mini:
			mini=temp
			min_index=i
	interface.Y_index=min_index
	if min_index==2:
		main2.consecframes2+=1
	else:
		main2.consecframes2=0
	
	mini=100000
	min_index=-1

	for i in range(len(iris_ratios)):
		temp=abs(iris_ratios[i]-minLoc[0])
		if temp<mini:
			mini=temp
			min_index=i
	interface.X_index=min_index
	




	