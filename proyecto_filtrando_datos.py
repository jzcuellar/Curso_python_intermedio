# Clase Explicacion https://platzi.com/clases/2255-python-intermedio/36467-proyecto-filtrando-datos/

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # list con todos los python devs -> utilizando list comprenhesion
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"] #1
    
    # lista (all_python_devs2_name) con nombre de todos los python devs -> Utilizando Filter y Map
    all_python_devs2 = list(filter(lambda worker: worker['language']=='python', DATA))
    all_python_devs2_name = list(map(lambda worker: worker['name'],all_python_devs2))

    # list con todos los trabajadores de platzi -> utilizando list comprenhesion
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    
    # lista (all_platzi_workers_name) con nombre de todos los platzi workers -> Utilizando Filter y Map
    all_platzi_workers2 = list(filter(lambda worker: worker['organization']== 'Platzi', DATA))
    all_platzi_workers2_name = list(map(lambda worker: worker['name'],all_platzi_workers2))

    # lista (adults_name) con nombre de todos los adultos -> Utilizando Filter y Map
    adults = list(filter(lambda worker: worker['age']>=18, DATA))
    adults_name = list(map(lambda worker: worker['name'],adults))

    # lista (adults_name2) con nombre de todos los adultos -> Utilizando list comprehension
    adults_name2 = [worker['name'] for worker in DATA if worker['age']>=18]
    
    # Voy a agregar una key y value al diccionario -> Utilizando Map
    old_people = list(map(lambda worker: worker | {"old":worker['age'] > 70}, DATA))

    # lista (old_people2) con nombre de todos los adultos > 70 -> Utilizando list comprehension
    old_people2 = [worker['name'] for worker in DATA if worker['age']>70]

    # print(all_python_devs)
    # print(all_platzi_workers2_name)
    # print(adults_name2)
    print(old_people2)
    # print(all_python_devs2_name)


if __name__ == '__main__':
    run()

#1 Worker