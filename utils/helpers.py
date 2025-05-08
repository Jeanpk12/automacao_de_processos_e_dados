def calcular_media_caracteres(posts):
    if not posts:
        return 0
    total = sum(len(post['body']) for post in posts)
    return round(total / len(posts), 2)
