import requests, os
#need install requests


def make_url(complement):
    url = "https://api.covid19api.com/"+complement
 
    return url



def get_data(url):
    data = requests.get(url).json()
    
    return data


def find_country(country):
    countries = get_data(make_url('summary'))["Countries"]

    for c in range(0, len(countries)):
        if country in countries[c]["Country"]:
            return countries[c]
        
    return f"ERROR! Couldn't find {country}"



def show_data(dictionary):
    for key, info in dictionary.items():
        print(f'{key:.<28}{info}')



print('loading libs...')


while True:
    os.system("clear")
    
    print('*'*36)
    print('*{:^34}*'.format('Info-Covid'))
   
    while True:
         
        print('*'*36)
        print('* [1] Show data world              *')
        print('* [2] Show data country            *')
        print('* [0] Exit                         *')
        print('* [i] How prevent                  *')
        print('*'*36)
    
   
        opc = input(' : ').strip()
        
        if opc not in '012i':
            os.system("clear")
            print(f'ERROR!! "{opc}" This option do not exists!')
        
        else:
            break
            
            
    print('*'*36)
    print('Wait a moment...')
    print('*'*36)
    
    if opc == '1':
        url = make_url('summary')
        
        show_data(get_data(url)["Global"])
    
    elif opc == '2':
        country = str(input('Type a country: ')).strip().title()
       
        show_data(find_country(country))
    
    elif opc == 'i':
        print('This option is available now!')

    else:
        exit()
    
    
    print('*'*36)
    
    cont = str(input('Do you want see more[Y/N]: ')).upper()
    
    if 'N' in cont:
        break

print('Come back always...')

