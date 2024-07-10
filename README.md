# Flickr Album Downloader

Este projeto é um script Python para baixar todas as imagens de álbuns de uma conta do Flickr. Utiliza a API do Flickr para buscar e fazer download das imagens.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes pacotes instalados:

- flickrapi
- requests

Você pode instalá-los usando pip:

```
pip install flickrapi requests
```

Depois preencher as variáveis de API e ID:

```
api_key = 'sua_api_key'
api_secret = 'seu_api_secret'
user_id = 'user_id_do_dono_da_foto'
```

Por fim, defina um dirétório para salvar as imagens:

```
base_dir = 'caminho/para/salvar/imagens'
```
