import json
import jinja2

# Template file at ./app/templates/example.json
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "config.json"
templateEnv.filters['jsonify'] = json.dumps
template = templateEnv.get_template(TEMPLATE_FILE)

globalconfig = {
    "server": "dev",
    "primary_site_admin_tenant_base_url": "https://admin.develop.tapis.io",
    "service_tenant_id": "admin",
    "service_name": "abaco",
    "service_password": "",
    "service_site_id": "tacc",
    "tenants": [
        "tacc",
        "dev",
        "admin"
    ],
    "version": "dev",
    "log_file": "/home/tapis/runtime_files/logs/service.log",
    "log_level": "DEBUG",
    "log_filing_strategy": "split",
    "tapisservice.auth_log_file": "/home/tapis/runtime_files/logs/tapisservice.log",
    "tapisservice.log_log_file": "/home/tapis/runtime_files/logs/tapisservice.log",
    "mongo_host": "mongo_host",
    "mongo_port": 27017,
    "mongo_replica_set": True,
    "mongo_tls": False,
    "mongo_tls_ca_cert_name": "ca.pem",
    "mongo_tls_client_cert_name": "client.pem",
    "mongo_tls_certs_path": "$env{abaco_host_path}/runtime_files/certs:/home/tapis/runtime_files/certs",
    "admin_mongo_user": "admin",
    "admin_mongo_pass": "admin",
    "rabbit_uri": "amqp://rabbit:5672",
    "rabbit_dash_host": "rabbit",
    "admin_rabbitmq_user": "admin",
    "admin_rabbitmq_pass": "admin",
    "spawner_abaco_conf_host_path": "$env{abaco_host_path}/config-local.json",
    "spawner_host_id": 0,
    "spawner_host_queues": [
        "default",
        "special"
    ],
    "spawner_host_ip": "10.160.32.167",
    "spawner_max_cmd_length": 10,
    "spawner_max_workers_per_host": 75,
    "spawner_max_workers_per_actor": 6,
    "spawner_docker_network": "abaco_abaco",
    "docker_dd": "unix://var/run/docker.sock",
    "worker_init_count": 1,
    "worker_autoscaling": True,
    "worker_max_run_time": -1,
    "worker_max_cpus": 1000000000,
    "worker_worker_ttl": 86400,
    "worker_sync_max_idle_time": 600,
    "worker_auto_remove": True,
    "worker_privileged_mounts": [
        "$env{abaco_host_path}/runtime_files/data1:/home/tapis/runtime_files/_abaco_data1:ro",
        "$env{abaco_host_path}/runtime_files/data2:/home/tapis/runtime_files/_abaco_data2:rw"
    ],
    "worker_leave_containers": False,
    "worker_socket_paths": "$env{abaco_host_path}/runtime_files/_abaco_results_sockets:/home/tapis/runtime_files/_abaco_results_sockets",
    "worker_fifo_paths": "$env{abaco_host_path}/runtime_files/_abaco_fifos:/home/tapis/runtime_files/_abaco_fifos",
    "web_encryption_key": "djq6ghD6YMWU43TyxGy58pmw_I2hfroAvcbqz9kV23o=",
    "web_access_control": "jwt",
    "web_user_role": "Internal/everyone",
    "web_accept_nonce": True,
    "web_apim_public_key": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCUp/oV1vWc8/TkQSiAvTousMzOM4asB2iltr2QKozni5aVFu818MpOLZIr8LMnTzWllJvvaA5RAAdpbECb+48FjbBe0hseUdN5HpwvnH/DW8ZccGvk53I6Orq7hLCv1ZHtuOCokghz/ATrhyPq+QktMfXnRS4HrKGJTzxaCcU7OQIDAQAB",
    "web_show_traceback": False,
    "web_max_log_length": 1000000,
    "web_case": "camel",
    "web_max_content_length": 500000000,
    "web_all_queues": [
        "default",
        "special"
    ],
    "site_id": "tacc",
    "global_site_object": {
        "site_mongo_pass": "defaultpass",
        "site_rabbitmq_pass": "defaultpass"
    },
    "tacc_site_object": {
    },
    "global_tenant_object": {
        "log_ex_limit": 86400,
        "log_ex": 43200,
        "use_tas_uid": False,
        "default_token": False,
        "generate_clients": True
    },
    "tacc_tenant_object": {
        "use_tas_uid": False,
        "default_token": False,
        "generate_clients": True,
        "global_mounts": [
        ]
    },
    "designsafe_tenant_object": {
        "actor_uid": 458981,
        "actor_gid": 816877,
        "global_mounts": [
            "$env{abaco_host_path}/runtime_files/data1:/home/tapis/runtime_files/_abaco_data1:ro",
            "$env{abaco_host_path}/runtime_files/data2/{tenant_id}/{username}:/home/tapis/runtime_files/_abaco_data2:rw"
        ]
    },
    "sd2e_tenant_object": {
        "use_tas_uid": True
    },
    "dev_tenant_object": {
        "global_mounts": [
            "$env{abaco_host_path}/runtime_files/data1:/home/tapis/runtime_files/_abaco_data1:ro"
        ]
    }
}

p=template.render(globalconfig=globalconfig)

with open('config-local.json', 'w') as json_file:
  json_file.write(p)