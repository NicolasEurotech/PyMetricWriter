import os
import re
import time

class MetricWriter:
    """
    # This class is used to write metrics in .prom file.\n
    """

    def __init__(self, file_name):
        """
        file_name -> it's reccomand to indicate only file name without extention ex. "backup_job_name". (Because directory is create in software directory or docker build with opportune path.)
        """

        if not os.path.isdir("./metrics/"):
            os.mkdir("./metrics/")

        self.file_name = file_name
        self.file_path = "./metrics/{_file_name}.prom".format(_file_name = file_name)

        self.start_time : time = time.time()
        self.end_time : time = 0

    def __get_end_time(self):
        return self.end_time
    
    def __set_end_time(self, end_time):
        self.end_time = end_time
    
    def __create_file(self):
        """
        Create a file with initialized file name, if already exist it replace
        """
        try:
            f = open(self.file_path, "w+")
            prom_text = ""
            f.write(prom_text)
            f.close()
        except Exception as e:
            print("Something with FILE went wrong\n {e}".format(e = e))

    def __sanitize_text(self, text : str) -> str:
        """
        Sanitize text from special characters, spaces, dots, etc.\n
        """
        #sanitized_text
        s_text = ""

        #use regex to replace special characters
        regex_special = r"[^\w\sÀ-ÿ]"
        s_text = re.sub(regex_special, "_", text)
        
        return s_text


    def append_in_file(self, metricWord : str, value : str):
        """
        Appendes in .prom file any param we want to export.\n
        text -> it's the name of the metric.\n
        value -> it's the value of the metric.\n
        #### In case of text with spaces, dots, or other special characters, it will be replaced with "_".
        """
        #Sanitize text and value
        metricWord = self.__sanitize_text(metricWord)

        try:
            f = open(self.file_path, "a+")
            prom_text = f"{self.file_name}_{metricWord} {value}\n"
            f.write(prom_text)
            f.close()
        except Exception as e:
            print("Something with FILE went wrong -> {e}".format(e = e))

    def change_metric_value(self, metricWord : str, value : str):
        """
        Can change the value status in .prom file.\n 
        metricWord -> String type identify what row want to change.\n
        value -> New set Value\n
        #### In case of text with spaces, dots, or other special characters, it will be replaced with "_".
        """

        metricWord = self.__sanitize_text(metricWord)

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
    
    def start_execution(self):
        """
        ### This function initialize the start of the script execution.\n
        Set status of script in 2, this means is in run. \n
        Place default values.
        """
        self.__create_file()
        self.append_in_file("status", "0")
        self.append_in_file("start_time", self.start_time)
        self.append_in_file("end_time", "0")
        self.append_in_file("execution_time", "0")
    
    def end_execution(self, status : int = 999):
        """
        ### Define the time of end execution of the function and the status of complete function.\n
        end_status can be:\n
        0 -> If the program is RUN or not complete.\n
        1 -> If is completed or OK.\n
        other -> If it has some error or other status.\n
        """
        #STATUS JOB
        match status:
            case 0:
                self.change_metric_value("status","0")
            case 1:
                self.change_metric_value("status","1")
            case _: 
                self.change_metric_value("status", str(status))

        #STOP TIME
        self.__set_end_time(time.time())
        self.change_metric_value("end_time", self.end_time)
        self.__execution_time()

    def __execution_time(self):
        """
        Append delta time from start to end -> execution time,\n and calculate/define the end of script execution.
        """
        end_time = self.__get_end_time()
        delta_time = end_time - self.start_time
        self.change_metric_value("execution_time", delta_time)

if __name__ == "__main__":
    test = MetricWriter("test")
    test.start_execution()
    
    test.append_in_file("test-minus-1", 1)
    test.change_metric_value("test-minus-1", 2)
    test.append_in_file("test white space", 1)
    test.change_metric_value("test white space", 2)
    test.append_in_file("test.dot.2", 1)
    test.change_metric_value("test.dot.2", 2)
    test.append_in_file("testé1ò2à3e':,;", 1)
    test.change_metric_value("testé1ò2à3e':,;", 2)

    time.sleep(1)
    test.end_execution()