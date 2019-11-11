import requests


def get_movie(movie, my_key):
    parameters = {'t': movie}
    url = 'http://www.omdbapi.com/?apikey=' + str(my_key)
    res = requests.get(url, parameters)
    return eval(res.content.decode('utf-8'))


def main():
    my_key = 59693491
    movie = 'Fantastic Mr. Fox'
    res = get_movie(movie, my_key)

    # check the response received from omdb
    if eval(res['Response']) and 'Error' not in res.keys():
        for key in res.keys():
            if key is 'Ratings':
                # print the 'Ratings' keys in the dictionary
                for items in range(0, len(res[key])):
                    print(f"{res[key][items]['Source']}: {res[key][items]['Value']}")
            elif key is not 'Response':
                print(f"{key}: {res[key]}")
    elif 'Error' in res.keys():
        print('Error:', res['Error'])
    else:
        print('Invalid response')


if __name__ == "__main__":
    main()