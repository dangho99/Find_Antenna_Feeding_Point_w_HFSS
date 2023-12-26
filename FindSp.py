import str2tree as s2t
import Helper as hp
import initGlobal as init
import math 
import matplotlib.pyplot as plt

ant = init.AnT()

# tree_str = s2t.load_str_tree('C:/Users/HupeCRD/Desktop/24-35Ghzz/GP2019_03_28_11h18m27s/temp/MPA_gen_1_pop_2.txt')
# tree = s2t.str2tree(tree_str,0,1,0,None)
# #hp.drawtree(tree)
# tree = s2t.update_tree(tree)
# tree.childs[1].valueofnode.plot()

# def FindSP(ind):
import numpy as np 
def create_list_point(tree):
	basic_shapes = hp.get_all_basics_subtree_GP(tree)
	print(basic_shapes)
	#basic_shapes = [['L1'],[np.array([[0,0],[20,0],[20,5],[5,5],[5,16],[0,16]])]]
	#basic_shapes = [['L2'],[np.array([[0,0],[20,0],[20,16],[1000   ,16],[10,5],[0,5]])]]
	#basic_shapes = [['L3'],[np.array([[0,0],[5,0],[5,10],[20,10],[20,16],[0,16]])]]
	#basic_shapes = [['L4'],[np.array([[0,10],[5,10],[5,0],[10,0],[10,16],[0,16]])]]
	#basic_shapes = [['U1'],[np.array([[0,0], [10,0], [10,10], [7,10], [7,5], [3,5], [3,10], [0,10]])]]
	#basic_shapes = [['U2'],[np.array([[0,0], [3,0], [3,5], [7,5], [7,0], [10,0], [10,10], [0,10]])]]
	#basic_shapes = [['U3'],[np.array([[0,0], [10,0], [10,10], [0,10], [0,7], [5,7], [5,3], [0,3]])]]
	#basic_shapes = [['U4'],[np.array([[0,0], [10,0], [10,3], [5,3], [5,7], [10,7], [10,10], [0,10]])]]
	list_point = []

	for i in range(len(basic_shapes[0])):
		if basic_shapes[0][i] == 'L1' or basic_shapes[0][i] == 'L3':
			a = 2
			b = 4
			temp_list_point = []					# save all temporary points 
			temp_shape = basic_shapes[1][i]
			start_point = (temp_shape[0][0], temp_shape[0][1])
			temp_list_point.append(start_point)
			cur_point = start_point  				# current point in 2D coordinate.
			while temp_list_point[-1][1] < temp_shape[a][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point) # update.
				if cur_point[1] < temp_shape[a][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[a][1]:
					break
				while  temp_list_point[-1][0] < temp_shape[a][0]:
					cur_point = (cur_point[0] + ant.distance_each_point,cur_point[1])
					if cur_point[0] < temp_shape[a][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[a][0]:
						break
				cur_point = (start_point[0], cur_point[1])
				
			# start_point = cur_point
			cur_point = (start_point[0], cur_point[1] - ant.distance_each_point)
			while temp_list_point[-1][1] < temp_shape[4][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[4][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[4][1]:
					break
				while temp_list_point[-1][0] < temp_shape[3][0]:
					cur_point = (cur_point[0] + ant.distance_each_point,cur_point[1])
					if cur_point[0] < temp_shape[3][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[3][0]:
						break
				cur_point = (start_point[0], cur_point[1])
			del temp_list_point[0]

		elif basic_shapes[0][i] == 'L2':
			temp_list_point = []
			temp_shape = basic_shapes[1][i]
			start_point = (temp_shape[0][0], temp_shape[0][1])
			temp_list_point.append(start_point)
			cur_point = start_point  				# current point in 2D coordinate.
			while temp_list_point[-1][1] < temp_shape[4][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point) # update.
				if cur_point[1] < temp_shape[4][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[4][1]:
					break
				while  temp_list_point[-1][0] < temp_shape[1][0]:
					cur_point = (cur_point[0] + ant.distance_each_point,cur_point[1])
					if cur_point[0] < temp_shape[1][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[1][0]:
						break
				cur_point = (start_point[0], cur_point[1])

			cur_point = (temp_shape[4][0], cur_point[1] - ant.distance_each_point)
			while temp_list_point[-1][1] < temp_shape[2][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[2][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[2][1]:
					break
				while temp_list_point[-1][0] < temp_shape[2][0]:
					cur_point = (cur_point[0] + ant.distance_each_point,cur_point[1])
					if cur_point[0] < temp_shape[2][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[2][0]:
						break
				cur_point = (temp_shape[4][0], cur_point[1])
			del temp_list_point[0]

		elif basic_shapes[0][i] == 'L4':
			temp_list_point = []
			temp_shape = basic_shapes[1][i]
			start_point = (temp_shape[0][0], temp_shape[0][1])
			temp_list_point.append(start_point)
			cur_point = start_point  				# current point in 2D coordinate.
			while temp_list_point[-1][1] < temp_shape[4][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point) # update.
				if cur_point[1] < temp_shape[4][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[4][1]:
					break
				while  temp_list_point[-1][0] < temp_shape[4][0]:
					cur_point = (cur_point[0] + ant.distance_each_point,cur_point[1])
					if cur_point[0] < temp_shape[4][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[4][0]:
						break
				cur_point = (start_point[0], cur_point[1])
			#######
			cur_point = (temp_shape[1][0], temp_shape[1][1] + ant.distance_each_point)
			while temp_list_point[-1][1] > temp_shape[3][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] - ant.distance_each_point)
				if cur_point[1] > temp_shape[3][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] <= temp_shape[3][1]:
					break
				while temp_list_point[-1][0] < temp_shape[3][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[3][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[3][0]:
						break
				cur_point = (temp_shape[1][0], cur_point[1])
			del temp_list_point[0]

		elif basic_shapes[0][i] == 'U1':
			temp_list_point = []
			temp_shape = basic_shapes[1][i]
			start_point = (temp_shape[7][0], temp_shape[7][1])
			temp_list_point.append(start_point)
			cur_point = start_point  				# current point in 2D coordinate.
			while temp_list_point[-1][1] > temp_shape[5][1]:
				cur_point = (cur_point[0] + ant.distance_each_point,cur_point[1] - ant.distance_each_point)
				if cur_point[1] > temp_shape[5][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] <= temp_shape[5][1]:
					break
				while temp_list_point[-1][0] < temp_shape[5][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[5][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[5][0]:
						break
				cur_point = (temp_shape[7][0], cur_point[1])
			cur_point = (temp_shape[7][0] , cur_point[1] + ant.distance_each_point)
			while temp_list_point[-1][1] > temp_shape[1][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] - ant.distance_each_point)
				if cur_point[1] > temp_shape[1][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] <= temp_shape[1][1]:
					break
				while temp_list_point[-1][0] < temp_shape[1][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[1][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[1][0]:
						break
				cur_point = (temp_shape[7][0], cur_point[1])
			cur_point = (temp_shape[4][0], temp_shape[4][1])

			while temp_list_point[-1][1] < temp_shape[2][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[2][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[2][1]:
					break
				while temp_list_point[-1][0] < temp_shape[2][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[2][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[2][0]:
						break
				cur_point = (temp_shape[4][0], cur_point[1])

		elif basic_shapes[0][i] == 'U2':
			temp_list_point = []
			temp_shape = basic_shapes[1][i]
			start_point = (temp_shape[0][0], temp_shape[0][1])
			temp_list_point.append(start_point)
			cur_point = start_point  				# current point in 2D coordinate.
			while temp_list_point[-1][1] < temp_shape[2][1]:
				cur_point = (cur_point[0] + ant.distance_each_point,cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[2][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[2][1]:
					break
				while temp_list_point[-1][0] < temp_shape[2][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[2][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[2][0]:
						break
				cur_point = (temp_shape[0][0], cur_point[1])
			cur_point = (temp_shape[0][0] , temp_shape[2][1])
			while temp_list_point[-1][1] < temp_shape[6][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[6][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[6][1]:
					break
				while temp_list_point[-1][0] < temp_shape[6][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[6][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[6][0]:
						break
				cur_point = (temp_shape[0][0], cur_point[1])
			cur_point = (temp_shape[3][0], temp_shape[3][1])

			while temp_list_point[-1][1] > temp_shape[5][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] - ant.distance_each_point)
				if cur_point[1] > temp_shape[5][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] <= temp_shape[5][1]:
					break
				while temp_list_point[-1][0] < temp_shape[5][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[5][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[5][0]:
						break
				cur_point = (temp_shape[3][0], cur_point[1])
		elif basic_shapes[0][i] == 'U3':
			temp_list_point = []
			temp_shape = basic_shapes[1][i]
			start_point = (temp_shape[0][0], temp_shape[0][1])
			temp_list_point.append(start_point)
			cur_point = start_point  				# current point in 2D coordinate.
			while temp_list_point[-1][1] < temp_shape[6][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[6][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[6][1]:
					break
				while temp_list_point[-1][0] < temp_shape[6][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[6][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[6][0]:
						break
				cur_point = (temp_shape[0][0], cur_point[1])
			cur_point = (temp_shape[6][0] , temp_shape[0][1])
			while temp_list_point[-1][1] < temp_shape[2][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[2][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[2][1]:
					break
				while temp_list_point[-1][0] < temp_shape[2][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[2][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[2][0]:
						break
				cur_point = (temp_shape[6][0], cur_point[1])
			cur_point = (temp_shape[4][0], temp_shape[4][1])

			while temp_list_point[-1][1] < temp_shape[2][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[2][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[2][1]:
					break
				while temp_list_point[-1][0] < temp_shape[5][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[5][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] > temp_shape[5][0]:
						break
				cur_point = (temp_shape[4][0], cur_point[1])

		elif basic_shapes[0][i] == 'U4':
			temp_list_point = []
			temp_shape = basic_shapes[1][i]
			start_point = (temp_shape[0][0], temp_shape[0][1])
			temp_list_point.append(start_point)
			cur_point = start_point  				# current point in 2D coordinate.
			while temp_list_point[-1][1] < temp_shape[2][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[2][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[2][1]:
					break
				while temp_list_point[-1][0] < temp_shape[2][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[2][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[2][0]:
						break
				cur_point = (temp_shape[0][0], cur_point[1])
			cur_point = (temp_shape[0][0], cur_point[1])

			while temp_list_point[-1][1] < temp_shape[4][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[4][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[4][1]:
					break
				while temp_list_point[-1][0] < temp_shape[4][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[4][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] >= temp_shape[4][0]:
						break
				cur_point = (temp_shape[0][0], cur_point[1])
			cur_point = (temp_shape[0][0], cur_point[1])

			while temp_list_point[-1][1] < temp_shape[6][1]:
				cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1] + ant.distance_each_point)
				if cur_point[1] < temp_shape[6][1]:
					temp_list_point.append(cur_point)
				if cur_point[1] >= temp_shape[6][1]:
					break
				while temp_list_point[-1][0] < temp_shape[6][0]:
					cur_point = (cur_point[0] + ant.distance_each_point, cur_point[1])
					if cur_point[0] < temp_shape[6][0]:
						temp_list_point.append(cur_point)
					if cur_point[0] > temp_shape[6][0]:
						break
				cur_point = (temp_shape[0][0], cur_point[1])

		if list_point == []:
			list_point = temp_list_point
			#print('init')
		else:
			# print(temp_list_point)
			# print(basic_shapes[0][i])
			# print('ok')
			# x = []
			# y = []
			# for i in range(len(temp_list_point)):
			# 	x.append(temp_list_point[i][0])
			# 	y.append(temp_list_point[i][1])
			# plt.plot(x,y,'ro')
			# #plt.plot(basic_shapes[1][i][:,0],basic_shapes[1][i][:,1],'ro')
			# plt.show()
			list_point = list_point + update_list(list_point, temp_list_point)

			#print('ok')

	########################## test
	#print(list_point)
	#print(len(list_point))
	x = []
	y = []
	for i in range(len(list_point)):
		x.append(list_point[i][0])
		y.append(list_point[i][1])
	plt.plot(x,y,'ro')
	# plt.plot(basic_shapes[1][0][:,0],basic_shapes[1][0][:,1],'ro')
	################################
	return list_point



def update_list(list1, list2):
	# function update new list of shortting pin positions delete the points that have smaller distance 
	newlist2 = []
	signal = False
	for i in range(len(list2)):
		for ii in range(len(list1)):
			if euclidean_distance(list2[i],list1[ii]) < (ant.distance_each_point):
				signal = True
		if not signal:
			newlist2.append(list2[i])
		signal = False
	return newlist2

def update_list_2(list1, list2):
	# function update new list of shortting pin positions delete the points that have smaller distance 
	# specially for discard the feed point.
	newlist2 = []
	signal = False
	for i in range(len(list2)):
		for ii in range(len(list1)):
			if euclidean_distance(list2[i],list1[ii]) < (ant.distance_each_point)/2:
				signal = True
		if not signal:
			newlist2.append(list2[i])
		signal = False
	return newlist2

def euclidean_distance(point1,point2):
	return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)



#create_list_point(tree)

				




