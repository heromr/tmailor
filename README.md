<div align="center">
  <h1 style="color: #0d47a1; font-size: 3em;">tmailor</h1>
  
  <p>
    <a href="https://github.com/heromr/tmailor/commits/main"><img src="https://img.shields.io/github/last-commit/heromr/tmailor?label=last%20updated&color=blueviolet" alt="GitHub last commit"></a>

  <p style="font-size: 1.2em; color: #424242;">A temporary email address that provides email addresses without registration, used to receive incoming emails without disclosing your actual email.</p>

  
  <h2 style="color: #0d47a1; font-size: 2em;">Installation</h2>
  
  <p style="font-size: 1.2em; color: #424242;">Recommended installation method is through pip:</p>
  
  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">pip install tmailor</code></pre>
  
  <p style="font-size: 1.2em; color: #424242;">Alternatively, you can clone the repository and install it manually:</p>
  
  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">git clone https://github.com/heromr/tmailor.git
  cd tmailor
  python setup.py install</code></pre>
  
</div>

<div>
  <h2 align="center">Client Class Usage</h2>

  <pre><code class="language-python">
from tmailor import Client

# Create an instance of the Client class
client = Client()

# Generate a random email address
random_email = client.generate_random_email()
print("Random Email Address:", random_email.email)

# Generate a custom email address
custom_email = client.generate_custom_email("john", "example.com")
print("Custom Email Address:", custom_email.email)

# Delete an email address
response = client.delete_email(random_email.email, random_email.token)
print("Deletion Response:", response)

# Get messages for an email address
messages = client.get_messages(random_email.email)
for message in messages.messages:
    print("Subject:", message.subject)
    print("Sender:", message.sender)
    print("Content:", message.body_text)
    print()

# Get a list of available domains
domains = client.get_domains()
for domain in domains.name:
    print("Domain:", domain)
  </code></pre>
</div>
