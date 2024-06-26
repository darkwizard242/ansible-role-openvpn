[![build-test](https://github.com/darkwizard242/ansible-role-openvpn/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-openvpn/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-openvpn/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-openvpn/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/openvpn) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openvpn&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openvpn) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openvpn&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openvpn) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openvpn&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openvpn) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-openvpn?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-openvpn?color=orange&style=flat-square)

# Ansible Role: openvpn

Role to install (_by default_) [openvpn](https://openvpn.net/) package or uninstall (_if passed as var_) on **Debian** family and **EL** family systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
openvpn_app: openvpn
openvpn_desired_state: present
```

### Variables table:

Variable              | Description
--------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
openvpn_app           | Defines the app to install i.e. **openvpn**
openvpn_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **openvpn** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openvpn
```

For customizing behavior of role (i.e. installation of latest **openvpn** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openvpn
  vars:
    openvpn_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **openvpn** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openvpn
  vars:
    openvpn_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-openvpn/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
