import requests
import pprint as p
URL = 'https://api.covid19api.com/summary'

covid19 = requests.get(URL)
covid19_global = covid19.json()['Global']
covid19 = covid19.json()['Countries']
titles = [item for item in list(covid19[0].keys()) if item not in
          ['ID', 'Slug', 'Date', 'Premium', 'CountryCode']]


def byNewConfirmed_key(covid19):
    return covid19["NewConfirmed"]


exit = False
try:
    while exit != True:
        colapse = (input(
            '1. Show COVID19 information\n2. Sort by new confirmed\n3. Отримати детальну інформацію по назві країни ("Country")\n4. Show global information\n5. Exit\n'))
        if colapse == '4':
            p.pprint(covid19_global)
        if colapse == '1':
            for item in titles:
                if item == 'Country':
                    print("{0:_^35s}".format(item), end='')
                else:
                    print("{0:_^15s}".format(item), end='')
            else:
                print(' ')
            for item in covid19:
                for key in item:
                    if key in titles:
                        if key == 'Country':
                            print("{0:<31}".format(item[key]), end='')
                        else:
                            print("{0:>15}".format(item[key]), end='')
                else:
                    print('')
        if colapse == '2':
            covid19 = sorted(covid19, key=byNewConfirmed_key, reverse=True)
            for item in titles:
                if item == 'Country':
                    print("{0:_^35s}".format(item), end='')
                else:
                    print("{0:_^15s}".format(item), end='')
            else:
                print(' ')
            for item in covid19:
                for key in item:
                    if key in titles:
                        if key == 'Country':
                            print("{0:<31}".format(item[key]), end='')
                        else:
                            print("{0:>15}".format(item[key]), end='')
                else:
                    print('')
        if colapse == '3':
            co = input('Enter country\t')
            for item in covid19:
                for key in item:
                    if key in titles:
                        if item[key] == co:
                            p.pprint(item)
        if colapse == '5':
            exit = True
            print('EXIT')
except Exception as e:
    print(e)
