import csv
import json
import time

timestr = time.strftime('%Y%m%d-%H%M%S')
file_path = 'csv/artiles_20230409-221317.csv'
output_path = f'json/trainings_data_{timestr}.jsonl'

def prompt_list_maker(file_path):
    prompt_list = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter='#')
        next(reader)
        for row in reader:
            category = row[0]
            title = row[1]
            article = row[2]
            prompt_list.append({"prompt": f"{category}, {title}'\n\n###\n\n", "completion": f"{article.replace(' War dieser Text hilfreich für Sie? ', ' ')}###"})
        return prompt_list

def prompt_list_writer(prompt_list, output_path):
    with open(output_path, 'w') as f:
        for element in prompt_list:
            f.write(json.dumps(element, ensure_ascii=False) + "\n")

prompt_list_writer(prompt_list_maker(file_path), output_path)