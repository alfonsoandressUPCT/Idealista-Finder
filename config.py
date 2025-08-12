# Este archivo actuará como un almacén central para las variables
variables = None

def set_variables(vars):
    global variables
    variables = vars

def get_variables():
    return variables

def set_output_dir(output_dir):
    global output_directory
    output_directory = output_dir

def get_output_dir():
    return output_directory