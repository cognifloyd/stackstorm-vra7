# vRealize Automation 7 Integration Pack

Stackstorm VMware vRealize Automation 7 Integration Pack

## Configuration

Copy the example configuration in [vra7.yaml.example](./vra7.yaml.example)
to `/opt/stackstorm/configs/vra7.yaml` and edit as required.

```yaml
---
hostname: cloud.company.local
username: administrator@vsphere.local
password: VMware1!
tenant: vsphere.local
verify_ssl: false
```

You can also use the [datastore](https://docs.stackstorm.com/datastore.html) to store values
such as the password. In your `vra7.yaml` file, use `password: "{{st2kv.system.vra7_password}}"`

Store the password in the datastore with `st2 key set vra7_password "VMware1!" --encrypt`

The included script [vra7config.py](./vra7config.py) can be used to interactively create the
configuration file, and automatically store the password in the datastore.

## Actions

* `get_all_requests` - List all catalog requests
* `get_resource_by_name` - Get resource details by name
* `get_number_of_vms` - Get number of VMs

## Aliases

All the above actions have matching ChatOps aliases:

* `get all vra7 requests"
* `get details about {{resourceName}}` or `tell me about {{resourceName}}`
* `How many vms are in vra` or `Tell me how many vms are in vra`
