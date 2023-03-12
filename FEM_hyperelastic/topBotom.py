import numpy as np
import os

name = "tex"
# Deformation gradient F
F = np.array([[1.2, 0.2],   # Assumption used for testing this function
            [0.2, 1.2]])


rvetype = 1

with open("Giraffe/RVE_data/grfTop" + str(rvetype) + ".txt", "r") as file:
    top = file.read()

with open("Giraffe/RVE_data/grfBottom" + str(rvetype) + ".txt", "r") as file:
    bottom = file.read()

# Read RVE data file
with open("Giraffe/RVE_data/rve{}.txt".format(rvetype), "r") as file:
    data = [float(x) for x in file.read().split()]
    Lxx, Lyy, t, nx, ny = data[:5]
    nx = int(nx)
    ny = int(ny)

# Get the nodal coordinates of the ends of the beams

X = np.zeros(((nx + ny) * 2, 3))

# Read the nodedata text files from data folder
with open("Giraffe/RVE_data/nodedata" + str(rvetype)  + ".txt", "r") as file:
    for i, line in enumerate(file):
        X[i] = [float(x) for x in line.strip().split()]
        

def giraffeInputGenerator(rvetype, name, F, Lxx, Lyy, t, nx, ny, X):

    # Consider rvetype                 
    rr = rvetype  


    # Create new folder with name of .inp file
    inp = name + '_' + str(rr)                       # inp = tex_0
    folder = "Giraffe/" + inp                              # folder = E:/Softwares/01/Giraffe/tex_0
    os.makedirs("Giraffe/" + inp, exist_ok=True)               # Creates tex_0 folder

    
    # Deformation gradient F
    # F = np.array([[1.2, 0.2],   # Assumption used for testing this function
    #             [0.2, 1.2]])


    # Get the strain from the deformation gradient
    strain = F - np.eye(2)

    # Get alpha values from strain tensor
    alpha1 = strain[0,0]
    alpha2 = strain[0,1]
    alpha3 = strain[1,0]
    alpha4 = strain[1,1]
    
    # Convert alpha into a matrix
    alpha = np.array([[alpha1, alpha2],[alpha3, alpha4]])
    # print(f'alpha = {alpha}')


    # Initialize disp and calculate the displacement
    # of the ends of the beams
    disp = np.zeros(((nx + ny) * 2, 2))
    disp[:,0] = alpha1*X[:,0] + alpha2*X[:,1]
    disp[:,1] = alpha3*X[:,0] + alpha4*X[:,1]

    

    displacement_block = []

    for i in range(1, ((nx + ny) * 2) + 1):
        block = ("""\n
NodalDisplacement {} NodeSet {} CS 125 NTimes 2
//Time UX UY UZ ROTX ROTY ROTZ
0\t0\t0\t0\t0\t0\t0
1\t{}\t{}\t0\t0\t0\t0\n
""").format(i, i + 4, disp[i-1][0], disp[i-1][1])
        displacement_block.append(block)

  
    # Open the file for writing

    filepath = 'Giraffe/' + inp + '/' + inp + '.inp'         # filepath - E:/Softwares/01/Giraffe/tex_0/tex_0.inp
    with open(filepath, 'w') as file:
        
    # Top part of Giraffe input file

        file.write(top) 

    # Displacement block

        file.write("\n\nDisplacements {}\n\n".format((nx + ny) * 2))
        for i in range((nx + ny) * 2):
            file.write(displacement_block[i])


    # Bottom part of Giraffe input file

        file.write(bottom)


    return inp, Lxx, Lyy, t, folder


inp, Lxx, Lyy, t, folder = giraffeInputGenerator(rvetype, name, F, Lxx, Lyy, t, nx, ny, X)