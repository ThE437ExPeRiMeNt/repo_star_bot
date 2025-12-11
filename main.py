# main.py

from account_creator import create_google_account
from github_starer import create_github_account_and_star
from config import TARGET_REPO, NUM_ACCOUNTS_TO_CREATE

if __name__ == "__main__":
    for i in range(NUM_ACCOUNTS_TO_CREATE):
        print(f"Creating account {i + 1}/{NUM_ACCOUNTS_TO_CREATE}")
        try:
            email, password = create_google_account()
            create_github_account_and_star(email, password, TARGET_REPO)
        except Exception as e:
            print(f"Error creating account or starring repo: {e}")
        print("-" * 30)
