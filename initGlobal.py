# linh.homanh@hust.edu.vn 
# thuan.bb.hust@gmail.com - 2018
import math
numProcess = [4]#,3] # number of the script would be run in each computer.
# = ['CRD02-PC'] #-- list of exist computers for running scripts.
PCnames =  ['DESKTOP-RA17117'] #['DESKTOP-K6646BG']
#PCnames = ['HupeCRD-PC','CRD-SERVER'] # ['DESKTOP-RA17117']#, 'CRD-SERVER'] #,'CRD01-PC'] # here for running parallel computer. -------- 
users_and_pass = {'CRD01-PC': ['CRD01', 'crd608'],'CRD-SERVER':['Administrator','Crd608']}
Re_trainning = False
Re_trainning_folder = 'C:/Opt_files/GP2019_04_08_11h10m11s/'		 # path to the folder need being Re_trainning_folderd. 
start_gen_for_retraining = 17
# signal_for_run_first_gen = True   
save_paras = 'numbs_paras.txt'   # do not change this parameter
save_names = 'names_paras.txt'   # de not change this parameter
# related to antenna.
debug = True   # this variable turn on to debug the program that related to GEOPANDAS library.
class AnT:
	def __init__(self):
		self.c = 3e8					# save_on 1
		self.fC = 3.5e9 				# save_on 2
		self.fStart = 3.3				# save_on 3         GHz
		self.fStop = 3.7				# save_on 4			GHz
		self.npoints = 100				# save_on 5
		self.Band_fitness = [3.4,3.6]	# save_on 6, 7      GHz
		self.Point_start_eval, self.Point_stop_eval = self.__getNum_point_for_evaluation(self.Band_fitness) 		# save_on 8, 9
		self.Center_start_eval, self.Center_stop_eval = self.__getNum_center_point_evaluation(self.fC)	# save_on 10, 11
		self.substrate_material = 'FR4_epoxy'													# save_on text_1
		self.hfssExePath   = 'C:/"Program Files"/Ansoft/HFSS14.0/Win64/hfss.exe'; # location of hfss executable (needs to be the
		
		#self.hfssExePath   = r'C:\"Program Files (x86)"\Ansoft\HFSS13.0\hfss.exe'; # location of hfss executable (needs to be the  
		self.resultsDir    = 'path2';   # location of results folders (containing final .hfss files)			# save_on text_2
		self.tmpDir        = 'path3';  # location of hfss temp files 								
		self.tmpTab 	   = 'path4'																
		self.overcome_desired = self.resultsDir + r'C:\Opt_files\overcome_desired'  # folder save any best found antenna structure with overcome of the
																	# fitness.
		self.Antenna_Name  	   = 'MPA'			# microstrip patch antenna 						# save_on  text_3
		self.maxTime = 7; # maximum allowed time (in minutes) for each computer to solve batch of files,
							# where the batch size is equal to the number ofs
							# processors on a computer
		self.cpu_percentage_kill = 4           # this help to detect any error in running hfss -> then kill. 
		self.hfss_shared_dir = 'path' 																					# save_on 46
		###________________________________________________________________________________________
		### 
		self.band2_examination = False
		self.fC2 = 2.4e9
		self.Band_fitness_2 = [2.3,2.5]
		self.Point_start_eval_2,self.Point_stop_eval_2 = self.__getNum_point_for_evaluation(self.Band_fitness_2) 		# save_on 42, 43
		self.Center_start_eval_2,self.Center_stop_eval_2 = self.__getNum_center_point_evaluation(self.fC2)	# save_on 44, 45
		self.hfss_save = False        						# whether save hfss after running or not.
		self.Find_shorting_point = False						# turn on or off the finding shorting point function.
		self.distance_each_point = 1.5						# distance between two shorting points.
		self.get_shorting_pin_data = False					# whether shorting pin data will be collected or not. 
		self.resonant_penalty = 100							# penalty weight for resonant frequency. 
		self.resonant_penalty_two_band = 200 			    # _____________________________________ but for two bands. 
		self.bandwidth_penalty = 6000 						# penalty for bandwidth -- ex: 6000*0.1[GHz] = 600 penalty for BW 100 MHz. 
		self.S11_penalty = 10 								# penalty for point S11 which has the value less than -10dB. "this pen should be greater 10"
	def __getNum_point_for_evaluation(self,Band_fitness):
		# function gets two specified points for evaluation_band.
		# for automated finding these two points.
		step = (self.fStop - self.fStart)/(self.npoints-1)
		temp = self.fStart
		i = 0
		while (temp < Band_fitness[0]):
			temp = temp + step
			i = i + 1
		temp = self.fStart
		j = 0
		while (temp < Band_fitness[1]):
			temp = temp + step
			j = j + 1
		#print(i,j)
		return i,j
	def __getNum_center_point_evaluation(self,fC):
		# similarly with above function.
		step = (self.fStop - self.fStart)/(self.npoints-1)
		temp = self.fStart
		i = 0
		center = fC/1e9
		while (temp < (center-0.01)):
			temp = temp + step
			i = i + 1
		temp = self.fStart
		j = 0
		while (temp < (center+0.01)):
			temp = temp + step
			j = j + 1
		return i,j

