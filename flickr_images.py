import flickrapi
import requests
import os

# Dados para acessar a API do Flickr
api_key = ''
api_secret = ''

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')


def download_image(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)


def sanitize_filename(filename):
    return "".join(c if c.isalnum() or c in "._- " else "-" for c in filename)


user_id = ''  # ID da conta aonde estão os albúns

albums = flickr.photosets.getList(user_id=user_id)['photosets']['photoset']

base_dir = ''
os.makedirs(base_dir, exist_ok=True)

for album in albums:
    album_id = album['id']
    album_title = album['title']['_content']
    album_title = sanitize_filename(album_title)
    album_dir = os.path.join(base_dir, album_title)

    if os.path.exists(album_dir):
        print(f"Pasta {album_title} já existe. Pulando este álbum.")
        continue

    os.makedirs(album_dir, exist_ok=True)
    print(f"Baixando imagens do álbum: {album_title}")
    photos = flickr.photosets.getPhotos(photoset_id=album_id, user_id=user_id)['photoset']['photo']

    counter = 1  # Renomear as imagens com números evita problema de arquivos com mesmo nome

    for photo in photos:
        photo_id = photo['id']
        photo_title = photo['title']

        sizes = flickr.photos.getSizes(photo_id=photo_id)['sizes']['size']
        original_size = next(size for size in sizes if size['label'] == 'Original')
        photo_url = original_size['source']

        file_path = os.path.join(album_dir, f"image_{counter}.jpg")

        download_image(photo_url, file_path)
        print(f"Imagem {counter} baixada com sucesso!")

        counter += 1

print("Todas as imagens foram baixadas!")
