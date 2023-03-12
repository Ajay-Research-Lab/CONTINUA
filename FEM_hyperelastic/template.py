import numpy as np
import string
import os
import time

# template_string = "Your name is ${firstname} ${lastname}"
# t = string.Template(template_string)
# result = t.substitute(firstname="Florian", lastname="Dahlitz")
# print(result)

##########

name = 'tex'
rvetype = 1
F = np.array([[1.2, 0.2],   # Assumption used for testing this function
            [0.2, 1.2]])

########################

# # Template

# ##########################
# start_time = time.time()

# # def giraffeInputGenerator(rvetype, name, F):

# # Consider rvetype
# rr = rvetype

# # Create new folder with name of .inp file
# inp = name + '_' + str(rr)
# folder = "Giraffe/" + inp
# os.makedirs(folder, exist_ok=True)

# # Take inputs from text file and assign following variables
# Lxx, Lyy, t, nx, ny = 1.0, 1.0, 1.0, 2, 2
# X = np.zeros(((nx + ny) * 2, 3))
# # Define nodal coordinates
# X = np.array([
#     [0, 2.27273, 0],
#     [9.09091, 2.27273, 0],
#     [0, 6.81818, 0],
#     [9.09091, 6.81818, 0],
#     [2.27273, 0, 0],
#     [2.27273, 9.09091, 0],
#     [6.81818, 0, 0],
#     [6.81818, 9.09091, 0]
# ])


# # Deformation gradient F
# strain = F - np.eye(2)
# alpha1 = strain[0,0]
# alpha2 = strain[0,1]
# alpha3 = strain[1,0]
# alpha4 = strain[1,1]
# alpha = np.array([[alpha1, alpha2],[alpha3, alpha4]])

# # Calculate the displacement of the ends of the beams
# disp = np.zeros(((nx + ny) * 2, 2))
# disp[:,0] = alpha1*X[:,0] + alpha2*X[:,1]
# disp[:,1] = alpha3*X[:,0] + alpha4*X[:,1]


# # Compute the number of nodes
# num_nodes = (nx + ny) * 2

# # Generate the displacement block
# disp_block = ""
# for i in range(num_nodes):
#     disp_block += f"""
# NodalDisplacement {i+1} NodeSet {i+5} CS 125 NTimes 2
# //Time UX UY UZ ROTX ROTY ROTZ
# 0\t0\t0\t0\t0\t0\t0
# 1\t{disp[i,0]}\t{disp[i,1]}\t0\t0\t0\t0
# """

