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


def Gantt_Chart(Name, ProcessInfo, TS, CS):

    StartFinishProcess = {}
    TurnList = []
    FirstList = 0
    # EndList = -1
    CurentTime = 0
    LastCurentTime = 0
    
    CurentTime = ProcessInfo[0][0]
    Line1 = str(f'|*{CurentTime}*|')
    
    c = 0
    for temp in ProcessInfo:
        if temp[0] <= CurentTime and temp[2] > 0:
            TurnList.append(Name[c])
            # EndList+=1
        c += 1
    LastCurentTime = CurentTime

    while(EndProcces(ProcessInfo)):

        index = Name.index(TurnList[FirstList])
        if Name[index] not in StartFinishProcess:
            StartFinishProcess[Name[index]] = [CurentTime, 0]
        FirstList += 1

        if ProcessInfo[index][0] > CurentTime:
            CurentTime = ProcessInfo[index][0]
            Line1 += str(f'    |*{CurentTime}*|')

        if ProcessInfo[index][2] > TS:
            CurentTime += TS
        else:
            CurentTime += ProcessInfo[index][2]

        ProcessInfo[index][2] -= TS
        if ProcessInfo[index][2] <= 0:
            StartFinishProcess[Name[index]][1] = CurentTime
        
        Line1 += str(f'    {Name[index]}    |*{CurentTime}*|')

        c = 0
        for temp in ProcessInfo:
            if temp[0] <= CurentTime and temp[0] > LastCurentTime and temp[2] > 0:
                TurnList.append(Name[c])
                # EndList+=1
            c += 1
        LastCurentTime = CurentTime
        
        if ProcessInfo[index][2] > 0:
            TurnList.append(Name[index])
            # EndList+=1
        
        if CS > 0:
            CurentTime += CS
            Line1 += str(f'    CS    |*{CurentTime}*|')

    print('\nGantt : \n\n', Line1, '\n')
    ART(StartFinishProcess, ProcessInfo)
        

def EndProcces(ProcessInfo):
    for item in ProcessInfo:
        if item[2] > 0:
            return True
    return False


def ART(SF, PI):

    RTandBTS = {}
    RT = 0
    sumRT = 0
    ART = 0
    c = 0

    for item in SF:
        RT = SF[item][1] - PI[c][0]
        print(f'RT{item} : {SF[item][1]} - {PI[c][0]} = {RT}')
        sumRT += RT
        RTandBTS[item] = [RT, PI[c][1]]
        c += 1
    ART = sumRT / c
    print(f'\n\tART : {sumRT} / {c} = {ART}\n')
    AWT(RTandBTS)


def AWT(FE):
    WT = 0
    AWT = 0
    c = 0
    sumWT = 0

    for item in FE:
        WT = FE[item][0] - FE[item][1]
        print(f'WT{item} : {FE[item][0]} - {FE[item][1]} = {WT}')
        sumWT += WT
        c += 1
    AWT = sumWT / c
    print(f'\n\tAWT : {sumWT} / {c} = {AWT}')


Process = []
ProcessName = []
WS = 0
cs = int(0)
ts = int(0)

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
        ts = int(input("Time Slice = "))
elif A == 1:
    # ProcessName = ['a', 'b']
    # Process = [[0, 3, 3], [4, 2, 2]]
    
    # ProcessName = ['a', 'b', 'c', 'd']
    # Process = [[0, 3, 3], [2, 2, 2], [2, 2, 2], [5, 2, 2]]

    # ProcessName = ['C', 'B', 'A', 'D']
    # Process = [[2, 2, 2], [1, 3, 3], [0, 8, 8], [2, 1, 1]]

    # ProcessName = ['A', 'B', 'C', 'D', 'E']
    # Process = [[1, 12, 12], [2, 8, 8], [3, 3, 3], [4, 5, 5], [5, 7, 7]]

    # ProcessName = ['A', 'B', 'C', 'D', 'E']
    # Process = [[0, 3, 3], [2, 6, 6], [4, 4, 4], [6, 5, 5], [8, 2, 2]]

    ListProcess = [
        # [['A', 'B'],[[0, 3, 3], [4, 2, 2]], [2], [0]],
        [['A', 'B', 'C', 'D'], [[0, 3, 3], [2, 2, 2], [2, 2, 2], [5, 2, 2]], [1], [0]],
        [['C', 'B', 'A', 'D'], [[1, 8, 8], [2, 6, 6], [3, 7, 7], [4, 1, 1]], [4], [0]],
        [['C', 'B', 'A', 'D'], [[0, 40, 40], [0, 20, 20], [0, 50, 50], [0, 30, 30]], [20], [5]],
        [['A', 'B', 'C', 'D', 'E'], [[1, 12, 12], [2, 8, 8], [3, 3, 3], [4, 5, 5], [5, 7, 7]], [5], [0]],
        [['A', 'B', 'C', 'D', 'E'], [[1, 12, 12], [2, 8, 8], [3, 3, 3], [4, 5, 5], [7, 7, 7]], [5], [0]],
        [['A', 'B', 'C', 'D', 'E'], [[0, 3, 3], [2, 6, 6], [4, 4, 4], [6, 5, 5], [8, 2, 2]], [1], [0]]
    ]
    os.system("cls")
    c = 1
    for items in ListProcess:
        i = 0

        print(f'Item{c} (CODE {c})')
        while i < len(items[0]):
            print(f'\t{items[0][i]} -> {items[1][i][0:2]}')
            i += 1
        print(f'\n\tTS = {items[2][0]}\n\tCS = {items[3][0]}\n')
        c += 1

    n = int(input("Enter One Code (Example: 1): "))
    os.system("cls")

    if n == 1:
        ProcessName = ListProcess[0][0]
        Process = ListProcess[0][1]
        ts = ListProcess[0][2][0]
        cs = ListProcess[0][3][0]
    elif n == 2:
        ProcessName = ListProcess[1][0]
        Process = ListProcess[1][1]
        ts = ListProcess[1][2][0]
        cs = ListProcess[1][3][0]
    elif n == 3:
        ProcessName = ListProcess[2][0]
        Process = ListProcess[2][1]
        ts = ListProcess[2][2][0]
        cs = ListProcess[2][3][0]
    elif n == 4:
        ProcessName = ListProcess[3][0]
        Process = ListProcess[3][1]
        ts = ListProcess[3][2][0]
        cs = ListProcess[3][3][0]
    elif n == 5:
        ProcessName = ListProcess[4][0]
        Process = ListProcess[4][1]
        ts = ListProcess[4][2][0]
        cs = ListProcess[4][3][0]
    elif n == 6:
        ProcessName = ListProcess[4][0]
        Process = ListProcess[4][1]
        ts = ListProcess[5][2][0]
        cs = ListProcess[5][3][0]
    elif n == 7:
        ProcessName = ListProcess[4][0]
        Process = ListProcess[4][1]
        ts = ListProcess[6][2][0]
        cs = ListProcess[6][3][0]


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
    
print(f'\nContect Switch = {cs}')
print(f'Time Slice = {ts}')

Gantt_Chart(ProcessName, Process, ts, cs)


Exit = input('''
Exit(0)
Restart(1)
''')
if int(Exit) == 1:
    os.system('cls')
    os.system('py .\RoundRobin_Algorithm.py')
