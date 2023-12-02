import sys

# to check what is the error exactly
def error_message_detail(error, error_detail:sys):
    _,_,exc_detail = error_detail.exc_info()
    file_name = exc_detail.tb_frame.f_code.co_filename
    error__message = "Error Occurred in script [{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_detail.tb_lineno, str(error)
    )
    return error__message
# to raise a custom exception
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error=error_message, error_detail=error_detail)
    def __str__(self):
        return self.error_message