# Super Safe

- Namespace: picoctf/18739f24
- ID: super-safe
- Type: custom
- Category: Web Exploitation
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Description

This website is super safe with the customized cookies! No one can steal the flag from the server!

## Details

Browse {{link_as('/', 'here')}}, and find the flag! Download the web server code {{url_for("app.py", "here")}}.

## Hints

- Look for what can be manipulated.
- Let the server believe that you are the admin.

## Solution Overview

The solution involves manipulating the username, X-Forwarded-For, and user-agent string to create a session cookie that matches the admin user’s structure. By controlling these inputs, an attacker aims to simulate a valid admin session and gain unauthorized access. Because the cookies have quite fast expiration times, the attacker may only achieve this by automating the process.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Understand cookies and HTTP headers.

## Tags

## Attributes

- author: Ronghao Ni
- organization: picoCTF
- event: 18739-D Assignment