# top = """ 
# Nodes	132
# //Yarn 1
# Node	1	0	2.27273	0
# Node	2	0.2835622252237	2.27273	0.05329356249635
# Node	3	0.5671244504474	2.27273	0.1065871249927
# Node	4	0.8503341952247	2.27273	0.1670006134745
# Node	5	1.133543940002	2.27273	0.2274141019563
# Node	6	1.417458641122	2.27273	0.2735878303818
# Node	7	1.701373342242	2.27273	0.3197615588073
# Node	8	1.987050436493	2.27273	0.3303358411347
# Node	9	2.272727530744	2.27273	0.3409101234621
# Node	10	2.55866899577	2.27273	0.3168474138206
# Node	11	2.844610460796	2.27273	0.2927847041791
# Node	12	3.1289657560775	2.27273	0.25282108957355
# Node	13	3.413321051359	2.27273	0.212857474968
# Node	14	3.6966189001435	2.27273	0.1622932570533
# Node	15	3.979916748928	2.27273	0.1117290391386
# Node	16	4.262685874464	2.27273	0.0558645195693001
# Node	17	4.545455	2.27273	1.873501354055E-16
# Node	18	4.828224125536	2.27273	-0.0558645195692999
# Node	19	5.110993251072	2.27273	-0.1117290391386
# Node	20	5.3942910998565	2.27273	-0.1622932570533
# Node	21	5.677588948641	2.27273	-0.212857474968
# Node	22	5.9619442439225	2.27273	-0.25282108957355
# Node	23	6.246299539204	2.27273	-0.2927847041791
# Node	24	6.53224100423	2.27273	-0.3168474138206
# Node	25	6.818182469256	2.27273	-0.3409101234621
# Node	26	7.103859563507	2.27273	-0.3303358411347
# Node	27	7.389536657758	2.27273	-0.3197615588073
# Node	28	7.673451358878	2.27273	-0.2735878303818
# Node	29	7.957366059998	2.27273	-0.2274141019563
# Node	30	8.2405758047755	2.27273	-0.1670006134745
# Node	31	8.523785549553	2.27273	-0.1065871249927
# Node	32	8.8073477747765	2.27273	-0.0532935624963502
# Node	33	9.09091	2.27273	-3.0278890506E-16
# //Yarn 2
# Node	34	0	6.81818	0
# Node	35	0.2835622252237	6.81818	-0.05329356249635
# Node	36	0.5671244504474	6.81818	-0.1065871249927
# Node	37	0.8503341952247	6.81818	-0.1670006134745
# Node	38	1.133543940002	6.81818	-0.2274141019563
# Node	39	1.417458641122	6.81818	-0.2735878303818
# Node	40	1.701373342242	6.81818	-0.3197615588073
# Node	41	1.987050436493	6.81818	-0.3303358411347
# Node	42	2.272727530744	6.81818	-0.3409101234621
# Node	43	2.55866899577	6.81818	-0.3168474138206
# Node	44	2.844610460796	6.81818	-0.2927847041791
# Node	45	3.1289657560775	6.81818	-0.25282108957355
# Node	46	3.413321051359	6.81818	-0.212857474968
# Node	47	3.6966189001435	6.81818	-0.1622932570533
# Node	48	3.979916748928	6.81818	-0.1117290391386
# Node	49	4.262685874464	6.81818	-0.0558645195693001
# Node	50	4.545455	6.81818	-1.873501354055E-16
# Node	51	4.828224125536	6.81818	0.0558645195692999
# Node	52	5.110993251072	6.81818	0.1117290391386
# Node	53	5.3942910998565	6.81818	0.1622932570533
# Node	54	5.677588948641	6.81818	0.212857474968
# Node	55	5.9619442439225	6.81818	0.25282108957355
# Node	56	6.246299539204	6.81818	0.2927847041791
# Node	57	6.53224100423	6.81818	0.3168474138206
# Node	58	6.818182469256	6.81818	0.3409101234621
# Node	59	7.103859563507	6.81818	0.3303358411347
# Node	60	7.389536657758	6.81818	0.3197615588073
# Node	61	7.673451358878	6.81818	0.2735878303818
# Node	62	7.957366059998	6.81818	0.2274141019563
# Node	63	8.2405758047755	6.81818	0.1670006134745
# Node	64	8.523785549553	6.81818	0.1065871249927
# Node	65	8.8073477747765	6.81818	0.0532935624963502
# Node	66	9.09091	6.81818	3.0278890506E-16
# //Yarn 3
# Node	67	2.27273	0	0
# Node	68	2.27273	0.2835622252237	-0.05329356249635
# Node	69	2.27273	0.5671244504474	-0.1065871249927
# Node	70	2.27273	0.8503341952247	-0.1670006134745
# Node	71	2.27273	1.133543940002	-0.2274141019563
# Node	72	2.27273	1.417458641122	-0.2735878303818
# Node	73	2.27273	1.701373342242	-0.3197615588073
# Node	74	2.27273	1.987050436493	-0.3303358411347
# Node	75	2.27273	2.272727530744	-0.3409101234621
# Node	76	2.27273	2.55866899577	-0.3168474138206
# Node	77	2.27273	2.844610460796	-0.2927847041791
# Node	78	2.27273	3.1289657560775	-0.25282108957355
# Node	79	2.27273	3.413321051359	-0.212857474968
# Node	80	2.27273	3.6966189001435	-0.1622932570533
# Node	81	2.27273	3.979916748928	-0.1117290391386
# Node	82	2.27273	4.262685874464	-0.0558645195693001
# Node	83	2.27273	4.545455	-1.873501354055E-16
# Node	84	2.27273	4.828224125536	0.0558645195692999
# Node	85	2.27273	5.110993251072	0.1117290391386
# Node	86	2.27273	5.3942910998565	0.1622932570533
# Node	87	2.27273	5.677588948641	0.212857474968
# Node	88	2.27273	5.9619442439225	0.25282108957355
# Node	89	2.27273	6.246299539204	0.2927847041791
# Node	90	2.27273	6.53224100423	0.3168474138206
# Node	91	2.27273	6.818182469256	0.3409101234621
# Node	92	2.27273	7.103859563507	0.3303358411347
# Node	93	2.27273	7.389536657758	0.3197615588073
# Node	94	2.27273	7.673451358878	0.2735878303818
# Node	95	2.27273	7.957366059998	0.2274141019563
# Node	96	2.27273	8.2405758047755	0.1670006134745
# Node	97	2.27273	8.523785549553	0.1065871249927
# Node	98	2.27273	8.8073477747765	0.0532935624963502
# Node	99	2.27273	9.09091	3.0278890506E-16
# //Yarn 4
# Node	100	6.81818	0	0
# Node	101	6.81818	0.2835622252237	0.05329356249635
# Node	102	6.81818	0.5671244504474	0.1065871249927
# Node	103	6.81818	0.8503341952247	0.1670006134745
# Node	104	6.81818	1.133543940002	0.2274141019563
# Node	105	6.81818	1.417458641122	0.2735878303818
# Node	106	6.81818	1.701373342242	0.3197615588073
# Node	107	6.81818	1.987050436493	0.3303358411347
# Node	108	6.81818	2.272727530744	0.3409101234621
# Node	109	6.81818	2.55866899577	0.3168474138206
# Node	110	6.81818	2.844610460796	0.2927847041791
# Node	111	6.81818	3.1289657560775	0.25282108957355
# Node	112	6.81818	3.413321051359	0.212857474968
# Node	113	6.81818	3.6966189001435	0.1622932570533
# Node	114	6.81818	3.979916748928	0.1117290391386
# Node	115	6.81818	4.262685874464	0.0558645195693001
# Node	116	6.81818	4.545455	1.873501354055E-16
# Node	117	6.81818	4.828224125536	-0.0558645195692999
# Node	118	6.81818	5.110993251072	-0.1117290391386
# Node	119	6.81818	5.3942910998565	-0.1622932570533
# Node	120	6.81818	5.677588948641	-0.212857474968
# Node	121	6.81818	5.9619442439225	-0.25282108957355
# Node	122	6.81818	6.246299539204	-0.2927847041791
# Node	123	6.81818	6.53224100423	-0.3168474138206
# Node	124	6.81818	6.818182469256	-0.3409101234621
# Node	125	6.81818	7.103859563507	-0.3303358411347
# Node	126	6.81818	7.389536657758	-0.3197615588073
# Node	127	6.81818	7.673451358878	-0.2735878303818
# Node	128	6.81818	7.957366059998	-0.2274141019563
# Node	129	6.81818	8.2405758047755	-0.1670006134745
# Node	130	6.81818	8.523785549553	-0.1065871249927
# Node	131	6.81818	8.8073477747765	-0.0532935624963502
# Node	132	6.81818	9.09091	-3.0278890506E-16

