import csv
import GeneSelfJupies as gs


#data = gs.import_data('./genome_weijian_ye_v5_Full_20190521204651.txt')

#data.run()
data_file_name = './genome_weijian_ye_v5_Full_20190521204651.txt'

# convert 23andme raw data
def twenty_three_and_me(data_file_name):
    #check_file(data_file_name)
    processed_data = {}
    with open(data_file_name, 'r') as data:
        data = csv.reader(data, delimiter='\t')
        for row in data:
            # make sure the genotype is valid
            print (row[-1])
            if len(row) == 4 and row[-1][-1] in ['A', 'T', 'G', 'C']:
                processed_data[row[0]] = row[-1]

    return processed_data


#twenty_three_and_me(data_file_name)

import plotly.plotly as py
import plotly.graph_objs as go

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart')