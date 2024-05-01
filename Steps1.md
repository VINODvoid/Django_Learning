# Steps Followed for Installation and Setup of Django

### 1. Install Python
- **Download Python**: Go to the official Python website at [python.org](https://www.python.org/downloads/) and download the latest version of Python for your operating system (Windows, macOS, or Linux).
- **Run Installer**: Once the download is complete, run the installer. **Important: Make sure to check the box that says "Add Python to PATH" or "Add Python X.X to PATH" during the installation process**. This option ensures that Python is added to the system PATH variable, allowing you to run Python from any command prompt or terminal window.
- **Check Installation**: After installation, open a terminal or command prompt and check that Python is installed by running:

```bash
python --version
```
---
### 2. Install Vs Code

- **Download VS Code**: Go to the official Visual Studio Code website at [code.visualstudio.com](https://code.visualstudio.com/) and download the installer for your operating system.
- **Run Installer**: Run the downloaded installer and follow the installation wizard's instructions to install VS Code.
- **Verify Installation**: After installation, open VS Code and ensure it launches without any issues.
---
  
### 3. Set Up a Python Virtual Environment

- **Create Virtual Environment**: You can create a Python virtual environment to isolate your Django project's dependencies.
-  While Python comes with its own built-in virtual environment module (`venv`), you can also install `virtualenv` for managing virtual environments.
- Install `virtualenv` using pip:
  ```bash
  pip install virtualenv
  ```
- **Create a new virtual environment**:
  ```bash
  virtualenv myenv
  ```
  Replace `myenv` with the name you want for your virtual environment.
- **Activate Virtual Environment**: Activate the virtual environment by running the appropriate command for your operating system:
- **Windows**: 
  ```bash
  myenv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source myenv/bin/activate
  ```
   You should see `(myenv)` at the beginning of the command prompt, indicating that the virtual environment is active.  
      <br>
    To verify that the virtual environment is active, you can also run the following command:
    ```bash
    which python
    ```
    If the output points to the Python interpreter within your virtual environment, it means the environment is active.
---
### 4.Install Django

- **Install Django**: Open a terminal or command prompt and use pip, Python's package manager, to install Django by running:
```bash
pip install django
```
- **Verify Installation**: After the installation completes, verify that Django is installed by running:
```bash
django-admin --version
```
---
<br>

Click Here to Move to Next Step: [Next Step](./Steps2.md)
<br>
 **Happy Coding!** :smiley:
 Developed with ❤️ by ~~Kalki~~.

---

