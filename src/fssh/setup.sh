#!/bin/bash

echo "SETUP \`fssh\`"
echo
echo "To fully automate the SSH login process, please provide your UTCS SSH credentials."
echo
echo "IF USING BASH/ZSH SHELL:"
echo "Enter your credentials into the inputs below, and this script will automatically populate your shell profile."
echo "These will be saved in the environment variables UTCS_USERNAME and UTCS_PASSPHRASE respectively."
echo "If you would like to do this manually, follow the instructions for OTHERWISE"
echo
echo "OTHERWISE:"
echo "Skip past these commands below by leaving them both blank."
echo "You will need to manually set up these variables."
echo "Do this by adding the fields UTCS_USERNAME and UTCS_PASSPHRASE (with correct values) to your shell profile."
echo
read -p "UTCS USERNAME (REQUIRED): " username
read -p "UTCS SSH PASSPHRASE (OPTIONAL): " passphrase

if [ ! -z "$username" ]; then
	if [ "$SHELL" = "/bin/bash" ]; then
		echo "export UTCS_USERNAME=\"$username\"" >>~/.bashrc
	elif [ "$SHELL" = "/bin/zsh" ]; then
		echo "export UTCS_USERNAME=\"$username\"" >>~/.zshrc
	fi
fi

if [ ! -z "$passphrase" ]; then
	if [ "$SHELL" = "/bin/bash" ]; then
		echo "export UTCS_PASSPHRASE=\"$passphrase\"" >>~/.bashrc
	elif [ "$SHELL" = "/bin/zsh" ]; then
		echo "export UTCS_PASSPHRASE=\"$passphrase\"" >>~/.zshrc
	fi
fi

echo
echo "Setup complete."
echo "You may use \`fssh\` now. See \`fssh -h\` for help."
