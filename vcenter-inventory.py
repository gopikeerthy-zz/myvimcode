# This script will  print the ESXi hosts,  vms, datastores names
from pyVmomi import vim
from pyvim import connect
import atexit

vc_name = '40.40.40.10' # use ip or FQDN
print("hello")
pass_vcuser = "xxxxx" # use your password 
vc_user = 'administrator@vsphere.local' # use a vcenter user 

def vc_connect():
    print('Connecting to vCenter.....', vc_name)
    s_instance = connect.SmartConnectNoSSL(host=vc_name, user=vc_user, pwd=pass_vcuser, port=443)
    root_content = s_instance.RetrieveContent()
    return root_content

# print(vc_connect())
# Method that populates objects of type vimtype
def get_all_objs(content1, vimtype):
        objs = {}
        container = content1.viewManager.CreateContainerView(content1.rootFolder, vimtype, True)
        for managed_object_ref in container.view:
                objs.update({managed_object_ref: managed_object_ref.name})
        return objs

content = vc_connect()

# For ESXi host
hosts = get_all_objs(content, [vim.HostSystem])
# For datacenters
dcs = get_all_objs(content, [vim.Datacenter])
# For datastores
datastores = get_all_objs(content, [vim.Datastore])
# For Virtual Networks/Portgroups
vnetworks = get_all_objs(content, [vim.Network])
# For VMs
vms = get_all_objs(content, [vim.VirtualMachine])
# This will print the vms, hosts, datastores, datacenter names
for h in hosts:
    print(h.name)
for d in dcs:
    print(d.name)
for ds in datastores:
    print(ds.name)
for v in vms:
    print(v.name)
for n in vnetworks:
    print(n.name)
# The below will print the MOB ref ID's also, if need we can enable
# print(vms)
# print(dcs)
# print(datastores)
# print(hosts)
# print(vnetworks)
atexit.register(connect.Disconnect, content)





