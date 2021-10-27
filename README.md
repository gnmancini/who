# who else is logged in.
This small program checks if there is a different user than the one logged and send an alert to gnome.


# Installation:
Clone the repository.
mkdir ~/who
mkdir -p ~/.config/systemd/user/
cp ~/who/who.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user start who.service
systemctl --user status who.service

# Important:
Use this program under your own risk. 
This is just a test.