# Elements	64
# //Yarn 1
# Beam_1	1   Mat 1   Sec 1   CS 1	Nodes	1	2	3
# Beam_1	2   Mat 1   Sec 1   CS 2	Nodes	3	4	5
# Beam_1	3   Mat 1   Sec 1   CS 3	Nodes	5	6	7
# Beam_1	4   Mat 1   Sec 1   CS 4	Nodes	7	8	9
# Beam_1	5   Mat 1   Sec 1   CS 5	Nodes	9	10	11
# Beam_1	6   Mat 1   Sec 1   CS 6	Nodes	11	12	13
# Beam_1	7   Mat 1   Sec 1   CS 7	Nodes	13	14	15
# Beam_1	8   Mat 1   Sec 1   CS 8	Nodes	15	16	17
# Beam_1	9   Mat 1   Sec 1   CS 9	Nodes	17	18	19
# Beam_1	10   Mat 1   Sec 1   CS 10	Nodes	19	20	21
# Beam_1	11   Mat 1   Sec 1   CS 11	Nodes	21	22	23
# Beam_1	12   Mat 1   Sec 1   CS 12	Nodes	23	24	25
# Beam_1	13   Mat 1   Sec 1   CS 13	Nodes	25	26	27
# Beam_1	14   Mat 1   Sec 1   CS 14	Nodes	27	28	29
# Beam_1	15   Mat 1   Sec 1   CS 15	Nodes	29	30	31
# Beam_1	16   Mat 1   Sec 1   CS 16	Nodes	31	32	33
# //Yarn 2
# Beam_1	17   Mat 1   Sec 1   CS 17	Nodes	34	35	36
# Beam_1	18   Mat 1   Sec 1   CS 18	Nodes	36	37	38
# Beam_1	19   Mat 1   Sec 1   CS 19	Nodes	38	39	40
# Beam_1	20   Mat 1   Sec 1   CS 20	Nodes	40	41	42
# Beam_1	21   Mat 1   Sec 1   CS 21	Nodes	42	43	44
# Beam_1	22   Mat 1   Sec 1   CS 22	Nodes	44	45	46
# Beam_1	23   Mat 1   Sec 1   CS 23	Nodes	46	47	48
# Beam_1	24   Mat 1   Sec 1   CS 24	Nodes	48	49	50
# Beam_1	25   Mat 1   Sec 1   CS 25	Nodes	50	51	52
# Beam_1	26   Mat 1   Sec 1   CS 26	Nodes	52	53	54
# Beam_1	27   Mat 1   Sec 1   CS 27	Nodes	54	55	56
# Beam_1	28   Mat 1   Sec 1   CS 28	Nodes	56	57	58
# Beam_1	29   Mat 1   Sec 1   CS 29	Nodes	58	59	60
# Beam_1	30   Mat 1   Sec 1   CS 30	Nodes	60	61	62
# Beam_1	31   Mat 1   Sec 1   CS 31	Nodes	62	63	64
# Beam_1	32   Mat 1   Sec 1   CS 32	Nodes	64	65	66
# //Yarn 3
# Beam_1	33   Mat 1   Sec 1   CS 33	Nodes	67	68	69
# Beam_1	34   Mat 1   Sec 1   CS 34	Nodes	69	70	71
# Beam_1	35   Mat 1   Sec 1   CS 35	Nodes	71	72	73
# Beam_1	36   Mat 1   Sec 1   CS 36	Nodes	73	74	75
# Beam_1	37   Mat 1   Sec 1   CS 37	Nodes	75	76	77
# Beam_1	38   Mat 1   Sec 1   CS 38	Nodes	77	78	79
# Beam_1	39   Mat 1   Sec 1   CS 39	Nodes	79	80	81
# Beam_1	40   Mat 1   Sec 1   CS 40	Nodes	81	82	83
# Beam_1	41   Mat 1   Sec 1   CS 41	Nodes	83	84	85
# Beam_1	42   Mat 1   Sec 1   CS 42	Nodes	85	86	87
# Beam_1	43   Mat 1   Sec 1   CS 43	Nodes	87	88	89
# Beam_1	44   Mat 1   Sec 1   CS 44	Nodes	89	90	91
# Beam_1	45   Mat 1   Sec 1   CS 45	Nodes	91	92	93
# Beam_1	46   Mat 1   Sec 1   CS 46	Nodes	93	94	95
# Beam_1	47   Mat 1   Sec 1   CS 47	Nodes	95	96	97
# Beam_1	48   Mat 1   Sec 1   CS 48	Nodes	97	98	99
# //Yarn 4
# Beam_1	49   Mat 1   Sec 1   CS 49	Nodes	100	101	102
# Beam_1	50   Mat 1   Sec 1   CS 50	Nodes	102	103	104
# Beam_1	51   Mat 1   Sec 1   CS 51	Nodes	104	105	106
# Beam_1	52   Mat 1   Sec 1   CS 52	Nodes	106	107	108
# Beam_1	53   Mat 1   Sec 1   CS 53	Nodes	108	109	110
# Beam_1	54   Mat 1   Sec 1   CS 54	Nodes	110	111	112
# Beam_1	55   Mat 1   Sec 1   CS 55	Nodes	112	113	114
# Beam_1	56   Mat 1   Sec 1   CS 56	Nodes	114	115	116
# Beam_1	57   Mat 1   Sec 1   CS 57	Nodes	116	117	118
# Beam_1	58   Mat 1   Sec 1   CS 58	Nodes	118	119	120
# Beam_1	59   Mat 1   Sec 1   CS 59	Nodes	120	121	122
# Beam_1	60   Mat 1   Sec 1   CS 60	Nodes	122	123	124
# Beam_1	61   Mat 1   Sec 1   CS 61	Nodes	124	125	126
# Beam_1	62   Mat 1   Sec 1   CS 62	Nodes	126	127	128
# Beam_1	63   Mat 1   Sec 1   CS 63	Nodes	128	129	130
# Beam_1	64   Mat 1   Sec 1   CS 64	Nodes	130	131	132

