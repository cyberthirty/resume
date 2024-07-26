from flask import Flask, request, render_template_string
import dns.resolver
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/enumerate', methods=['POST'])
def enumerate_subdomains():
    domain = request.form['domain']
    wordlist = request.files['wordlist']

    # Save uploaded wordlist temporarily
    wordlist_path = 'temp_wordlist.txt'
    wordlist.save(wordlist_path)

    results = []

    try:
        with open(wordlist_path, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]

        for subdomain in subdomains:
            full_domain = f"{subdomain}.{domain}"
            try:
                dns.resolver.resolve(full_domain, 'A')
                results.append(f'<div class="alert alert-success">[*] {full_domain} found</div>')
            except dns.resolver.NoAnswer:
                results.append(f'<div class="alert alert-danger">[*] {full_domain} not found</div>')
            except dns.resolver.NXDOMAIN:
                results.append(f'<div class="alert alert-danger">[*] {full_domain} not found</div>')
            except Exception:
                results.append(f'<div class="alert alert-danger">[*] {full_domain} error</div>')
    finally:
        os.remove(wordlist_path)

    return ''.join(results)

if __name__ == '__main__':
    app.run(debug=True)
