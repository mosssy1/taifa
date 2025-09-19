import workMachine
import visualisation
import workWithDataFiles


input_file = 'input3.txt'
output_file = 'output3.txt'
column, row = 0, 0

data, mode, column, row = workWithDataFiles.read_data(input_file, column, row)
print(data)

if mode == 'mili':
    moore = workMachine.milly_to_moore(data)
    print(moore)
    workWithDataFiles.write_data(output_file, moore, mode, column, row)
    visualisation.get_visual_moore(moore)       
elif mode == 'mur':
    milly = workMachine.moore_to_milly(data)
    print(milly)
    workWithDataFiles.write_data(output_file, milly, mode, column, row)
    visualisation.get_visual_milly(milly)


