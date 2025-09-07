# 🔐 Local Password Manager

A simple **Password Manager** built with Python that stores your
credentials securely on your local machine.\
This tool helps you generate strong passwords and manage them without
relying on cloud storage.

------------------------------------------------------------------------

## 🖼️ Screenshots

![Password Manager](/images/Screenshot_password_manager.png)

------------------------------------------------------------------------

## ✨ Features

-   🔎 Search saved credentials by website
-   ➕ Add new login details (Website, Email/Username, Password)
-   🗑️ Clear all inputs with one click
-   🔑 Generate strong passwords (12, 16, or 20 characters)
-   💾 Data stored **locally** for maximum privacy
-   🎨 Clean and user-friendly interface

------------------------------------------------------------------------

## 📦 Installation

1.  Clone the repository:

    ``` bash
    git clone https://github.com/your-username/password-manager.git
    cd password-manager
    ```

2.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

3.  Run the app:

    ``` bash
    python main.py
    ```

------------------------------------------------------------------------

## 🖥️ Windows Executable

If you don't have Python installed, you can download the **ready-to-use
`.exe` file** from the
[Releases](https://github.com/your-username/password-manager/releases)
section.

------------------------------------------------------------------------

## 🛠️ Build Executable Yourself

If you want to build the `.exe`:

``` bash
pip install pyinstaller
pyinstaller --onefile main.py
```

The executable will be created inside the `dist/` folder.

------------------------------------------------------------------------

## ⚠️ Security Note

This password manager stores data **locally on your machine**.\
It's great for personal use, but for highly sensitive accounts, consider
using a dedicated encrypted password manager.

------------------------------------------------------------------------

## 📜 License

This project is licensed under the MIT License -- see the
[LICENSE](LICENSE) file for details.
