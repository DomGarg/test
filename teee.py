import requests
import userForms

#link = "https://brandonassing.lib.id/tp-me@dev/getNumbers/"
#f = requests.get(link)
#f.json()
#print(f.text[0])



# Search GitHub's repositories for requests
response = requests.get(
    'https://dgargala.lib.id/notyet@dev/getNumbers/',
    params={'q': 'requests+language:python'},
)


# Inspect some attributes of the `requests` repository
json_response = response.json()

for i in json_response:
    #temp = json_response[i]
    #print(i[0], i[1][1], "+" + i[1][0])
    userForms.Company(i[0], i[1][1], "+" + i[1][0], None, None)

repository = json_response
print(repository)  # Python 3.6+
print(f'Repository description: {repository[0]}')  # Python 3.6+
