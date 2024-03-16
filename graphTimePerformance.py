import matplotlib.pyplot as plt

def readFile(filename):
    _500x500_5000 = {}

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
            _500x500_5000[threads] = time      

    data = {"500x500 - 5000 Generations": _500x500_5000}     

    return data

def plotEfficiency(data):
    for key, value in data.items():
        plt.plot(list(value.keys()), list(value.values()), color='darkblue')
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
    speedUpData = GenerateSpeedUpData(data["500x500 - 5000 Generations"])
    plt.plot(list(speedUpData.keys()), list(speedUpData.values()), color='darkred')
    plt.xticks([1, 2, 4, 8, 10, 16, 20])
    plt.xlabel('Threads')
    plt.ylabel('Speed-Up')
    plt.title("500x500 - 5000 Generations")
    plt.show() 

def main():
    data = readFile("time_average_outputs.txt")
    plotEfficiency(data)
    plotSpeedUp(data)

if __name__ == "__main__":
    main()
