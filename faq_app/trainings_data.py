import csv
import json
import time

timestr = time.strftime('%Y%m%d-%H%M%S')
file_path = 'faq_app/faq_contents/articles_20230409-221317.csv'
output_path = f'faq_app/trainings_data/trainings_data_{timestr}.jsonl'

def prompt_list_maker(file_path, category_filter=''):
    '''
    Reads in the csv file containing articles returned by articles_to_csv() in articles.py, extracts category, link and article and
    appends them to a list that gets returned. The list will have one element of the original list in one line, formatted
    according to openai trainings data requirements.
    '''
    prompt_list = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter='#')
        next(reader)
        for row in reader:
            category = row[0]
            title = row[1]
            article = row[2]
            if not category_filter:
                prompt_list.append({"prompt": f"{category}, {title}'\n\n###\n\n", "completion": f"{article.replace(' War dieser Text hilfreich für Sie? ', ' ')}###"})
            else:
                print(category)
                print(category_filter)
                if category_filter == category:
                    prompt_list.append({"prompt": f"{category}, {title}'\n\n###\n\n", "completion": f"{article.replace(' War dieser Text hilfreich für Sie? ', ' ')}###"})
        return prompt_list

def prompt_list_writer(prompt_list, output_path='trainings_data/'):
    '''
    Writes the list of prompts returned by prompt_list_maker() and writes them to a jsonl file.
    '''
    with open(output_path, 'w') as f:
        for element in prompt_list:
            f.write(json.dumps(element, ensure_ascii=False) + "\n")

prompt_list_writer(prompt_list_maker(file_path, 'Domains'), f'faq_app/trainings_data/trainings_data_{timestr}.jsonl')