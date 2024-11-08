# BlindSSRF
BlindSSRF Tool
# NO MORE NGROK AND DIFFICULTIES

Blind SSRF OOB (Out Of Bound)

After spending considerable time struggling with Ngrok during my penetration tests—facing EDR preventions and being disrupted by confirmation buttons that hindered the execution of Blind SSRF PoCs—I decided to create a solution that would save time and effort for anyone else encountering similar roadblocks.

The tool leverages **Seveo.net** as an alternative to Ngrok, offering a simpler and more efficient way to expose local services to the internet for Blind SSRF OOB testing. With Seveo.net, you can bypass the common disruptions of Ngrok while ensuring a smooth testing experience.

This tool is designed to streamline the process of conducting Blind SSRF PoCs, especially in situations where Ngrok may fall short. By providing an easy-to-use, secure, and efficient way to manage your OOB requests, it helps you focus more on your testing and less on workarounds.

![image](https://github.com/user-attachments/assets/1bc7f03e-77a7-43fa-a0ce-7cb5810f5ffd)


## Have you heard about [SERVEO.NET](http://SERVEO.NET) ?

> After I’ve cleared myself why we should try other tools let’s interduce you with SERVEO.
> 

Serveo is an SSH server just for remote port forwarding. When a user connects to Serveo, they get a public URL that anybody can use to connect to their localhost server.

### How it Works ?
![2](https://github.com/user-attachments/assets/7bde9e96-20b4-456c-9487-f22a5e73cda3)



> Using SSH -R to forward the ports towards [seveo.net](http://seveo.net) server for connections tunneling as ngrok actually does…
> 

# **Advantages Of Using SERVEO.**

1. EDRs and other security measures do not detect these, it could be great also for infrastructure tunneling.
2. No annoying NGROK button for confirmation of visiting files in the server.
3. Crossplatform competability Windows, Linux/Unix.
4. Using SSH for encryptions.
5. Could be useful for creating private connections with asymmetric keys.
6. Bunch of advatanges but you’ve already understood that it beats up NGROK.
7. No need of installation , SSH is usable by default and known as good communication channel to the security measures.

**No Dependencies Are Needed.**

git clone it from my repository or just download the zip file

Windows: python.exe [blindssrf.py](http://blindssrf.py) 

Linux: python blindssrf.py

### Step 1 — Follow The Screenshot Instructions Below:

![7](https://github.com/user-attachments/assets/8e05a340-9c71-4e87-836d-9dc234cffec6)

### Step 2 — Validate That The HTML Was Created Resides In The Current Execution Directory, Review It And Modify it As You Wish:

![8](https://github.com/user-attachments/assets/7f527ec2-08c7-4194-9501-6324cc9514c8)


### Step 3 — Terminals Will Pop, Copy The OutPut Of The SSH Command In Green And Send To The Application:
![9](https://github.com/user-attachments/assets/fd4a50a9-6f0a-4e8d-a396-05ca3220731f)

![10](https://github.com/user-attachments/assets/a0871160-b8d9-4d7c-a0ba-f58b1b1fdc17)


### Step 4 — Await For Incoming HTTP Requests In The Collaborator:

![11](https://github.com/user-attachments/assets/6e50d923-9876-4fb1-8bdf-dc4815abbfb0)

# Installation:
**If you found it useful and you want to save the script in the environment variable and run it as “blindssrf” in the terminal use the following setup:**
**python.exe [setup.py](http://setup.py).**
