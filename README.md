# GithubAPI
 Github API coded in python

GitHub Profile & Repository Viewer
This is a simple Python project that interacts with the public GitHub API to retrieve and display user information and public repositories based on a GitHub username input.
The user enters a GitHub username.

How It Works?
The program sends HTTP GET requests using the requests library:
One to fetch the user's profile (/users/{username})
One to fetch their public repositories (/users/{username}/repos)
The data is parsed from JSON and printed to the console.

We can improve this project with "Authenticated Issue Creator"
This enhanced version allows users to authenticate using a personal access token and create an issue in any repository they have write access to. It demonstrates how to perform authenticated POST requests to the GitHub REST API.

****Authenticated Issue Creator Located in venv file