# CoordinateSystems	125
# //Yarn 1
# CS	1	E1	0	1	0	E3	0.982793219017874	0	0.184709200237791
# CS	2	E1	0	1	0	E3	0.977996070827189	0	0.208623309931035
# CS	3	E1	0	1	0	E3	0.987032037202101	0	0.160523386260914
# CS	4	E1	0	1	0	E3	0.999315655188056	0	0.0369894754770393
# CS	5	E1	0	1	0	E3	0.996477868228675	0	-0.0838561752671556
# CS	6	E1	0	1	0	E3	0.990268028399176	0	-0.139173388010817
# CS	7	E1	0	1	0	E3	0.984442415488383	0	-0.175707514316825
# CS	8	E1	0	1	0	E3	0.981037878224383	0	-0.193816102243854
# CS	9	E1	0	1	0	E3	0.981037878224383	0	-0.193816102243854
# CS	10	E1	0	1	0	E3	0.984442415488383	0	-0.175707514316825
# CS	11	E1	0	1	0	E3	0.990268028399176	0	-0.139173388010816
# CS	12	E1	0	1	0	E3	0.996477868228675	0	-0.0838561752671556
# CS	13	E1	0	1	0	E3	0.999315655188056	0	0.0369894754770392
# CS	14	E1	0	1	0	E3	0.987032037202101	0	0.160523386260914
# CS	15	E1	0	1	0	E3	0.977996070827219	0	0.208623309930894
# CS	16	E1	0	1	0	E3	0.982793219017851	0	0.184709200237917
# //Yarn 2
# CS	17	E1	0	1	0	E3	0.982793219017874	0	-0.184709200237791
# CS	18	E1	0	1	0	E3	0.977996070827189	0	-0.208623309931035
# CS	19	E1	0	1	0	E3	0.987032037202101	0	-0.160523386260914
# CS	20	E1	0	1	0	E3	0.999315655188056	0	-0.0369894754770393
# CS	21	E1	0	1	0	E3	0.996477868228675	0	0.0838561752671556
# CS	22	E1	0	1	0	E3	0.990268028399176	0	0.139173388010817
# CS	23	E1	0	1	0	E3	0.984442415488383	0	0.175707514316825
# CS	24	E1	0	1	0	E3	0.981037878224383	0	0.193816102243854
# CS	25	E1	0	1	0	E3	0.981037878224383	0	0.193816102243854
# CS	26	E1	0	1	0	E3	0.984442415488383	0	0.175707514316825
# CS	27	E1	0	1	0	E3	0.990268028399176	0	0.139173388010816
# CS	28	E1	0	1	0	E3	0.996477868228675	0	0.0838561752671556
# CS	29	E1	0	1	0	E3	0.999315655188056	0	-0.0369894754770392
# CS	30	E1	0	1	0	E3	0.987032037202101	0	-0.160523386260914
# CS	31	E1	0	1	0	E3	0.977996070827219	0	-0.208623309930894
# CS	32	E1	0	1	0	E3	0.982793219017851	0	-0.184709200237917
# //Yarn 3
# CS	33	E1	1	0	0	E3	0	0.982793219017874	-0.184709200237791
# CS	34	E1	1	0	0	E3	0	0.977996070827189	-0.208623309931035
# CS	35	E1	1	0	0	E3	0	0.987032037202101	-0.160523386260914
# CS	36	E1	1	0	0	E3	0	0.999315655188056	-0.0369894754770393
# CS	37	E1	1	0	0	E3	0	0.996477868228675	0.0838561752671556
# CS	38	E1	1	0	0	E3	0	0.990268028399176	0.139173388010817
# CS	39	E1	1	0	0	E3	0	0.984442415488383	0.175707514316825
# CS	40	E1	1	0	0	E3	0	0.981037878224383	0.193816102243854
# CS	41	E1	1	0	0	E3	0	0.981037878224383	0.193816102243854
# CS	42	E1	1	0	0	E3	0	0.984442415488383	0.175707514316825
# CS	43	E1	1	0	0	E3	0	0.990268028399176	0.139173388010816
# CS	44	E1	1	0	0	E3	0	0.996477868228675	0.0838561752671556
# CS	45	E1	1	0	0	E3	0	0.999315655188056	-0.0369894754770392
# CS	46	E1	1	0	0	E3	0	0.987032037202101	-0.160523386260914
# CS	47	E1	1	0	0	E3	0	0.977996070827219	-0.208623309930894
# CS	48	E1	1	0	0	E3	0	0.982793219017851	-0.184709200237917
# //Yarn 4
# CS	49	E1	1	0	0	E3	0	0.982793219017874	0.184709200237791
# CS	50	E1	1	0	0	E3	0	0.977996070827189	0.208623309931035
# CS	51	E1	1	0	0	E3	0	0.987032037202101	0.160523386260914
# CS	52	E1	1	0	0	E3	0	0.999315655188056	0.0369894754770393
# CS	53	E1	1	0	0	E3	0	0.996477868228675	-0.0838561752671556
# CS	54	E1	1	0	0	E3	0	0.990268028399176	-0.139173388010817
# CS	55	E1	1	0	0	E3	0	0.984442415488383	-0.175707514316825
# CS	56	E1	1	0	0	E3	0	0.981037878224383	-0.193816102243854
# CS	57	E1	1	0	0	E3	0	0.981037878224383	-0.193816102243854
# CS	58	E1	1	0	0	E3	0	0.984442415488383	-0.175707514316825
# CS	59	E1	1	0	0	E3	0	0.990268028399176	-0.139173388010816
# CS	60	E1	1	0	0	E3	0	0.996477868228675	-0.0838561752671556
# CS	61	E1	1	0	0	E3	0	0.999315655188056	0.0369894754770392
# CS	62	E1	1	0	0	E3	0	0.987032037202101	0.160523386260914
# CS	63	E1	1	0	0	E3	0	0.977996070827219	0.208623309930894
# CS	64	E1	1	0	0	E3	0	0.982793219017851	0.184709200237917
# //Coordinate Systems for Surfaces
# //Yarn 1
# CS	65	E1	0	1	0	E3	0.982182391196423	0	0.197047611979498
# CS	66	E1	0	1	0	E3	0.979213268586057	0	0.18403653344929
# CS	67	E1	0	1	0	E3	0.990095525065849	0	0.0986424874084407
# CS	68	E1	0	1	0	E3	0.999778047622641	0	-0.023591664942873
# CS	69	E1	0	1	0	E3	0.993714045490506	0	-0.111562719821725
# CS	70	E1	0	1	0	E3	0.988426748361318	0	-0.157631701805187
# CS	71	E1	0	1	0	E3	0.983523775276127	0	-0.184916623715394
# CS	72	E1	0	1	0	E3	0.981037878224384	0	-0.193816102243854
# CS	73	E1	0	1	0	E3	0.981955053203958	0	-0.184621681390231
# CS	74	E1	0	1	0	E3	0.986279695912897	0	-0.157289295519774
# CS	75	E1	0	1	0	E3	0.99302994845422	0	-0.111485917318694
# CS	76	E1	0	1	0	E3	0.996017215160625	0	-0.0235029209465819
# CS	77	E1	0	1	0	E3	0.996233176610237	0	0.0992539771080274
# CS	78	E1	0	1	0	E3	0.98580664363824	0	0.185275713847675
# CS	79	E1	0	1	0	E3	0.978604673634126	0	0.196329842338842
# //Yarn 2
# CS	80	E1	0	1	0	E3	0.982182391196423	0	-0.197047611979498
# CS	81	E1	0	1	0	E3	0.979213268586057	0	-0.18403653344929
# CS	82	E1	0	1	0	E3	0.990095525065849	0	-0.0986424874084407
# CS	83	E1	0	1	0	E3	0.999778047622641	0	0.023591664942873
# CS	84	E1	0	1	0	E3	0.993714045490506	0	0.111562719821725
# CS	85	E1	0	1	0	E3	0.988426748361318	0	0.157631701805187
# CS	86	E1	0	1	0	E3	0.983523775276127	0	0.184916623715394
# CS	87	E1	0	1	0	E3	0.981037878224384	0	0.193816102243854
# CS	88	E1	0	1	0	E3	0.981955053203958	0	0.184621681390231
# CS	89	E1	0	1	0	E3	0.986279695912897	0	0.157289295519774
# CS	90	E1	0	1	0	E3	0.99302994845422	0	0.111485917318694
# CS	91	E1	0	1	0	E3	0.996017215160625	0	0.0235029209465819
# CS	92	E1	0	1	0	E3	0.996233176610237	0	-0.0992539771080274
# CS	93	E1	0	1	0	E3	0.98580664363824	0	-0.185275713847675
# CS	94	E1	0	1	0	E3	0.978604673634126	0	-0.196329842338842
# //Yarn 3
# CS	95	E1	1	0	0	E3	0	0.982182391196423	-0.197047611979498
# CS	96	E1	1	0	0	E3	0	0.979213268586057	-0.18403653344929
# CS	97	E1	1	0	0	E3	0	0.990095525065849	-0.0986424874084407
# CS	98	E1	1	0	0	E3	0	0.999778047622641	0.023591664942873
# CS	99	E1	1	0	0	E3	0	0.993714045490506	0.111562719821725
# CS	100	E1	1	0	0	E3	0	0.988426748361318	0.157631701805187
# CS	101	E1	1	0	0	E3	0	0.983523775276127	0.184916623715394
# CS	102	E1	1	0	0	E3	0	0.981037878224384	0.193816102243854
# CS	103	E1	1	0	0	E3	0	0.981955053203958	0.184621681390231
# CS	104	E1	1	0	0	E3	0	0.986279695912897	0.157289295519774
# CS	105	E1	1	0	0	E3	0	0.99302994845422	0.111485917318694
# CS	106	E1	1	0	0	E3	0	0.996017215160625	0.0235029209465819
# CS	107	E1	1	0	0	E3	0	0.996233176610237	-0.0992539771080274
# CS	108	E1	1	0	0	E3	0	0.98580664363824	-0.185275713847675
# CS	109	E1	1	0	0	E3	0	0.978604673634126	-0.196329842338842
# //Yarn 4
# CS	110	E1	1	0	0	E3	0	0.982182391196423	0.197047611979498
# CS	111	E1	1	0	0	E3	0	0.979213268586057	0.18403653344929
# CS	112	E1	1	0	0	E3	0	0.990095525065849	0.0986424874084407
# CS	113	E1	1	0	0	E3	0	0.999778047622641	-0.023591664942873
# CS	114	E1	1	0	0	E3	0	0.993714045490506	-0.111562719821725
# CS	115	E1	1	0	0	E3	0	0.988426748361318	-0.157631701805187
# CS	116	E1	1	0	0	E3	0	0.983523775276127	-0.184916623715394
# CS	117	E1	1	0	0	E3	0	0.981037878224384	-0.193816102243854
# CS	118	E1	1	0	0	E3	0	0.981955053203958	-0.184621681390231
# CS	119	E1	1	0	0	E3	0	0.986279695912897	-0.157289295519774
# CS	120	E1	1	0	0	E3	0	0.99302994845422	-0.111485917318694
# CS	121	E1	1	0	0	E3	0	0.996017215160625	-0.0235029209465819
# CS	122	E1	1	0	0	E3	0	0.996233176610237	0.0992539771080274
# CS	123	E1	1	0	0	E3	0	0.98580664363824	0.185275713847675
# CS	124	E1	1	0	0	E3	0	0.978604673634126	0.196329842338842
# CS	125	E1	1	0	0	E3	0	0	1

