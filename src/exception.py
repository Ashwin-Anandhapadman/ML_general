import sys #sys provides functions and variables to manipulate diff. parts of python run time env.\


def error_message_detail(error, error_detail:sys):
    #errordetail will be stores in sys and we get it out
    _,_,exc_tb = error_detail.exc_info()

    # we put _,_,exc_tb becuz we want tonly the 3rd info from error_detail that gives details on files in which error occured and line number and its details

    file_name=exc_tb.tb_frame.f_code.co_filename #check custom exception handling documentation for this code

    error_message = "error occured in python script name [{0}] Line number is [{1}] error message[{2}]".format(

    file_name,exc_tb.tb_lineno, str(error)
    return error_message

    )
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)

        self.error_message= error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

