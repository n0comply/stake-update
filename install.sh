sudo apt install expect
cd /root/stake-update/
mkdir logs
cd /root/stake-update/scripts &&
chmod +x pm2stake.exp && ./pm2stake.exp
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib &&
chmod +x runsheets.sh &&
./runsheets.sh
