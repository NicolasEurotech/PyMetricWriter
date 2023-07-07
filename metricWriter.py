import os
import time

## METRIC WRITE CLASS -> CAN WRITE .prom FILE TO UPDATE IN RUN PROM FILES
## This class is suggetst to create a library use in enviroment like imported

class MetricWriter:

    # file_name -> it's reccomand to indicate only file name without extention ex. "backup_job_name", because directory is create in software directori or docker build with opportune path.
    def __init__(self, file_name, start_time : time = time.time(), end_time : time = 0):

        if not os.path.isdir("./metrics/"):
            os.mkdir("./metrics/")

        self.file_name = file_name
        self.file_path = "./metrics/{_file_name}.prom".format(_file_name = file_name)
        self.start_time = start_time
        self.end_time = end_time

    def get_end_time(self):
        return self.end_time
    
    def set_end_time(self, end_time):
        self.end_time = end_time
    
    ## This function create a file with initialized file name, if already exist it replace
    def create_file(self):
        try:
            f = open(self.file_path, "w+")
            prom_text = ""
            f.write(prom_text)
            f.close()
        except Exception as e:
            print("Something with FILE went wrong\n {e}".format(e = e))

    ## This function appendes in .prom file any param we want to export 
    def append_in_file(self, text, value):
        try:
            f = open(self.file_path, "a+")
            prom_text = "{_file_name}_{_text} {_value}\n".format(_file_name=self.file_name, _text = text, _value = value)
            f.write(prom_text)
            f.close()
        except Exception as e:
            print("Something with FILE went wrong -> {e}".format(e = e))

    ## This function change the value status in .prom file
    # 0 -> If the program is in ERROR or not complete
    # 1 -> If is completed or OK
    # 2 -> If is in RUN 
    # METRICWORD -> String type identify what row need to change
    # VALUE -> New set Value
    # #
    def change_metric_value(self, metricWord, value : str):
        tempText = ""
        try:
            with open(self.file_path,"r") as textLines:
                for row in textLines:
                    if (row.find(metricWord) >= 1):
                        rowExplode = row.split(" ")
                        rowExplode[1] = " {_value}".format(_value=value)
                        tempText += rowExplode[0]+rowExplode[1]+"\n"
                    else:
                        tempText += row                    

                textLines.close()
        except Exception as e:
            print("Something with FILE went wrong\nREAD | CHANGE -> {e}".format(e = e))

        try:
            f = open(self.file_path, "w+")
            f.writelines(tempText)
            f.close()
        except Exception as e:
            print("Something with FILE went wrong\nWRITE | CHANGE -> {e}".format(e = e))
    
    ## This function:
    # 1. Define the start time of program.
    # 2. Set status of script in 0, this means is in run. 
    # 3. Place default values 
    def start_execution(self):
        self.create_file()
        self.append_in_file("status", "0")
        self.append_in_file("start_time", self.start_time)
        self.append_in_file("end_time", "0")
        self.append_in_file("execution_time", "0")
        
    ## This function define:
    # 1. The time of end execution of the function
    # 2. The status of complete function
    def end_execution(self, end_status : bool):
        #STATUS JOB
        if(end_status):
            self.change_metric_value("status","1")
        else:
            self.change_metric_value("status","2")

        #STOP TIME
        self.set_end_time(time.time())
        self.change_metric_value("end_time", self.end_time)
        self.execution_time()

    ## This function append delta time from start to end -> execution time
    #  and calculate/define the end of script execution
    def execution_time(self):
        end_time = self.get_end_time()
        self.change_metric_value("execution_time" , end_time - self.start_time )

if __name__ == "__main__":
    test = MetricWriter("test")
    test.start_execution()
    time.sleep(1)
    test.end_execution()
    





