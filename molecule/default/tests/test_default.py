import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'openvpn'
PACKAGE_BINARY = '/usr/sbin/openvpn'


def test_openvpn_package_installed(host):
    """
    Tests if openvpn is installed
    """
    assert host.package(PACKAGE).is_installed


def test_openvpn_binary_exists(host):
    """
    Tests if openvpn binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_openvpn_binary_file(host):
    """
    Tests if openvpn binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_openvpn_binary_which(host):
    """
    Tests the output to confirm openvpn's binary location.
    """
    assert host.check_output('which openvpn') == PACKAGE_BINARY
