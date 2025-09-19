from pyvis.network import Network


def get_visual_moore(data):
    G = Network(directed=True) 
    G.repulsion(spring_length=250)

    for state in data: 
        G.add_node('q' + str(state[0]) + '/y' + str(state[1])) 
    for state in data:    
        for i in range(len(data[state])): 
            G.add_edge('q' + str(state[0]) + '/y' + str(state[1]), 'q' + str(data[state][i][2]) + '/y' + str(data[state][i][1]), label='x' + str(data[state][i][0]+1)) # ��������� ����� � ������� ���� xK

    G.show('graph.html', notebook=False)

def get_visual_milly(data):
    G = Network(directed=True) 
    G.repulsion(spring_length=250)

    for i in range(len(data)):
        G.add_node('q' + str(data[i][0])) 
        
    for i in range(len(data)):
        G.add_edge('q' + str(data[i][0]), 'q' + str(data[i][3]), label='x' + str(data[i][1]) + '/y' + str(data[i][2]))

    G.show('graph.html', notebook=False)
