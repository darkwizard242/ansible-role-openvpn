import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openvpn_package_installed(host):
    assert host.package("openvpn").is_installed


def test_openvpn_binary_exists(host):
    assert host.file('/usr/bin/openvpn').exists


def test_openvpn_binary_file(host):
    assert host.file('/usr/bin/openvpn').is_file


def test_openvpn_binary_which(host):
    assert host.check_output('which openvpn') == '/usr/bin/openvpn'