# Surfaces	64
# //Yarn 1
# FlexibleSECylinder_1	1	A    1.13636 B   0.28409    N   2   CSA	1   CSB	65	NormalExterior  Nodes	1	3
# FlexibleSECylinder_1	2	A    1.13636 B   0.28409    N   2   CSA	65   CSB	66	NormalExterior  Nodes	3	5
# FlexibleSECylinder_1	3	A    1.13636 B   0.28409    N   2   CSA	66   CSB	67	NormalExterior  Nodes	5	7
# FlexibleSECylinder_1	4	A    1.13636 B   0.28409    N   2   CSA	67   CSB	68	NormalExterior  Nodes	7	9
# FlexibleSECylinder_1	5	A    1.13636 B   0.28409    N   2   CSA	68   CSB	69	NormalExterior  Nodes	9	11
# FlexibleSECylinder_1	6	A    1.13636 B   0.28409    N   2   CSA	69   CSB	70	NormalExterior  Nodes	11	13
# FlexibleSECylinder_1	7	A    1.13636 B   0.28409    N   2   CSA	70   CSB	71	NormalExterior  Nodes	13	15
# FlexibleSECylinder_1	8	A    1.13636 B   0.28409    N   2   CSA	71   CSB	72	NormalExterior  Nodes	15	17
# FlexibleSECylinder_1	9	A    1.13636 B   0.28409    N   2   CSA	72   CSB	73	NormalExterior  Nodes	17	19
# FlexibleSECylinder_1	10	A    1.13636 B   0.28409    N   2   CSA	73   CSB	74	NormalExterior  Nodes	19	21
# FlexibleSECylinder_1	11	A    1.13636 B   0.28409    N   2   CSA	74   CSB	75	NormalExterior  Nodes	21	23
# FlexibleSECylinder_1	12	A    1.13636 B   0.28409    N   2   CSA	75   CSB	76	NormalExterior  Nodes	23	25
# FlexibleSECylinder_1	13	A    1.13636 B   0.28409    N   2   CSA	76   CSB	77	NormalExterior  Nodes	25	27
# FlexibleSECylinder_1	14	A    1.13636 B   0.28409    N   2   CSA	77   CSB	78	NormalExterior  Nodes	27	29
# FlexibleSECylinder_1	15	A    1.13636 B   0.28409    N   2   CSA	78   CSB	79	NormalExterior  Nodes	29	31
# FlexibleSECylinder_1	16	A    1.13636 B   0.28409    N   2   CSA	79   CSB	16	NormalExterior  Nodes	31	33
# //Yarn 2
# FlexibleSECylinder_1	17	A    1.13636 B   0.28409    N   2   CSA	17   CSB	80	NormalExterior  Nodes	34	36
# FlexibleSECylinder_1	18	A    1.13636 B   0.28409    N   2   CSA	80   CSB	81	NormalExterior  Nodes	36	38
# FlexibleSECylinder_1	19	A    1.13636 B   0.28409    N   2   CSA	81   CSB	82	NormalExterior  Nodes	38	40
# FlexibleSECylinder_1	20	A    1.13636 B   0.28409    N   2   CSA	82   CSB	83	NormalExterior  Nodes	40	42
# FlexibleSECylinder_1	21	A    1.13636 B   0.28409    N   2   CSA	83   CSB	84	NormalExterior  Nodes	42	44
# FlexibleSECylinder_1	22	A    1.13636 B   0.28409    N   2   CSA	84   CSB	85	NormalExterior  Nodes	44	46
# FlexibleSECylinder_1	23	A    1.13636 B   0.28409    N   2   CSA	85   CSB	86	NormalExterior  Nodes	46	48
# FlexibleSECylinder_1	24	A    1.13636 B   0.28409    N   2   CSA	86   CSB	87	NormalExterior  Nodes	48	50
# FlexibleSECylinder_1	25	A    1.13636 B   0.28409    N   2   CSA	87   CSB	88	NormalExterior  Nodes	50	52
# FlexibleSECylinder_1	26	A    1.13636 B   0.28409    N   2   CSA	88   CSB	89	NormalExterior  Nodes	52	54
# FlexibleSECylinder_1	27	A    1.13636 B   0.28409    N   2   CSA	89   CSB	90	NormalExterior  Nodes	54	56
# FlexibleSECylinder_1	28	A    1.13636 B   0.28409    N   2   CSA	90   CSB	91	NormalExterior  Nodes	56	58
# FlexibleSECylinder_1	29	A    1.13636 B   0.28409    N   2   CSA	91   CSB	92	NormalExterior  Nodes	58	60
# FlexibleSECylinder_1	30	A    1.13636 B   0.28409    N   2   CSA	92   CSB	93	NormalExterior  Nodes	60	62
# FlexibleSECylinder_1	31	A    1.13636 B   0.28409    N   2   CSA	93   CSB	94	NormalExterior  Nodes	62	64
# FlexibleSECylinder_1	32	A    1.13636 B   0.28409    N   2   CSA	94   CSB	32	NormalExterior  Nodes	64	66
# //Yarn 3
# FlexibleSECylinder_1	33	A    1.13636 B   0.28409    N   2   CSA	33   CSB	95	NormalExterior  Nodes	67	69
# FlexibleSECylinder_1	34	A    1.13636 B   0.28409    N   2   CSA	95   CSB	96	NormalExterior  Nodes	69	71
# FlexibleSECylinder_1	35	A    1.13636 B   0.28409    N   2   CSA	96   CSB	97	NormalExterior  Nodes	71	73
# FlexibleSECylinder_1	36	A    1.13636 B   0.28409    N   2   CSA	97   CSB	98	NormalExterior  Nodes	73	75
# FlexibleSECylinder_1	37	A    1.13636 B   0.28409    N   2   CSA	98   CSB	99	NormalExterior  Nodes	75	77
# FlexibleSECylinder_1	38	A    1.13636 B   0.28409    N   2   CSA	99   CSB	100	NormalExterior  Nodes	77	79
# FlexibleSECylinder_1	39	A    1.13636 B   0.28409    N   2   CSA	100   CSB	101	NormalExterior  Nodes	79	81
# FlexibleSECylinder_1	40	A    1.13636 B   0.28409    N   2   CSA	101   CSB	102	NormalExterior  Nodes	81	83
# FlexibleSECylinder_1	41	A    1.13636 B   0.28409    N   2   CSA	102   CSB	103	NormalExterior  Nodes	83	85
# FlexibleSECylinder_1	42	A    1.13636 B   0.28409    N   2   CSA	103   CSB	104	NormalExterior  Nodes	85	87
# FlexibleSECylinder_1	43	A    1.13636 B   0.28409    N   2   CSA	104   CSB	105	NormalExterior  Nodes	87	89
# FlexibleSECylinder_1	44	A    1.13636 B   0.28409    N   2   CSA	105   CSB	106	NormalExterior  Nodes	89	91
# FlexibleSECylinder_1	45	A    1.13636 B   0.28409    N   2   CSA	106   CSB	107	NormalExterior  Nodes	91	93
# FlexibleSECylinder_1	46	A    1.13636 B   0.28409    N   2   CSA	107   CSB	108	NormalExterior  Nodes	93	95
# FlexibleSECylinder_1	47	A    1.13636 B   0.28409    N   2   CSA	108   CSB	109	NormalExterior  Nodes	95	97
# FlexibleSECylinder_1	48	A    1.13636 B   0.28409    N   2   CSA	109   CSB	48	NormalExterior  Nodes	97	99
# //Yarn 4
# FlexibleSECylinder_1	49	A    1.13636 B   0.28409    N   2   CSA	49   CSB	110	NormalExterior  Nodes	100	102
# FlexibleSECylinder_1	50	A    1.13636 B   0.28409    N   2   CSA	110   CSB	111	NormalExterior  Nodes	102	104
# FlexibleSECylinder_1	51	A    1.13636 B   0.28409    N   2   CSA	111   CSB	112	NormalExterior  Nodes	104	106
# FlexibleSECylinder_1	52	A    1.13636 B   0.28409    N   2   CSA	112   CSB	113	NormalExterior  Nodes	106	108
# FlexibleSECylinder_1	53	A    1.13636 B   0.28409    N   2   CSA	113   CSB	114	NormalExterior  Nodes	108	110
# FlexibleSECylinder_1	54	A    1.13636 B   0.28409    N   2   CSA	114   CSB	115	NormalExterior  Nodes	110	112
# FlexibleSECylinder_1	55	A    1.13636 B   0.28409    N   2   CSA	115   CSB	116	NormalExterior  Nodes	112	114
# FlexibleSECylinder_1	56	A    1.13636 B   0.28409    N   2   CSA	116   CSB	117	NormalExterior  Nodes	114	116
# FlexibleSECylinder_1	57	A    1.13636 B   0.28409    N   2   CSA	117   CSB	118	NormalExterior  Nodes	116	118
# FlexibleSECylinder_1	58	A    1.13636 B   0.28409    N   2   CSA	118   CSB	119	NormalExterior  Nodes	118	120
# FlexibleSECylinder_1	59	A    1.13636 B   0.28409    N   2   CSA	119   CSB	120	NormalExterior  Nodes	120	122
# FlexibleSECylinder_1	60	A    1.13636 B   0.28409    N   2   CSA	120   CSB	121	NormalExterior  Nodes	122	124
# FlexibleSECylinder_1	61	A    1.13636 B   0.28409    N   2   CSA	121   CSB	122	NormalExterior  Nodes	124	126
# FlexibleSECylinder_1	62	A    1.13636 B   0.28409    N   2   CSA	122   CSB	123	NormalExterior  Nodes	126	128
# FlexibleSECylinder_1	63	A    1.13636 B   0.28409    N   2   CSA	123   CSB	124	NormalExterior  Nodes	128	130
# FlexibleSECylinder_1	64	A    1.13636 B   0.28409    N   2   CSA	124   CSB	64	NormalExterior  Nodes	130	132

