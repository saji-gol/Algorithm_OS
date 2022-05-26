import os


def Sort(ProcessList, ProcessName):

    Process = []
    ProcessN = str()
    counter = 0

    for P in ProcessList:
        c = 0
        for i in ProcessList:
            if counter > c:
                c += 1
                continue
            else:
                if P[0] > i[0]:
                    Process = ProcessList[counter]
                    ProcessN = ProcessName[counter]

                    ProcessList[counter] = ProcessList[c]
                    ProcessName[counter] = ProcessName[c]

                    ProcessList[c] = Process
                    ProcessName[c] = ProcessN
                    
                    P = ProcessList[counter]
                c += 1

        counter += 1

    return ProcessList, ProcessName


def Gantt_Chart(Name, ProcessInfo, CS):

    TurnIndex = int
    StartFinishProcess = []
    Line1 = str(f'|\t{Name[0]}\t|')
    Line3 = str(f'{ProcessInfo[0][0]}\t \t{ProcessInfo[0][0] + ProcessInfo[0][1]}')
    StartFinishProcess.append(
        [ProcessInfo[0][0], ProcessInfo[0][0] + ProcessInfo[0][1]])
    ProcessInfo[0][2] = 0
    counter = 1
    CurentTime = int(ProcessInfo[0][0] + ProcessInfo[0][1])

    while (1):
        if CS > 0:
            CurentTime += CS
            Line1 += str(f'\t|')
            Line3 += str(f'\t{CurentTime}')

        Result = ProcessTurn(ProcessInfo, CurentTime)
        TurnIndex = Result[0]
        MR = Result[1]

        if MR:
            n = ProcessInfo[TurnIndex][0] - CurentTime
            CurentTime += n
            Line1 += str(f'\t|')
            Line3 += str(f'\t{CurentTime}')

        Line1 += str(f'\t{Name[TurnIndex]}\t|')
        Line3 += str(f'\t\t{ProcessInfo[TurnIndex][1] + CurentTime}')

        StartFinish = [int(CurentTime), int(
            CurentTime+ProcessInfo[TurnIndex][1])]
        StartFinishProcess.insert(TurnIndex, StartFinish)

        CurentTime += int(ProcessInfo[TurnIndex][1])
        ProcessInfo[TurnIndex][2] = 0

        counter += 1
        if counter == len(Name):
            break

    print('\nGantt : \n', Line1, '\n', Line3)
    ART(StartFinishProcess, ProcessInfo)
    AWT(StartFinishProcess, ProcessInfo)
    return 0


def ProcessTurn(ProcessInfo, CT):
    MinIndex = int
    c = int(0)
    MultiR = False
    QualifiedProcces = 0

    for i in ProcessInfo:
        if(i[2] > 0 and i[0] <= CT):
            QualifiedProcces += 1

    if QualifiedProcces > 0:
        for x in ProcessInfo:
            if (x[2] > 0 and x[0] <= CT):
                break
            c += 1

        MinIndex = c
        c = 0
        for process in ProcessInfo:
            if (process[2] > 0 and process[0] <= CT):
                if process[2] <= ProcessInfo[MinIndex][2]:
                    MinIndex = c
            c += 1
    else:
        x = 0
        MinIndex = -1
        for i in ProcessInfo:
            if i[2] > 0:
                if MinIndex != -1:
                    if i[2] > 0 and i[2] < ProcessInfo[MinIndex][2]:
                        MinIndex = x
                else:
                    MinIndex = x
                    MultiR = True
            x += 1

    return MinIndex, MultiR


def ART(SF, PI):
    Sum = int(0)
    AvrageRT = float
    c = int(0)

    print('\n')
    for process in SF:
        Sum += process[1]-PI[c][0]
        print(f'RT : {process[1]} - {PI[c][0]} = {process[1]-PI[c][0]}')
        c += 1
    AvrageRT = float(Sum/len(PI))
    print(f'\n\tAvrage Respons Time = {AvrageRT}')


def AWT(SF, PI):
    Sum = int(0)
    RT = int(0)
    AvrageWT = float
    c = int(0)
    for process in SF:
        RT += process[1]-PI[c][0]
        c += 1
    for process in PI:
        Sum += process[1]
    print(f'\nWT : {RT} - {Sum} = {RT-Sum}')
    print(f'AWT : {RT-Sum} / {len(PI)} = {(RT-Sum)/len(PI)}')
    RT -= Sum
    AvrageWT = float(RT/len(PI))
    print(f'\n\tAvrage Wait Time = {AvrageWT}')


Process = []
ProcessName = []
WS = 0
cs = int(0)

os.system('cls')
A = int(input('''Default(1)
Custom(2)
'''))

if A == 2:
    os.system('cls')

    while(WS == 0):

        print('Enter Process Name A-Z (end = 0 - restart = 1) = ', end='')
        name = input()

        if(name == '1'):
            os.system('py .\RoundRobin_Algorithm.py')

        while(name != '0'):
            ProcessName.append(name)
            name = []
            AT = input('Enter Arival Time = ')
            CBT = input('Enter Execute Time = ')
            Remaining = CBT
            name.append(int(AT))
            name.append(int(CBT))
            name.append(int(Remaining))
            Process.append(name)
            break
        else:
            WS = 1

    else:
        cs = int(input("Contect Switch = "))

elif A == 1:

    ListProcess = [
        [['A', 'B', 'C', 'D'], [[0, 2, 2], [3, 4, 4], [3, 1, 1], [4, 2, 2]], [0]],
        [['A', 'B', 'C', 'D'], [[1, 1, 1], [2, 3, 3], [3, 2, 2], [5, 4, 4]], [0]],
        [['A', 'B', 'C', 'D'], [[0, 8, 8], [1, 3, 3], [2, 2, 2], [2, 1, 1]], [2]]
    ]

    os.system("cls")

    c = 1
    for items in ListProcess:
        i = 0

        print(f'Item{c} (CODE {c})')
        while i < len(items[0]):
            print(f'\t{items[0][i]} -> {items[1][i][0:2]}')
            i += 1
        print(f'\n\tCS = {items[2][0]}\n')
        c += 1

    n = int(input("Enter One Code (Example: 1): "))
    os.system("cls")

    if n == 1:
        ProcessName = ListProcess[0][0]
        Process = ListProcess[0][1]
        cs = ListProcess[0][2][0]
    elif n == 2:
        ProcessName = ListProcess[1][0]
        Process = ListProcess[1][1]
        cs = ListProcess[1][2][0]
    elif n == 3:
        ProcessName = ListProcess[2][0]
        Process = ListProcess[2][1]
        cs = ListProcess[2][2][0]


ret = Sort(Process, ProcessName)
Process = ret[0]
ProcessName = ret[1]

os.system('cls')

counter = 0
print('Process :')
for x in ProcessName:
    print(x, "-> ", end='')
    print(Process[counter][0:2])
    counter += 1

Gantt_Chart(ProcessName, Process, cs)

Exit = input('''
Exit(0)
Restart(1)
''')
if int(Exit) == 1:
    os.system('cls')
    os.system('py .\SJF_Algorithm.py')