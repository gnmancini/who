# who else is logged in.
This small program checks if there is a different user than the one logged and send an alert to gnome.


# Installation:
1. cd ~
1. git clone git@github.com:gnmancini/who.git
1. cd who
1. mkdir -p ~/.config/systemd/user/
1. cp ~/who/who.service ~/.config/systemd/user/
1. sed -i 's|username|'$USERNAME'|g' ~/.config/systemd/user/who.service 
1. systemctl --user daemon-reload
1. systemctl --user start who.service
1. systemctl --user status who.service

# Important:
Use this program under your own risk. 
This is just a test.