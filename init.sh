project_path=`pwd`
interpreter_python_path='python'
project_domain='0.0.0.0'

# read -p "Enter path to the python interpreter: " interpreter_python_path
# read -p "Enter the project domain: " project_domain
# $interpreter_python_path -m venv env
# source ./env/bin/activate
# pip install -U pip
# pip install -r requirements.txt

cp -f copy/nginx.conf etc/
cp -f copy/gunicorn.service systemd/

sed -i "s~template_path~$project_path~g" ./etc/nginx.conf ./systemd/gunicorn.service
sed -i "s~template_domain~$project_domain~g" ./etc/nginx.conf

sudo ln -sf $project_path/etc/nginx.conf /etc/nginx/sites-enabled/
sudo ln -sf $project_path/systemd/gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl enable gunicorn
sudo service nginx restart