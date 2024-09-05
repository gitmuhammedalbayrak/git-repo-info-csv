# -*- coding: utf-8 -*-

import requests
import csv

# GitHub kullanıcı adını buraya yaz
username = "gitmuhammedalbayrak"

# GitHub API URL'si
url = f"https://api.github.com/users/{username}/repos"

# API'den verileri çek
response = requests.get(url)
repos = response.json()

# CSV dosyasına yazma
with open('github_repos.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # CSV başlıkları
    writer.writerow(['Repo Adı', 'Açıklama', 'Dil', 'Yıldız Sayısı', 'Fork Sayısı', 'URL'])

    # Her repo için bilgileri yaz
    for repo in repos:
        writer.writerow([repo['name'], repo['description'], repo['language'], repo['stargazers_count'], repo['forks_count'], repo['html_url']])

print("Repo bilgileri github_repos.csv dosyasına yazıldı.")