import os

def try_me():
    user = os.path.expanduser('~').split('/')[-1]

    return f"""
Hello {user} !!!
If You Are Seeing This It Means,
Neither Of US Fail And My Package Was Sucessfully Install.
Have Fun !!!
"""

if __name__ == "__main__":
    print(try_me())
