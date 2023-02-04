sudo apt install unclutter python3-pip python3-pygame python3-dbus awesome
sudo pip install -r requirements.txt
chmod +x load.sh
mkdir -p /home/chip/.config/awesome/
ln rc.lua /home/chip/.config/awesome/rc.lua
#Restart awesome and it should load directly to the new menu:
echo 'awesome.restart()' | awesome-client
