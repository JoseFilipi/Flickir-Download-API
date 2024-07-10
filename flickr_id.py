import flickrapi

# Dados para acessar a API do Flickr
api_key = ''
api_secret = ''

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# Nome do usuário
username = 'embratursebrae'

user_info = flickr.people.findByUsername(username=username)
user_id = user_info['user']['nsid']

print(f"ID do usuário: {user_id}")
