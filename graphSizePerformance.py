import matplotlib.pyplot as plt

from graphTimePerformance import plotEfficiency

def readFile(filename):
    _1x16 = {}
    _2x8 = {}
    _4x4 = {}
    _8x2 = {}
    _16x1 = {}

    with open(filename) as file:
        print("Reading data from "+filename+" : \n")
        for line in file:
            time = float(line.strip().split(" ")[-1].strip())
            size = int(line.strip().split(" ")[4].strip())
            xsize = int(line.strip().split(" ")[5].strip())
            gen = int(line.strip().split(" ")[6].strip())
            threads = int(line.strip().split(" ")[7].strip("':"))
            print(
                 "Time: "+str(time)+"\n"
                +"Size: "+str(size)+"x"+str(xsize)+"\n"
                +"Generations: "+str(gen)+"\n"
                +"Threads: "+str(threads)+"\n"
            )
            if size == 1:
                _1x16[threads] = time
            elif size == 2:
                _2x8[threads] = time
            elif size == 4:
                _4x4[threads] = time
            elif size == 8:
                _8x2[threads] = time
            elif size == 16:
                _16x1[threads] = time       

    data = {
        "1x16": _1x16,
        "2x8": _2x8,
        "4x4": _4x4,
        "8x2": _8x2,
        "16x1": _16x1
    }     
    
    return data

def plotEfficiency(data):
    for key, value in data.items():
        plt.plot(list(value.keys()), list(value.values()), color="darkblue")
        plt.xticks([1, 2, 4, 8, 10, 16, 20])
        plt.xlabel('Threads')
        plt.ylabel('Time (seconds)')
        plt.title(key)
        plt.show() 

def GenerateSpeedUpData(data):
    # data is dict of threads:time
    baseTime = data[1]
    for key, value in data.items():
        data[key] = baseTime / value
    
    return data

def plotSpeedUp(data):
    for key, value in data.items():
        speedUpData = GenerateSpeedUpData(value)
        plt.plot(list(speedUpData.keys()), list(speedUpData.values()), color="darkred")
        plt.xticks([1, 2, 4, 8, 10, 16, 20])
        plt.xlabel('Threads')
        plt.ylabel('Speed-Up')
        plt.title(key)
        plt.show() 

def main():
    data = readFile("size_average_outputs.txt")
    plotEfficiency(data)
    plotSpeedUp(data)

if __name__ == "__main__":
    main()
