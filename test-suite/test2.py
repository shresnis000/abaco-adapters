import docker
import timeit
import time
import requests

cli = docker.APIClient('unix://var/run/docker.sock')
dname = 'testin'
start_timer = timeit.default_timer()
cont = cli.create_container(image='nshresth/flask-helloworld', name=dname, ports=[5000], host_config=cli.create_host_config(port_bindings={5000: None}))
container = cli.start(container=cont.get('Id'))
idx = 0
while idx<25:
    try:
        port=cli.inspect_container(cont.get('Id'))['NetworkSettings']['Ports']['5000/tcp'][0]['HostPort']
        break
    except:
        idx = idx+1
        time.sleep(1)
sent_request = timeit.default_timer()
r = requests.get(f'http://localhost:{port}')
got_response = timeit.default_timer()
cli.kill(dname)
cli.prune_containers()
end_timer = timeit.default_timer
time_data = {'total': (end_timer - start_timer) * 1000,
                     'get_response': (got_response - sent_request) * 1000,
                     'initialization': (sent_request - got_response) * 1000,
                     }

print(time_data)