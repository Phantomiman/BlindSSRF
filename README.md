# BlindSSRF
BlindSSRF Tool
# NO MORE NGROK AND DIFFICULTIES

Blind SSRF OOB (Out Of Bound)

After spending considerable time struggling with Ngrok during my penetration tests—facing EDR preventions and being disrupted by confirmation buttons that hindered the execution of Blind SSRF PoCs—I decided to create a solution that would save time and effort for anyone else encountering similar roadblocks.

The tool leverages **Seveo.net** as an alternative to Ngrok, offering a simpler and more efficient way to expose local services to the internet for Blind SSRF OOB testing. With Seveo.net, you can bypass the common disruptions of Ngrok while ensuring a smooth testing experience.

This tool is designed to streamline the process of conducting Blind SSRF PoCs, especially in situations where Ngrok may fall short. By providing an easy-to-use, secure, and efficient way to manage your OOB requests, it helps you focus more on your testing and less on workarounds.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/8663a8a8-7f6a-45f9-b6c5-610e8c962da6/image.png)

## Have you heard about [SERVEO.NET](http://SERVEO.NET) ?

> After I’ve cleared myself why we should try other tools let’s interduce you with SERVEO.
> 

Serveo is an SSH server just for remote port forwarding. When a user connects to Serveo, they get a public URL that anybody can use to connect to their localhost server.

### How it Works ?

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/b463a825-5fb7-404e-880a-feed615eb2c1/image.png)

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

# Lets Put The Puzzle Together.

### Step 1  — Create The HTML POC File.

![step1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/0bf1a00c-2fd0-4e31-81d1-4eda1a371dbc/step1.png)

### Step 2 — Launch Python Server In The Same Directory The HTML Resides In, And Use ” SSH -R 80:localhost:80 [serveo.net](http://serveo.net) “ In Order To Create The Tunnel.

![2024-10-29_18-05-50.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/13ae07d5-d7f7-4d38-9d6c-56b75c61a5c9/2024-10-29_18-05-50.png)

### Step 3 — Use The Public URL From The Output Of SSH Command.

![06.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/860b546d-80e2-462d-9119-28c3ce3bb3ee/06.png)

### Step 4 — Once Connection Detected It Will Be Mentioned In The Terminal.

![2024-10-29_18-13-06.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/0323ad16-f8f3-40aa-bb37-3bf8681ad264/2024-10-29_18-13-06.png)

# Great Now Let’s Automate It with The Script blindssrf.py:

> In order to boost the progress i’ve started programming this mini script but after some difficulties I’ve asked our friend ChatGPT to assist me:
> 

**No Dependencies Are Needed.**

git clone it from my repository or just download the zip file

Windows: python.exe [blindssrf.py](http://blindssrf.py) 

Linux: python blindssrf.py

### Step 1 — Follow The Screenshot Instructions Below:

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/05d9c76e-3088-45db-951f-10b2d4eb69c6/image.png)

### Step 2 — Validate That The HTML Was Created Resides In The Current Execution Directory, Review It And Modify it As You Wish:

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/fe5423c9-6347-4a92-be8e-df605ddc4609/image.png)

### Step 3 — Terminals Will Pop, Copy The OutPut Of The SSH Command In Green And Send To The Application:

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/dd683bd3-1633-4682-a5ae-4b8cc86a1466/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/603d8c7d-fa63-4cd4-9d23-7228aeacb901/image.png)

### Step 4 — Await For Incoming HTTP Requests In The Collaborator:

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/2f5ab48c-ebee-4a37-97ce-07e9141edabb/65e5adbb-4fde-4a93-a2db-70ffef0a9fef/image.png)

# Installation:

**If you found it useful and you want to save the script in the environment variable and run it as “blindssrf” in the terminal use the following setup:**

**python.exe [setup.py](http://setup.py).**