# SurfaceSets	4
# //Yarn 1
# SurfaceSet	1	Surfaces	16	List	 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# //Yarn 2
# SurfaceSet	2	Surfaces	16	List	 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
# //Yarn 3
# SurfaceSet	3	Surfaces	16	List	 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
# //Yarn 4
# SurfaceSet	4	Surfaces	16	List	 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64

# Contacts	4
# //Yarn 1
# SSSS	1	SurfaceSet1	1	SurfaceSet2	3	MU	0 EPN	3.5E5 CN 0  EPT 0 CT 0 Pinball 1 MaxPointwiseInt 1
# SSSS	2	SurfaceSet1	1	SurfaceSet2	4	MU	0 EPN	3.5E5 CN 0  EPT 0 CT 0 Pinball 1 MaxPointwiseInt 1
# //Yarn 2
# SSSS	3	SurfaceSet1	2	SurfaceSet2	3	MU	0 EPN	3.5E5 CN 0  EPT 0 CT 0 Pinball 1 MaxPointwiseInt 1
# SSSS	4	SurfaceSet1	2	SurfaceSet2	4	MU	0 EPN	3.5E5 CN 0  EPT 0 CT 0 Pinball 1 MaxPointwiseInt 1


# Materials 1
# Hooke 1 E 210E9 Nu 0.3 Rho 7800

