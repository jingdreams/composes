#!/usr/bin/python3
import sys
import os

if len(sys.argv) == 1 or len(sys.argv) > 2:
    sys.exit('请输入：pomelo-admin/pomelo-merchant/pomelo-payment')

if sys.argv[1] == 'pomelo-admin':
    project = (sys.argv[1], '9081', '8089')
elif sys.argv[1] == 'pomelo-merchant':
    project = (sys.argv[1], '9082', '8180')
elif sys.argv[1] == 'pomelo-payment':
    project = (sys.argv[1], '9080', '8080')
elif sys.argv[1] == 'product-center':
    project = (sys.argv[1], '9090', '9090')
else:
    sys.exit('请输入：pomelo-admin/pomelo-merchant/pomelo-payment')


def docker_etc(app, port1, port2):
    os.system('docker stop %s' % app)
    os.system('docker rm %s' % app)
    os.system('docker rmi %s:1.0-SNAPSHOT' % app)
    os.system(
        'docker build -f /mydata/pay/%s/Dockerfile -t %s:1.0-SNAPSHOT /mydata/pay/%s' % (app, app, app))
    os.system(
        'docker run --cap-add=SYS_PTRACE -p %s:%s --name %s -v /etc/localtime:/etc/localtime -v /mydata/logs/%s:/var/logs --net root_net -d %s:1.0-SNAPSHOT' % (port1, port2, app, app, app))


if __name__ == '__main__':
    app = sys.argv[1]

    port1 = project[1]
    port2 = project[2]
    docker_etc(app, port1, port2)
    