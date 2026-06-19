# 🛡️ AUR-Shield

A lightweight, automated preventive malware and IoC (Indicator of Compromise) scanner for Arch Linux (AUR) packages. It hooks into `pacman` transaction triggers to inspect installation scripts (`.INSTALL`) and metadata blocks (`.PKGINFO`) right after download, but *before* any code execution or unpacking happens.
---

## Installation

### Method 1: The Standard Arch Way (Recommended)

1. Clone this repository:
```
git clone https://github.com/sashkomster-lab/aur-shield.git
cd aur-shield
```
Build and install the package globally using makepkg:
```
makepkg -si
```
This will automatically compile the script, install dependencies, and set up the Pacman hook.


###Method 2: Quick Manual Install
If you prefer to install it manually without using python-setuptools:

Copy the script to your local bin and make it executable:
```
sudo cp aur-shield /usr/bin/aur-shield
sudo chmod +x /usr/bin/aur-shield
```
Setup the Pacman hook manually:
```
sudo mkdir -p /etc/pacman.d/hooks
sudo cp aur-hunter.hook /etc/pacman.d/hooks/
```
Usage & Commands
Once installed, the background Pacman hook works completely automatically during every yay, paru, or pacman upgrade.

However, you can manage the tool manually using the CLI:

Check System Status:
```
aur-shield --status
```
Sync & Update Malware Signatures:
```
aur-shield --update
```
Manually Pipe a Package Check:
```
echo "package-name" | aur-shield --check
```
Logs & Signatures
Local Logs: Saved to ``` ~/.cache/aur-shield.log ``` if any critical threats are blocked.
Custom Rules: You can modify or add your own regex rules in ```~/.config/aur-shield/signatures.txt```