# Sections 1
# UserDefined 1

# GA	1.5833333333E+07	
# EA	3.8000000000E+07	
# ES1	0	
# ES2	0	
# EI11	7.6672262397E+04	
# EI22	1.2267561983E+07	
# EI12	0	
# GS1	0	
# GS2	0	
# GS1S	0	
# GS2S	0	
# GJT	1.2027021552E+06	
# J11	5.1977206577E-08	
# J22	8.3163530523E-07	
# J12	0.0000000000E+00	
# A	1.0142021738E+00	
# SC	0	0
# BC	0	0
# Rho	2.5760735215E-06	
# SD	1	

# SectionDetails	1					
# SolidSection	1	AxisPosition	0	0	NPoints	21
# Point	1	1.136363636	0			
# Point	2	1.080746041	0.087788919			
# Point	3	0.919337494	0.166984447			
# Point	4	0.667937787	0.229834373			
# Point	5	0.351155675	0.27018651			
# Point	6	6.96107E-17	0.284090909			
# Point	7	-0.351155675	0.27018651			
# Point	8	-0.667937787	0.229834373			
# Point	9	-0.919337494	0.166984447			
# Point	10	-1.080746041	0.087788919			
# Point	11	-1.136363636	3.48054E-17			
# Point	12	-1.080746041	-0.087788919			
# Point	13	-0.919337494	-0.166984447			
# Point	14	-0.667937787	-0.229834373			
# Point	15	-0.351155675	-0.27018651			
# Point	16	-2.08832E-16	-0.284090909			
# Point	17	0.351155675	-0.27018651			
# Point	18	0.667937787	-0.229834373			
# Point	19	0.919337494	-0.166984447			
# Point	20	1.080746041	-0.087788919			
# Point	21	1.136363636	-6.96107E-17			

