project_path=`pwd`
interpreter_python_path='python'
project_domain='0.0.0.0'

sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"

cp -f copy/nginx.conf etc/

sed -i "s~template_path~$project_path~g" ./etc/nginx.conf
sed -i "s~template_domain~$project_domain~g" ./etc/nginx.conf

sudo ln -sf $project_path/etc/nginx.conf /etc/nginx/sites-enabled/
sudo service nginx restart

cd ./ask/
python3 manage.py makemigrations qa
python3 manage.py migrate
gunicorn --bind=0.0.0.0:8000 --workers=2 --timeout=15 --log-level=debug ask.wsgi:application