# related substrate.
class Sub:
	def __init__(self):
		self.radius = 10
		self.rangeOx = [2*self.radius,2*self.radius] # min/max range of width of patch antenna.				# save_on 12, 13
		self.rangeOy = [math.sqrt(3)*self.radius,math.sqrt(3)*self.radius] # min/max range of length of patch antenn.				# save_on 14, 15
		self.rangeOz = [0.6,1.6] # min/max range of 									# save_on 16, 17
		self.addition = 0 # 'mm' # increase the range of substrate.						# save_on 18
		self.decrease = 0 # 'mm' # number mm of substrate's both width and length will be decrease before create any pattern. 	# save_on 19

sub = Sub()
# L parameter.
min_basic_pattern = min(min(sub.rangeOx),min(sub.rangeOy))
minL_x = min_basic_pattern*0.1/2
maxL_x = min_basic_pattern*0.4/2
minL_y = min_basic_pattern*0.1/2
maxL_y = min_basic_pattern*0.4/2
# U parameter.
minU_x = (min_basic_pattern/9)/2
maxU_x = ((min_basic_pattern*0.8)/4)/2
minU_y = (min_basic_pattern/5)/2
maxU_y = (min_basic_pattern/2)/2
# related to 2D polygon.
class L:
	# L terminal.
	def __init__(self):
		self.rangex1 = [minL_x,maxL_x] #min/max range of x1.					# save_on 20, 21
		self.rangex2 = [minL_x,maxL_x]											# save_on 22, 23
		self.rangey1 = [minL_y,maxL_y]											# save_on 24, 25
		self.rangey2 = [minL_y,maxL_y]											# save_on 26, 27
class U:
	# U terminal.
	def __init__(self):
		self.rangex1 = [minU_x,maxU_x]											# save_on 28, 29
		self.rangex2 = [minU_x,maxU_x]											# save_on 30, 31
		self.rangex3 = [minU_x,maxU_x]											# save_on 32, 33
		self.rangey1 = [minU_y,maxU_y]											# save_on 34, 35
		self.rangey2 = [minU_y/2,minU_y*0.9]										# save_on 36, 37
		self.rangey3 = [minU_y,maxU_y]											# save_on 38, 39

class GP:
	def __init__(self):
		self.maxSub = 1 # maxdep of the the gensubstrate tree.
		self.maxPat = 1 
		self.maxBlue = 4														# save_on 40

		self.rate = 0 # is the rate of number grow type of ind in all popsize.
		self.proRed = 0.05 # the probability selects red node to apply GP operators. 
		self.prosubBlue = 0.75 # the probability selects subBlue node(like union node, Usubtree9 node,...)
		self.proBlue = 0.05 # the probability selects Blue node(Bluetree).
		self.proSubstrate = 0.05 # .............................
		self.proGensub = 0.05 # ...............................
		self.proGenpat = 1 - self.proRed - self.prosubBlue\
        - self.proBlue - self.proSubstrate - self.proGensub # Don't change, and make sure it's not negative.


		self.numpop = 50 # number of the individuals in a population.			# save_on 41
		self.numgen =  20 # number of generation in a GP process.
		self.reprorate = 0.4  # the rate of the best individuals that will be remained to the next generation. 
		self.crossrate = 0.4  # the probability selects the crossover operator.
		self.mutarate = 1 - self.reprorate - self.crossrate # the probability selects mutation operator.

		self.desired_fitness = -1000 # parameter for evaluating wheather a antenna structure is good enough or not, and then if it's 
									# good enough. It will be saved in a specified result folder.
		self.overcome_fitness = -1400 # parameter for evaluating wheather a antenna structure is overcome the desired result. It's will be
									# saved in specified result folder.
class lowlevel:
	def __init__(self):
		self.lowoptimize = True 
		self.low_propor  = 0.2     # proportion of inds will be optimized by lowlevel. 
		self.number_iters = 5  
		# self.step_size = 0.01
		self.init_number = 5
		self.active_function = 'relu' # the activation function for neural network architecture.
		self.optimizer = 'adam'       # the method for optimize the neural network.
		self.number_direction = 6    # the number of direction search.
		self.anpha = 0.2		 	  # the step size for direct search method.
		self.shrink = 0.5 			  # parameter to shrink the step size anpha.
		self.number_search_step = 6   # the number of search step for direct search method.
		self.number_sample = 15		  # number of samples for creating the trainning data for neural network.
		self.tmpDir        = 'path6'  # location of temporary hfss and vbs files.
		self.tmpTab 	   = 'path7'  # location of temporary .tab files.

import os
if not len(PCnames) == 1:
	# checking for successful setting up parallel runing.
	if not os.path.exists('\\\\' + PCnames[0] + '\\' + 'HFSS_shared'):
		raise Exception('you should make the path ' + '\\\\' + PCnames[0] + '\\' + 'HFSS_shared' + ' and it need be shared in network')
	if not os.path.exists('\\\\' + PCnames[0] + '\\' + 'Opt_files'):
		raise Exception('you should make the path ' + '\\\\' + PCnames[0] + '\\' + 'Opt_files' + ' and it need be shared in network')

	for i in range(len(PCnames) -1):
		ii = i + 1
		if not os.path.exists('\\\\' + PCnames[ii] + '\\' + 'HFSS_shared'):
			raise Exception('you should make the path ' + '\\\\' + PCnames[ii] + '\\' + 'HFSS_shared' + ' and it need be shared in network')
	print('running in PARALLEL ')
