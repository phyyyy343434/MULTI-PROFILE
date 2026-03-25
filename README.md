🚀 MULTI-PROFILE
Effortless Git Identity Management for Multiple Accounts

📖 Overview
MULTI-PROFILE is a streamlined solution for developers who manage multiple GitHub or GitLab accounts (e.g., Work vs. Personal) on a single machine.

✅ The Solution
Using Git Conditional Includes to dynamically load configurations based on the project path.

🛠️ Implementation Guide
1. Organize Your Directories
Separate your projects into dedicated root folders:

~/Developer/work/

~/Developer/personal/

2. Configure SSH Keys
Edit your ~/.ssh/config file:

Code snippet
# Work Account
Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_work

# Personal Account
Host github.com-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_personal
3. Setup Git Conditional Includes
In your global ~/.gitconfig, add the following logic:

Code snippet
[user]
    name = Default Name
    email = default@email.com

# Apply work config for projects in the 'work' folder
[includeIf "gitdir:~/Developer/work/"]
    path = ~/Developer/work/.gitconfig-work

# Apply personal config for projects in the 'personal' folder
[includeIf "gitdir:~/Developer/personal/"]
    path = ~/Developer/personal/.gitconfig-personal
4. Create Sub-Configs
Create the specific identity files (e.g., ~/Developer/work/.gitconfig-work):

Code snippet
[user]
    name = Your Name
    email = work-email@company.com
📂 Architecture Preview
Plaintext
Root/
├── .gitconfig (Global Settings)
├── Developer/
│   ├── work/
│   │   ├── .gitconfig-work (Identity A)
│   │   └── project-alpha/
│   └── personal/
│       ├── .gitconfig-personal (Identity B)
│       └── side-hustle/
🚀 Key Benefits
Zero Manual Switching: Set it once, and Git handles the rest.

Privacy: Keeps your personal email out of corporate histories.

Security: Ensures the correct SSH key is used for the correct server.

🤝 Contributing
Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

⚖️ License
Distributed under the MIT License. See LICENSE for more information.

Developed by PHE SOPHY | 2026
