[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-openvpn.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-openvpn) ![Ansible Role](https://img.shields.io/ansible/role/48387?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/48387?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/48387?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openvpn&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-openvpn) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-openvpn?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-openvpn?color=orange&style=flat-square)

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

Variable              | Value (default) | Description
--------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
openvpn_app           | openvpn         | Defines the app to install i.e. **openvpn**
openvpn_desired_state | present         | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
