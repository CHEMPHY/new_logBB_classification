import os
with open('../data/features_clean.csv') as f:
    first_line = f.readline()
    first_line = first_line.rstrip(os.linesep)
    first_line = first_line.split(',')
    first_line = first_line[1:]
    f.close()
for i in range(len(first_line)):
    if 'PubchemFP' in first_line[i]:
        index = i
        break
file_name_prefix_list = ['x_train','x_test']
for file_name_prefix in file_name_prefix_list:
    data = []
    with open('../data/' + file_name_prefix + '.csv') as f:
        for line in f:
            temp = line.rstrip(os.linesep) 
            temp = temp.split(',')
            data.append(temp)
        f.close()
    with open('../data/' + file_name_prefix + '_padel.csv','w') as f:
        f.write(','.join(first_line[:index]))
        f.write(os.linesep)
        for i in range(len(data)):
            f.write(','.join(data[i][:index]))
            f.write(os.linesep)
        f.close()
    with open('../data/' + file_name_prefix +'_pubchem.csv','w') as f:
        f.write(','.join(first_line[index:]))
        f.write(os.linesep)
        for i in range(len(data)):
            f.write(','.join(data[i][index:]))
            f.write(os.linesep)
        f.close()
    with open('../data/' + file_name_prefix + '_padel_pubchem.csv','w') as f:
        f.write(','.join(first_line))
        f.write(os.linesep)
        for i in range(len(data)):
            f.write(','.join(data[i]))
            f.write(os.linesep)
        f.close()