# NodeSets	12
# //left
# NodeSet	1	Nodes	2	List	1	34
# //right
# NodeSet	2	Nodes	2	List	33	66
# //bottom
# NodeSet 3	Nodes	2 	List 	67	100
# //top
# NodeSet 4	Nodes	2 	List 	99	132
# //left
# NodeSet 5	Nodes	1 	List 	1
# NodeSet 6	Nodes	1 	List 	34
# //right
# NodeSet 7	Nodes	1 	List 	33
# NodeSet 8	Nodes	1 	List 	66
# //bottom
# NodeSet 9	Nodes	1 	List 	67
# NodeSet 10	Nodes	1 	List 	100
# //top
# NodeSet 11	Nodes	1 	List 	99
# NodeSet 12	Nodes	1 	List 	132

# Constraints	4
# NodalConstraint	1	NodeSet	1
# 	UX		BoolTable	1
# 	UY		BoolTable	1 
# 	UZ		BoolTable	0 
# 	ROTX	BoolTable	0 
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0

# NodalConstraint	2	NodeSet	2
# 	UX		BoolTable	1 
# 	UY		BoolTable	1 
# 	UZ		BoolTable	0 
# 	ROTX	BoolTable	0 
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0
	
# NodalConstraint	3	NodeSet	3
# 	UX		BoolTable	1 
# 	UY		BoolTable	1
# 	UZ		BoolTable	0 
# 	ROTX	BoolTable	0
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0

# NodalConstraint	4	NodeSet	4
# 	UX		BoolTable	1 
# 	UY		BoolTable	1 
# 	UZ		BoolTable	0 
# 	ROTX	BoolTable	0 
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0\n\n """
 
 
 
# bottom = """ \n\n
# SpecialConstraints 8
# SameRotation 1 Nodes 1  33 BoolTable 1
# SameRotation 2 Nodes 34 66 BoolTable 1
# SameRotation 3 Nodes 67 99 BoolTable 1
# SameRotation 4 Nodes 100 132 BoolTable 1

# NodalConstraintDOF 5 Nodes 1  33 
# 	UX		BoolTable	0
# 	UY		BoolTable	0 
# 	UZ		BoolTable	1 
# 	ROTX	BoolTable	0 
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0
# NodalConstraintDOF 6 Nodes 34 66
# 	UX		BoolTable	0
# 	UY		BoolTable	0 
# 	UZ		BoolTable	1 
# 	ROTX	BoolTable	0 
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0
# NodalConstraintDOF 7 Nodes 67 99 
# 	UX		BoolTable	0
# 	UY		BoolTable	0 
# 	UZ		BoolTable	1 
# 	ROTX	BoolTable	0 
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0
# NodalConstraintDOF 8 Nodes 100 132
# 	UX		BoolTable	0
# 	UY		BoolTable	0 
# 	UZ		BoolTable	1 
# 	ROTX	BoolTable	0 
# 	ROTY	BoolTable	0	
# 	ROTZ	BoolTable	0

# SolutionSteps 1

# Dynamic 1
# EndTime 1
# TimeStep 0.001
# MaxTimeStep 0.02
# MinTimeStep 0.000001
# MaxIt 10
# MinIt 3
# ConvIncrease 4
# IncFactor 1.5
# Sample 1
# RayleighDamping Alpha 0.0 Beta 0.0 Update 0
# NewmarkCoefficients Beta 0.3 Gamma 0.5

# SolverOptions
# Processors 4 LinSys Direct

# Monitor Sample 1
# MonitorNodeSets 1 2 3 4

# PostFiles
# MagFactor 1
# WriteMesh 0
# WriteRenderMesh 1
# WriteRigidContactSurfaces 0
# WriteFlexibleContactSurfaces 1
# WriteForces 0
# WriteConstraints 0
# WriteSpecialConstraints 1
# WriteContactForces 1
# WriteRenderRigidBodies 0
# WriteRenderParticles 0 """


# giraffe_template = """
# ${top}

# Displacements ${num_nodes}

# ${disp_block}

# ${bottom}
# """

# t = string.Template(giraffe_template)

# # Substitute the placeholders in the template string with the appropriate values
# giraffe_input = t.substitute(top=top, bottom=bottom, num_nodes=num_nodes, disp_block=disp_block)


# # Open the file for writing

# filepath = 'Giraffe/' + inp + '/' + inp + '.inp'         # filepath - E:/Softwares/01/Giraffe/tex_0/tex_0.inp

# # Write the Giraffe input file to disk
# with open(filepath, 'w') as f:
#     f.write(giraffe_input)

#     # return inp, Lxx, Lyy, t, folder
    
# end_time = time.time() 
# # calculate the execution time
# execution_time = end_time - start_time
# print("Execution time:", execution_time, "seconds")  
    





########################

# Read files

##########################
start_time = time.time()

rr = rvetype  


# Create new folder with name of .inp file
inp = name + '_' + str(rr)                       # inp = tex_0
folder = "Giraffe/" + inp                              # folder = E:/Softwares/01/Giraffe/tex_0
os.makedirs("Giraffe/" + inp, exist_ok=True)               # Creates tex_0 folder

# Take inputs from text file and assign following variables 
with open("Giraffe/RVE_data/rve"+ str(rr)  +".txt", "r") as file:
    Lxx, Lyy, t, nx, ny = [float(x) for x in file.read().split()]
    nx = int(nx)
    ny = int(ny)

# Get the nodal coordinates of the ends of the beams

X = np.zeros(((nx + ny) * 2, 3))

# Read the nodedata text files from data folder
with open("Giraffe/RVE_data/nodedata" + str(rr)  + ".txt", "r") as file:
    for i, line in enumerate(file):
        X[i] = [float(x) for x in line.strip().split()]

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


# Read the top portion from grfTop{i}.txt
with open("Giraffe/RVE_data/grfTop" + str(rr)  + ".txt", "r") as top_file:
    top = top_file.read()

# Read the bottom portion from grfBottom{i}.txt
with open("Giraffe/RVE_data/grfBottom" + str(rr) + ".txt", "r") as bottom_file:
    bottom = bottom_file.read()


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


end_time = time.time() 
# calculate the execution time
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds") 