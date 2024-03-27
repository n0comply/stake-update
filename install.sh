cd /root
mkdir logs
cd /root/scripts &&
chmod +x pm2stake.exp && ./pm2stake.exp
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib &&
chmod +x runsheets.sh &&
./runsheets.sh
