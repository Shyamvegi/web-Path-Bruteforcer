import sys
import time
import threading
import requests
import http.client

''' All modules are imported
    threading is to run threads and do multithreading
    requests modoule is to fetch data from url using get method in it
    time module is used to claculate time before starting process and after the end of process
    sys module is a system module where cmd line args and teminating the execution of process can be done 
'''

# webPathbruteForcer class which fecthes the paths using methods that i build using threading which runs faster
class webPathBruteForcer:
    #initialization
    def __init__(self,domain,pathfile,statusCodes):
        self.url= self.processUrl(domain)
        self.pathList = self.processFile(pathfile)
        self.statusCodes = set(statusCodes)
        self.bruteforceStatus = dict()
        # print(self.url)
        # print(self.pathList)
        # print(self.statusCodes)

    #this method uses requests module and get method in it to get data from url used as traget function to thread    
    def fetchRequest(self,url):
        try:
            res = requests.get(url,timeout= 10)
            if str(res.status_code) in self.statusCodes:
                self.bruteforceStatus[url] = str(res.status_code)
        except:
            self.bruteforceStatus[url] = '404'

    # this method creates thread and starts the thread after processing it kills the process and call processoutput method
    def multiThreadingRequests(self):
        threadList = []
        for webpath in self.pathList:
            url = self.url + webpath
            #print(url)
            threadList.append(threading.Thread(target=self.fetchRequest,args=(url,)))
            threadList[-1].start()
        endTimer = time.time()
        for reqThread in threadList:
            reqThread.join()
        self.processOutput()
        # print(self.bruteforceStatus)
        return endTimer;

    # this method process the output to show in cli and saves it into output.txt file
    def processOutput(self):
        try:
            with open('output.txt','a') as outfile:
                outfile.write("======================\n")
                for key,value in self.bruteforceStatus.items():
                    if value in self.statusCodes:
                        #result = key + " [Status code " + str(value) + "]"
                        result = f'{key} [Status Code : {value}]'
                        print(result)
                        outfile.write(result+'\n')
                print('Output saved into file output.txt')
        except Exception as e:
            print(e)
            print('output not saved into file')
            sys.exit()

    # this method process url by adding https to domain
    def processUrl(self,domain):
        return "https://"+domain+"/"

    # this method process the paths file to list of paths
    # reads data from wordlist.txt or any pathfile and process it into list
    def processFile(self,pathfile):
        try:
            pathList =[]
            with open(pathfile,'r') as file:
                pathList = file.read().splitlines()
        except FileNotFoundError:
            print(f'{pathFile}does not exist')
            sys.exit(1)
        return pathList

#main code
if __name__ == "__main__":
    #read data from cmd line and create object
    try:
        #create instance to class and pass args 
        bruteForcer = webPathBruteForcer(sys.argv[1],sys.argv[2],sys.argv[3:])
    except IndexError:
        print("cmdline args are not matched")
        sys.exit()
    except FileNotFoundError:
        print(f'{sys.argv[2]} does not found')
    except Exception as e:
        print(e)
        sys.exit()
    startTimer = time.time()
    endTimer = bruteForcer.multiThreadingRequests()
    print("========================================")
    print(f'{round(endTimer - startTimer,3)} Seconds  taken for web path bruteForcer')