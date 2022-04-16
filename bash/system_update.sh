#!/bin/bash
# Developer: NR-SkaterBoy
# Github: https://github.com/NR-SkaterBoy
# E-mail: nr.rick.dev@gmail.com
# Linux Systems source package update

# Help menu
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
    echo " "
    echo "Supported OS:"
    echo -e "\t1.\tUbuntu\t\t\t2.\tKali Linux"
    echo -e "\t3.\tFedora\t\t\t4.\tRaspbian"
    exit
fi

# *** Linux Types *** #
# Just Supported Systems
# Debian: Ubuntu|Kali|Raspbian|Sparky
# RPM: Fedora - Later

git pull
shell=True

# Linux version ID
. /etc/os-release

# Password
# PASSWD=$(zenity --password --title=authentication)
export SUDO_ASKPASS="bash/pass.sh"

case "$ID" in
    "ubuntu" | "kali" | "raspbian" | "sparky") # Ubuntu-Kali-Raspbian-Sparky
        if zenity --question --title="APT Update" --text="Would you like to run apt update?" --no-wrap; then
            sudo -A apt update
        fi

        if zenity --question --title="APT Upgrade" --text="Would you like to run apt upgrade?" --no-wrap; then
            sudo -A apt upgrade -y
        fi
        
        if zenity --question --title="APT Autoremove" --text="Would you like to run apt autoremove?" --no-wrap; then
            sudo -A apt autoremove -y
        fi
        sudo -A apt --fix-broken install
    ;;
    *)
        zenity --error --title="Error" --text="Update failed!\nPlease check the supported systems or your internet connection!" --no-wrap
        exit
    ;;
esac
# System restart
if zenity --question --title="Restart" --text="Please restart the system!\n\nWould you like to restart the system?" --no-wrap; then
    sudo -A shutdown -r now
fi