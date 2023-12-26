parent = None 
def get_data_csv(tree,parent):
	current_node = {}
	current_node['parent'] = parent
	current_node['name'] = tree.strname
	if tree.childs != None:
		current_node['children'] = []
		for i in range(len(tree.childs)):
			current_node['children'].append(get_data_csv(tree.childs[i], tree.strname))
	return current_node

import str2tree as st 
import Helper as hp 

tree_str = st.load_str_tree('C:/Opt_files/GP2019_06_15_17h00m26s/temp/MPA_gen_1_pop_0.txt')
tree = st.str2tree(tree_str,0,1,0,None)
tree = st.update_tree(tree)
# [Substrate,polygons,centroid,poly_list, poly_list_type] = hp.get_all_para_for_hfss(tree) # get necessary parameters for genscript function.
# name = 'C:/Users/DELL/Desktop/Newfolder/' # name of directory would
# 																			# be used to save .vbs and .hfss file.
# #tabname = global_tabname + str(gen) + '_pop_' + str(i) # name of directory
# 																			# would be used to save .tab file. 
# genscript(Substrate,polygons,centroid,name + '.vbs',name,name + '.hfss',poly_list,poly_list_type)
hp.drawtree(tree)
x = get_data_csv(tree,None)
print(x)
#import json
#with open(r'C:\Users\HupeCRD\Desktop\json.json','w') as xxx:
#    json.dump(x,xxx,indent=4)