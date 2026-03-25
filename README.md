<div align="center">🚀 MULTI-PROFILE</div>
<div align="center">

The ultimate way to manage multiple Git identities and SSH keys seamlessly.

Report Bug · Request Feature

</div>

🧐 About The Project
MULTI-PROFILE solves the identity crisis for developers. If you use one machine for both Work and Personal projects, you’ve likely committed code with the wrong email address or struggled with SSH key conflicts.

This project provides a clean architecture using Git Conditional Includes to automatically switch your user.name, user.email, and SSH keys based on the directory you are currently in.

✨ Key Features
⚙️ Automatic Switching: No more manual git config user.email for every project.

🔒 SSH Isolation: Map specific keys to specific GitHub profiles.

📁 Organized Workflow: Keeps your global configurations clean and modular.

🛠️ Getting Started
1. Folder Setup
Organize your workspace into dedicated root folders:

Bash
mkdir -p ~/Developer/work
mkdir -p ~/Developer/personal
2. SSH Configuration
Edit your ~/.ssh/config file to handle multiple accounts:

Code snippet
# Work Profile
Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_work

# Personal Profile
Host github.com-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_personal
3. Git Conditional Logic
Update your global ~/.gitconfig to include paths dynamically:

Code snippet
[user]
    name = Your Default Name
    email = default@email.com

[includeIf "gitdir:~/Developer/work/"]
    path = ~/Developer/work/.gitconfig-work

[includeIf "gitdir:~/Developer/personal/"]
    path = ~/Developer/personal/.gitconfig-personal
🏗️ Project Architecture
Plaintext
Root/
├── .gitconfig                 # Global logic & routing
├── Developer/
│   ├── work/
│   │   ├── .gitconfig-work    # Work Identity (Email/Name)
│   │   └── company-repo/
│   └── personal/
│       ├── .gitconfig-personal # Personal Identity (Email/Name)
│       └── side-project/
🗺️ Roadmap
[x] Core structure for Work/Personal profiles.

[x] SSH Key mapping guide.

[ ] Add automated setup script (setup.sh).

[ ] Support for macOS, Linux, and Windows.

🤝 Contributing
Contributions make the open-source community an amazing place!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

<div align="center">

Developed with ⚡ by PHE SOPHY
</div>
