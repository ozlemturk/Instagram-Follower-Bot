# Instagram Follower Bot

This project is a simple Instagram bot using Python and Selenium. It logs into Instagram, opens the followers of a similar account, and can optionally follow users.

## Features

- Log into Instagram using credentials from `.env`
- Open the followers list of a specified account
- Scroll through the followers to load more
- Follow users (method ready to implement)
- Keep Chrome browser open after script finishes

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (matching your Chrome version)
- Python packages:
  - selenium
  - python-dotenv

## Setup

1. Clone the repository or download the files.
2. Install dependencies:
   ```bash
   pip install selenium python-dotenv
3.Create a .env file in the project root and add your credentials:

USERNAME=your_instagram_username
PASSWORD=your_instagram_password
SIMILAR_ACCOUNT=target_account

## Usage

* Run the script:
  ```bash
  python insta_follower.py
  ```
* The bot will log in, open the target account’s followers, and scroll to load more.

## Warnings

* Instagram may flag automated interactions as spam. Use responsibly.
* Add delays (time.sleep) if implementing the follow functionality to avoid account restrictions.
* This bot is intended for educational purposes only.
