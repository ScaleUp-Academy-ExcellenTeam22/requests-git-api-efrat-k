import requests
import json


def search_github(num_of_repo, language):
    """Search the GitHub API for repositories using an input keyword.
    Args:
        keyword: A keyword string.
        num_of_repo: the num of repo to return
    Returns:
        A nested list of GitHub repositories returned for a keyword. Each result list contains the repository name,
       and num of stars.
    """

    query = "https://api.github.com/search/repositories?q=language:" + language + '&sort=stars&order=desc'
    response = requests.get(query)
    results = response.content.decode()
    results = json.loads(results)

    results_list = []
    for repo in range(0, int(num_of_repo)):
        results_list.append([results["items"][repo]["name"], results["items"][repo]["stargazers_count"]])
    return results_list


def main():
    num_of_repo = input("Enter the number of repositories you want:")
    language = input("Enter the language:")

    # search repositories on GitHub
    github_results = search_github(num_of_repo, language)
    for repo in range(len(github_results)):
        print(f'{github_results[repo][0]} is a {language} repo with {github_results[repo][1]} stars')


if __name__ == '__main__':
    main()
