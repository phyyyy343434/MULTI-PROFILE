Status: Active ✅

Understood, Master JZYY. The diagram looks like a mess because the special characters and spacing aren't being escaped properly in GitHub's Markdown.

I have fixed the PROJECT STRUCTURE to use a dedicated Code Block (which forces a fixed-width font and prevents the text from "smushing" together). I also added clean headers to match the Apple-style precision you want.

Copy and paste this version:

<div align="center">🚀 MULTI-PROFILE</div>
<div align="center">

Advanced Git Identity & SSH Key Orchestration System

</div>

PROJECT OVERVIEW
This project is a robust, automated solution for managing multiple Git identities and SSH configurations on a single workstation.

The primary objective is to eliminate "Identity Leakage" (committing withß the wrong email) and "Authentication Friction" (SSH key conflicts) when switching between professional, personal, and open-source environments.

PROJECT STRUCTURE
Plaintext
MULTI-PROFILE/
├── configs/
│   ├── .gitconfig-personal    # Personal identity (Name/Email)
│   └── .gitconfig-work        # Professional identity (Name/Email)
├── scripts/
│   └── setup.sh               # Environment initialization script
├── .gitconfig                 # Global entry point (Conditional Logic)
├── ssh_config_example         # Reference for ~/.ssh/config mapping
├── LICENSE                    # MIT License
└── README.md                  # Technical documentation
KEY FEATURES & IMPLEMENTATION DETAILS
A. Conditional Configuration Injection
Instead of manually updating global variables, this project uses the includeIf directive.

Logic: When a user enters a specific directory tree (e.g., ~/Developer/work/), Git automatically merges the corresponding profile.

Benefit: Zero manual commands required when switching projects.

B. SSH Identity Mapping
Standard SSH setups struggle with multiple keys for the same host (github.com).

Implementation: Custom Host aliases in ~/.ssh/config.

Result: Discrete keys for github.com-work and github.com-personal.

SETUP & DEPLOYMENT
1. Clone the repository:

Bash
git clone https://github.com/phyyyy343434/MULTI-PROFILE.git
cd MULTI-PROFILE
2. Configure your Global Git:
Add these lines to your ~/.gitconfig:

Code snippet
[includeIf "gitdir:~/Developer/work/"]
    path = ~/Developer/work/.gitconfig-work

[includeIf "gitdir:~/Developer/personal/"]
    path = ~/Developer/personal/.gitconfig-personal
TECHNICAL DEBT & OPTIMIZATION ROADMAP
Automated Setup Script: Currently manual; planned bash automation.

Cross-Platform Support: Optimized for Unix; Windows support coming soon.

Asset Optimization: Transitioning to standardized rem-based spacing scales.

PROJECT STATUS
This project is actively maintained as a core utility for the JZYY Development Environment.

Maintained by: PHE SOPHY ✅
