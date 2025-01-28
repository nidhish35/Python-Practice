import platform
import webbrowser

def get_vs_code_download_link():
    """
    Detects the current operating system and returns the appropriate VS Code download URL.
    """
    system_name = platform.system().lower()  # 'windows', 'linux', 'darwin'
    architecture = platform.architecture()[0]  # '32bit' or '64bit'

    download_link = None

    if system_name == "windows":
        # Default to the 64-bit installer
        if architecture == "32bit":
            download_link = "https://code.visualstudio.com/sha/download?build=stable&os=win32"
        else:
            download_link = "https://code.visualstudio.com/sha/download?build=stable&os=win64"
    elif system_name == "linux":
        # VS Code provides different packages for Linux distributions
        download_link = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
    elif system_name == "darwin":
        # macOS
        download_link = "https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal"

    return download_link

def download_vs_code():
    """
    Opens the download page for VS Code based on the detected OS.
    """
    link = get_vs_code_download_link()
    if link:
        print(f"Opening download link for VS Code: {link}")
        webbrowser.open(link)  # Opens the link in the default web browser
    else:
        print("Unable to determine the appropriate download link for your OS.")

if __name__ == "__main__":
    download_vs_code()
