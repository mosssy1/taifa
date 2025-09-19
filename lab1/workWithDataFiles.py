def read_data(filename, column, row):
    with open(filename, 'r') as f:

        column, row, mode = f.readline().split()

        column = int(column)
        row = int(row)

        data = {}

        if mode == 'mili':

            for i in range(row):
                line = f.readline().split()

                for j in range(column):
                    output, next_state = line[j].split('/')
                    if (output == '-' or next_state == '-'):
                        continue
                        
                    output = int(output[1:])
                    next_state = int(next_state[1:])
                    state = j

                    if state not in data:
                        data[state] = []

                    data[state].append((i, next_state, output))

        elif mode == 'mur':
            data = []
            for i in range(row + 1):
                line = f.readline().split()
                for j in range(len(line)):
                    if line[j] != '-':
                        line[j] = int(line[j][1:])
                data.append(line)
                    
        return data, mode, column, row

def write_data(filename, data, mode, column, row):
    with open(filename, 'w') as f:
        
        if mode == 'mili':
            arr = []

            fstring = ''
            for state in data: 
                fstring += 'q' + str(state[0]) + '/y' + str(state[1]) + ' '
                    
            f.write(fstring + '\n')
            
            for state in data: 
                line = []
                for tup in data[state]:
                    line.append('q' + str(tup[2]) + '/y' + str(tup[1]))
                arr.append(line)
            print(arr)
                    
            a = len(arr)
            b = len(arr[0])
            
            for j in range(b):
                for i in range(a):
                    if j < len(arr[i]):
                        f.write(arr[i][j] + ' ')
                f.write('\n')
         
        elif mode == 'mur': 
            print(data)
            data = sorted(data, key=lambda x: (x[0], x[1], x[2], x[3]))
            
            for i in range(1, row+1):
                line = ''
                for j in range(len(data)):
                    if data[j][1] == i:
                        line += 'q' + str(data[j][3]) + '/y' + str(data[j][2]) + ' '
                        
                f.write(line + '\n')

            print(data)
