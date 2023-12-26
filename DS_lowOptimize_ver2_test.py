import numpy as np
import str2tree 
str_name = str2tree.load_str_tree('C:\\Opt_files\\GP2019_06_29_17h27m07s\\temp\\MPA_gen_1_pop_4.txt')
fitness = -445 
gen = 10 
population_num = 0 
best_hisFitness_inlow = -500
curFitness = [1,2,3]
temp_curFitness = '['
for i in range(len(curFitness)):
	temp_curFitness = temp_curFitness + str(curFitness[i]) + ','
temp_curFitness = temp_curFitness + ']'

curFitness = temp_curFitness


import os 
thesyn = 'python DS_lowOptimize_ver2.py ' + str_name + ' ' + str(fitness) + ' ' + str(gen) + ' ' \
					+ str(population_num) + ' ' + str(best_hisFitness_inlow) + ' ' + \
					str(curFitness)
#print(thesyn)
os.system(thesyn)