from typing import List
constant = '-e .'
def get_requirements(filename: str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    req_list = []
    with open(filename, 'r') as f:
        data = f.read()
        req_list = data.split('\n')

        if constant in req_list:
            req_list.remove(constant)
        return req_list
    

get = get_requirements('requirements.txt')
print(get)