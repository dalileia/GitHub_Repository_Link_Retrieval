import os

class ConvertJson():

    def convert_json():
        
        input_file = '/product/app/data/input_github_search.json'
        output_file = '/product/app/data/github_search.json'

        json_list = []

        with open(input_file, 'r') as file:
            for line in file:
                json_list.append(line.strip())

        if json_list:
            last_line = json_list[-1]
            json_list[-1] = last_line[:-1] if last_line.endswith(',') else last_line

        with open(output_file, 'w') as file:
            file.write('[')
            file.write(''.join(json_list))
            file.write(']')

        os.remove('/product/app/data/input_github_search.json')
