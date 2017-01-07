# What's popular at recurse center?

import datetime
import os
import pickle

from github import Github, GithubException

from hackers import lst


### Need 


g = Github('user', 'password')
g = Github('chirs', 'password')
g = Github('drchirs', 'password')


def repos_for_user(username):
    l = []

    try:
        repos = [e for e in g.get_user(username).get_repos()]
    except GithubException.RateLimitExceededException:
        import pdb; pdb.set_trace()
    except:
        print(username)
        return []

    for repo in repos:

        description = repo.description
        stars = repo.stargazers_count
        watchers = repo.watchers_count
        forks = repo.forks_count

        try:
            commits = repo.get_commits().reversed
        except GithubException.RateLimitExceededException:
            import pdb; pdb.set_trace()
        except:
            continue

        c1 = commits[0] # need to get the first commit, not the last.

        date_string = c1.raw_data['commit']['committer']['date']
        
        ds2 = date_string.split('T')[0]

        try:
            year, month, day = [int(e) for e in ds2.split('-')]
        except:
            import pdb; pdb.set_trace()

        dt = datetime.datetime(year, month, day)

        d = {
            'name': repo.name,
            'full_name': repo.full_name,
            'description': repo.description or '',
            'watchers': watchers,
            'stars': stars,
            'forks': forks,
            'start_date': dt,
            }

        l.append(d)


    return l


def save_github(lst):
    if not os.path.exists('repos.pickle'):
        f = open('repos.pickle', 'wb')
        pickle.dump([], f)
        f.close()
        
    print('pickling')
    f = open('repos.pickle', 'ab')
    pickle.dump(lst, f)
    f.close()


def check_empty_user():

    if not os.path.exists('users.pickle'):
        s = set()
        f = open('users.pickle', 'wb')
        pickle.dump(s, f)
        f.close()
        


def save_user(username):
    check_empty_user()

    f = open('users.pickle', 'rb')
    s = pickle.load(f)
    s.add(username)

    f = open('users.pickle', 'wb')
    pickle.dump(s, f)
    f.close()


def check_users(username):

    check_empty_user()

    print('pickling')
    f = open('users.pickle', 'rb')
    s = pickle.load(f)
    return username in s

    
    


def started_at_rc(dt, batch_dates):
    for start, end in batch_dates:
        if dt < end and dt > start:
            return True
    return False


def collect_repos(lst):

    l = []

    for username, batch_dates in lst:

        if not check_users(username):
            save_user(username)
            repos = repos_for_user(username)
        
            for repo in repos:
                if started_at_rc(repo['start_date'], batch_dates):
                    l.append(repo)

            save_github(l)
        
    return l


def main():

    repos = collect_repos(lst)



if __name__ == "__main__":
    main()
