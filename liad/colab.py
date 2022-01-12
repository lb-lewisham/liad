import os


def in_colab():
    """Guesses whether the script is currently in google colab."""
    return True if os.getenv("HOME") == "/root" else False
