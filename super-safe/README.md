# Super Safe README

This challenge is a web exploitation challenge that involves manipulating the username,
X-Forwarded-For, and user-agent string to create a session cookie that matches the
admin user’s structure. By controlling these inputs, an attacker aims to simulate
a valid admin session and gain unauthorized access. Because the cookies have quite
fast expiration times, the attacker may rely on automating the process to achieve
this.

## File Structure

- `app.py`: The web server code for the challenge.
- `init_db.py`: The script to initialize the database (including setting up the admin
  user).
- `Dockefile`: The Dockerfile for building the challenge image.
- `problem.md`: The problem statement for the challenge (parsed by `cmgr`).
- `solver/solve.py`: The solution script for the challenge.
- `README.md`: This file.

## Setup with `cmgr` (borrowed from example picoCTF challenges)

1. You have `cmgr` installed and configured.

   - Refer to the [setup page](https://github.com/picoCTF/start-problem-dev/blob/master/setup-cmgr.md)
     if this is not the case for you.

2. copy this challenge directory to the `cmgr/challenges` directory (or other directories
   that `CMGR_DIR` environment variable points to).

3. Run `cmgr update` and `cmgr playtest picoctf/ronghaon/super-safe`
   - You should have some similar output as below:

    ```bash
    cmgr: [WARN:  disk quota for picoctf/ronghaon/super-safe container 'challenge' ignored (disk quotas are not enabled)]
    challenge information available at: http://localhost:4242/
    ```

4. Visit the link provided in the output to access the challenge.

## Vulnerability

The vulnerability in this challenge lies in the server's cookie handling mechanism.
The server uses a cookie to store the user's session information, including the username
and whether the user is an admin. The server checks the cookie to determine if the
user is an admin and grants access to the flag accordingly.

The cookie has the following structure:

```text
{timestamp}+++{uuid}+++{user_id}+++{user_ip}+++{user_agent_string}
```

The server encrypts this cookie using a secret key and sends it to the client. The
client sends this cookie back to the server with each request. The server decrypts
the cookie, extracts the user information, and checks if the user is an admin.

Here, an attacker can manipulate the username and user-agent string to login and
receive a cookie that matches the admin user's structure. However, the attacker may
not know its IP address in the server's network. To bypass this, the attacker can
manipulate the `X-Forwarded-For` header to set the IP address to the server's IP
address. By controlling these inputs, an attacker aims to simulate a valid admin
session and gain unauthorized access to the flag. Because the cookies have quite
fast expiration times, the attacker may only achieve this by automating the process.

## Possible Solution

See `solver/solve.py` for a possible solution to this challenge.
