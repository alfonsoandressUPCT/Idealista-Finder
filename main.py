import config
from gui_input import GuiInput
from api_arguments import api_arguments
from api_request import api_request
from data_map import data_map
from data_economy import data_economy
from gui_output import Gui_Output

if __name__ == "__main__":

    GuiInput()

    variables = config.get_variables()

    argumentos = api_arguments(variables)

    SEARCH_PARAMS = argumentos[0]
    MAX_RESULTS = argumentos[1]

    api_request(SEARCH_PARAMS, MAX_RESULTS)

    data_map()
    data_economy()

    Gui_Output()