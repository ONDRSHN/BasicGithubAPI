import requests

def get_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Kullanıcı bulunamadı.")
        return None

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Repo bilgileri alınamadı.")
        return []

def display_profile_info(profile):
    print("\nKullanıcı Bilgileri")
    print("-" * 30)
    print(f"Kullanıcı Adı: {profile.get('login')}")
    print(f"Ad Soyad: {profile.get('name')}")
    print(f"Bio: {profile.get('bio')}")
    print(f"Takipçi: {profile.get('followers')}")
    print(f"Takip Edilen: {profile.get('following')}")
    print(f"Public Repo Sayısı: {profile.get('public_repos')}")

def display_repos(repos):
    print("\nPublic Repos")
    print("-" * 30)
    for repo in repos:
        print(f"- {repo['name']} | ⭐ {repo['stargazers_count']} | Forks: {repo['forks_count']}")

def main():
    username = input("GitHub kullanıcı adını girin: ")
    profile = get_user_profile(username)
    if profile:
        display_profile_info(profile)
        repos = get_user_repos(username)
        display_repos(repos)

if __name__ == "__main__":
    main()
